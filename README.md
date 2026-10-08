# LDR Sensor Data Logger Using Arduino and Python

## Overview
This project records light-dependent resistor (LDR) readings using an Arduino Uno and analyses the collected data with Python, Pandas, and Matplotlib. Readings were collected under three experimental conditions: room light, covered sensor, and flashlight illumination.

## Objectives
- Interface an LDR voltage-divider circuit with an Arduino analog input.
- Collect timestamped sensor readings over the serial connection.
- Organize the experiment data into CSV format.
- Calculate summary statistics and visualize the readings.

## Hardware
- Arduino Uno
- LDR (light-dependent resistor)
- 10 kΩ resistor
- Breadboard and jumper wires
- USB cable for programming and serial data

## Circuit
Connect the components as follows:

`5V -> LDR -> A0 -> 10 kΩ resistor -> GND`

The junction between the LDR and the 10 kΩ resistor connects to analog input A0. The exact readings depend on the LDR, resistor, lighting, and circuit arrangement.

## Software
- Arduino IDE
- Python 3
- pandas
- matplotlib

## Repository Structure
```text
LDR-Sensor-Data-Logger/
├── Arduino/
│   └── ldr_logger.ino
├── Data/
│   └── ldr_data.csv
├── Python/
│   └── ldr_analysis.py
├── Results/
│   ├── ldr_light_conditions.png
│   └── ldr_summary.csv
└── README.md
```

## How to Run the Arduino Logger
1. Wire the LDR voltage divider as described above.
2. Open `Arduino/ldr_logger.ino` in Arduino IDE.
3. Select Arduino Uno and the correct serial port.
4. Upload the sketch.
5. Open Serial Monitor at **9600 baud**.
6. The sketch prints timestamp and raw LDR readings about once per second.

The included CSV contains the experimental readings used for this analysis. The data was grouped by lighting condition based on the experiment notes/screenshots.

## How to Run the Python Analysis
Install the dependencies:

```bash
python -m pip install pandas matplotlib
```

Run the script from the project folder:

```bash
python Python/ldr_analysis.py
```

The script prints count, minimum, maximum, mean, median, and standard deviation for each condition. It also creates/updates the graph and summary CSV in `Results/`.

## Experimental Results
The included dataset contains **84 readings**:
- Room Light: 34 readings
- Covered: 25 readings
- Flashlight: 25 readings

| Condition | Count | Minimum | Maximum | Average |
|---|---:|---:|---:|---:|
| Covered | 25 | 102 | 115 | 110.36 |
| Room Light | 34 | 490 | 523 | 509.91 |
| Flashlight | 25 | 839 | 948 | 925.60 |

The readings clearly differ across the three tested conditions. These values are raw ADC readings, not calibrated lux measurements. The average values are specific to this circuit and test setup.

## Limitations and Future Improvements
- Collect a controlled experiment with equal sample counts and consistent lighting duration.
- Calibrate the sensor against a light meter if measurements in lux are required.
- Add automatic condition labels or threshold-based light classification.
- Stream readings directly into a file for longer experiments.
- Add a timestamp in seconds and improve the plot with condition-specific time windows.

## Skills Demonstrated
Arduino, Embedded C/C++, analog sensor interfacing, serial communication, CSV data handling, Python, Pandas, Matplotlib, basic statistical analysis, and technical documentation.

## Author
Anand Muddannavar
