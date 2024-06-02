# Industry 4.0 exercises
This repository contains the exercises for the Industry 4.0 course of the Master in *Computer Science and Engineering - Intelligent Embedded Systems* at the University of Bologna.

## Assignment 1
Implementation and evaluation of two variants for deploying a pre-trained Artificial Neural Network (ANN) on an embedded device, specifically the Puck.js device, using the Espruino software. The objective is to recognize simple movement gestures using data from an accelerometer.

The two deployment variants considered are:
1. On-board deployment: The sensor data is directly fed to the ANN on the embedded device, and only the results are transmitted.
2. Off-board deployment: The ANN is hosted on an external computation host, while the embedded device transmits raw data to the host via Bluetooth Low Energy (BLE).

The focus is on energy consumption analysis for each variant, crucial for maximizing the lifetime of battery-powered devices. By contrasting the energy profiles of both approaches, we aim to determine the most energy-efficient deployment method.

## Assignment 2
This assignment explores the utilization of gaze data, primarily focusing on visualizing and classifying eye movements into different activities such as reading, inspection, and search.

The provided notebooks offer tools for visualizing gaze data and implementing a basic classifier using a Support Vector Machine (SVM). This classifier utilizes features extracted from eye movement metrics, such as fixation dispersion and duration.

The task involves experimenting with an alternative classifier distinct from the provided SVM and comparing its performance against the SVM results, through metrics like confusion matrices on the provided test dataset.

## Capstone Project
The project main goal is to monitor an electric screwdriver, focusing on movement and temperature measuements to ensure optimal performance and prevent overheating. The project aims to enhance the longevity of the tool through proactive maintenance and timely interventions based on real-time monitoring data.

Key Features:
- Movement Monitoring: Track rotational speed and torque to ensure optimal performance and detect anomalies.
- Temperature Monitoring: Real-time monitoring of thermal conditions to prevent overheating and schedule maintenance.
- Voltage Monitoring: Continuous monitoring of electrical supply to maintain stability and protect internal components.
- Data Collection and Visualization: Utilize Puck.js Bluetooth sensors for data collection and develop a dashboard for real-time visualization of key performance indicators.
- Comprehensive Dashboard: Provides an intuitive overview of temperature, motion/vibration, voltage, Puck.js sensor battery status, and environmental luminosity.

This project offers insights into Industry 4.0 practices for tool monitoring and maintenance, showcasing the integration of sensor technology with advanced data visualization techniques to optimize tool performance and longevity.