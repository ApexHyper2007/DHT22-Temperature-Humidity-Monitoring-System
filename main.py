import csv
import os
import time
from datetime import datetime

import Adafruit_DHT


# Sensor configuration
SENSOR = Adafruit_DHT.DHT22
GPIO_PIN = 18
READ_INTERVAL = 3  # Seconds between reading attempts

LOG_FILE = "sensor_log.csv"
CURRENT_FILE = "current_reading.csv"

CSV_FIELDS = ["timestamp", "temperature_c", "humidity_percent"]


def read_sensor():
    """Read and validate temperature and humidity from the DHT22 sensor."""
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, GPIO_PIN)

    if humidity is None or temperature is None:
        print("Sensor reading failed; will retry.")
        return None

    # Broad plausibility checks for DHT22 measurements.
    if not (-40 <= temperature <= 80 and 0 <= humidity <= 100):
        print("Invalid sensor reading; skipping.")
        return None

    return round(temperature, 2), round(humidity, 2)


def write_reading(filename, reading, append):
    """Write one reading to a CSV file, adding a header when needed."""
    file_exists = os.path.exists(filename) and os.path.getsize(filename) > 0
    mode = "a" if append else "w"

    with open(filename, mode, newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_FIELDS)

        if not append or not file_exists:
            writer.writeheader()

        writer.writerow(reading)


def save_reading(temperature, humidity):
    """Save the reading to the historical log and latest-reading file."""
    reading = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "temperature_c": temperature,
        "humidity_percent": humidity,
    }

    write_reading(LOG_FILE, reading, append=True)
    write_reading(CURRENT_FILE, reading, append=False)


def main():
    print("DHT22 Temperature & Humidity Monitor")
    print(f"GPIO pin: {GPIO_PIN} | Reading interval: {READ_INTERVAL} seconds")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            try:
                result = read_sensor()

                if result is not None:
                    temperature, humidity = result
                    print(
                        f"{datetime.now():%Y-%m-%d %H:%M:%S} | "
                        f"Temperature: {temperature:.2f} °C | "
                        f"Humidity: {humidity:.2f}%"
                    )
                    save_reading(temperature, humidity)

            except (OSError, RuntimeError, csv.Error) as error:
                print(f"Reading or logging error: {error}")

            time.sleep(READ_INTERVAL)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")


if __name__ == "__main__":
    main()
