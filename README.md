# Formula 1 Race Strategy & Performance Analytics

## Project Overview

This project explores Formula 1 race performance and strategy using data collected from the [OpenF1 API](https://openf1.org/), focusing initially on the 2026 Mexico City Grand Prix.

The dataset includes information on all 22 participating drivers and their respective constructors, including lap times, tire stints, pit stops, and race results.

The goal is to investigate how factors such as lap-time consistency, tire selection, and pit-stop strategy relate to race performance. While the initial dataset covers the entire grid, I plan to narrow the analysis to the top three finishers to better understand the differences in their race strategies and what may have contributed to their success.

## Data Collection

Race data is retrieved through the OpenF1 API using Python's `requests` library and organized into CSV files using `pandas`.

The collected datasets include:

- **Drivers:** Driver information and constructor affiliations.
- **Laps:** Individual lap times and sector performance.
- **Stints:** Tire compounds and the number of laps completed on each set.
- **Pit Stops:** Pit-lane events and timing information.
- **Session Results:** Final race classifications.
- **Constructors:** Driver-to-team relationships extracted from the drivers dataset.

The data collection script is located in `scripts/data_download.py`, and the downloaded datasets are stored in `data/raw/`.

## Tools & Technologies

- **Python:** Data collection, processing, and statistical analysis
- **Pandas:** Data manipulation and organization
- **Requests:** API integration
- **Tableau Public:** Planned interactive dashboards and visualizations
- **Git & GitHub:** Version control and project documentation

## Future Development

### 1. Podium Finishers: Race Strategy Comparison

The next stage will focus on comparing the top three finishers at the 2026 Mexico City Grand Prix.

I plan to examine differences in lap-time consistency, tire compound selection, stint lengths, pit-stop timing, and overall race pace to identify patterns that may help explain each driver's performance.

### 2. Kimi Antonelli: Road to the World Championship

I also plan to expand the project beyond a single Grand Prix by analyzing Kimi Antonelli's performance and race strategies throughout the 2026 season.

This analysis will investigate whether his approach to tire management, pit-stop timing, and race consistency remained relatively stable or changed over the course of the season, particularly in the races leading up to his championship result.

Comparing Antonelli's performance with his Mercedes teammate, George Russell, may also provide additional context for understanding differences in race strategy and performance within the same constructor.

### 3. Interactive Data Visualization

I plan to develop an interactive Tableau dashboard to visualize driver performance, race strategy comparisons, and season-long trends.

The dashboard will allow users to explore relationships between lap times, tire strategies, pit stops, and race outcomes.

## Data Source

[OpenF1 API](https://openf1.org/) — An open-source API providing Formula 1 timing, telemetry, and race session data.

## Running the Project

Install the required Python libraries:

```bash
python -m pip install pandas requests
```

Run the data collection script from the project directory:

```bash
python scripts/data_download.py
```

The downloaded data will be saved as CSV files in the `data/raw/` directory.