DHT22 Temperature & Humidity Monitoring System

A Python-based environmental monitoring system that uses the DHT22 digital sensor to measure temperature and relative humidity. The system reads sensor data, displays measurements in the terminal, and records timestamped readings for future analysis.

Project Overview

This project demonstrates basic sensor interfacing, real-time data acquisition, error handling, and data logging using Python and Raspberry Pi GPIO.

Features

Real-time temperature and humidity monitoring

Automatic sensor reading retries

Timestamped data logging in CSV format

Separate files for historical records and the latest reading

Input validation for sensor measurements

Graceful shutdown using Ctrl + C

Hardware Requirements

Raspberry Pi with GPIO support

DHT22 temperature and humidity sensor

Jumper wires

Pull-up resistor, if required by the sensor module

Software Requirements

Python 3

Adafruit DHT Python library

Compatible Raspberry Pi operating system with GPIO access

Hardware Connections

DHT22 Pin

Raspberry Pi Connection

VCC

3.3V

DATA

GPIO 18 (Physical Pin 12)

GND

Ground (GND)

Note: Verify the pin configuration of your particular sensor module before connecting the hardware.

Installation

Clone the repository:

git clone https://github.com/TabletopPants29/DHT22.git
cd DHT22

Install the required sensor library using an installation method compatible with your Raspberry Pi operating system.

Usage

Run the Python script:

python3 main.py

The program continuously reads temperature and humidity, displays valid measurements in the terminal, and saves them to CSV files.

Press Ctrl + C to stop the monitoring process.

Data Logging

The system generates the following files during execution:

sensor_log.csv — Stores historical sensor readings with timestamps.

current_reading.csv — Stores the most recent valid sensor reading.

Each record contains the timestamp, temperature in degrees Celsius, and relative humidity as a percentage. The CSV format allows the collected data to be analyzed using spreadsheet applications or Python data-analysis libraries.

Configuration

The following parameters can be modified in main.py:

GPIO_PIN — GPIO pin connected to the sensor.

READ_INTERVAL — Time interval between successive reading cycles, in seconds.

Error Handling

The program handles unsuccessful sensor readings, validates measurement ranges, reports logging errors, and supports controlled termination. Invalid readings are skipped rather than recorded as valid measurements.

Limitations

Requires compatible physical hardware and GPIO access.

Sensor readings may occasionally fail because of connection issues or sensor limitations.

Data is stored locally; cloud storage and remote monitoring are not implemented.

Future Enhancements

Real-time temperature and humidity visualization

Historical data analysis and reporting

Web-based monitoring dashboard

Configurable threshold alerts

Remote data storage and monitoring
