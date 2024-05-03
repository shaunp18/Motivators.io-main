# Employee Satisfaction Report Generator

## Overview
This Python script generates an **Employee Satisfaction Report**. It collects user ratings on various aspects of their work environment across different categories and compiles these into a comprehensive report. The report is presented in PDF format, including graphical representation of average ratings per category.

## Features
- Interactive user input for rating different job satisfaction categories.
- Detailed textual report generation based on user ratings.
- Visualization of average ratings with a bar graph.
- Export of the report and graph to a PDF file.

## Requirements
- **Python 3.x**
- **Matplotlib**
- **ReportLab**

## Installation
Ensure **Python 3.x** is installed on your system. If not, download and install from [Python's official site](https://www.python.org/downloads/).

Install the required Python packages:
~~~bash
pip install matplotlib
pip install reportlab
~~~

## Usage
1. Run the script: `python employee_satisfaction_report.py`
2. Rate each category from 0 (Not at all important) to 5 (Extremely important).
3. After all inputs, the script generates 'Employee_Satisfaction_Report.pdf'.
4. Open the PDF to view the report and graphical analysis.

## Categories Included
- Benefits and Wellness
- Building and Innovating
- Career Growth and Development
- Compensation
- Culture and Values
- Executive Leadership
- Flexible Work
- Inclusion and Social Connection
- Job Security and Stability
- Manager Relationship
- Meaningful Work
- Personal Impact

## Customization
Customize the script by editing the `categories` and `report_messages` dictionaries to add or modify categories.

## Notes
- Install all dependencies before running the script.
- The script uses a command-line interface.
- The generated PDF is saved in the script's directory.

## License
All rights to this code are reserved for Motivators.io
