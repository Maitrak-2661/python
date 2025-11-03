
Project:pr final happiness report


1. Overview
This project analyzes the 2015 World Happiness Report to identify and visualize the relationships between a nation's reported happiness and key socio-economic factors.

The analysis focuses on the correlations between the Happiness Score and the following three variables:

GDP per Capita

Social Support

Healthy Life Expectancy

2. Dataset
Source: World Happiness Report (2015)

File: 2015.csv

3. Requirements
All required Python libraries are listed in the requirements.txt file.

To install them, run:

Bash

pip install -r requirements.txt
4. Usage
Ensure you have 2015.csv, analysis.py, and requirements.txt in the same project directory.

Install the required packages (see section 3).

Run the analysis script from your terminal:

Bash

python analysis.py
The script will:

Print the top 10 happiest countries to the console.

Create a new directory named outputs/ (if it doesn't already exist).

Save all visualization .png files into the outputs/ directory.

5. Key Findings (from Visualizations)
happiness_pairplot_2015.png: The pairplot provides a high-level overview, showing clear positive, linear relationships between the Happiness Score and all three key variables (GDP, Social Support, and Life Expectancy).

Individual Scatter Plots: The regplot visualizations confirm the pairplot's findings, showing strong positive correlations. As GDP, social support, and life expectancy increase, the happiness score tends to increase as well.

📄 requirements.txt
pandas
matplotlib
seaborn