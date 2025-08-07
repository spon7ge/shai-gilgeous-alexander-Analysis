# 🏀 Shai Gilgeous-Alexander Career Analysis (2018–2025)

Welcome! This repository contains a comprehensive analysis of Shai Gilgeous-Alexander's NBA career from his rookie season in 2018 through the current 2024-25 season. The goal of this project is to explore the development, performance trends, and key statistical insights of one of the NBA's rising stars.

## Overview

Shai Gilgeous-Alexander (SGA) entered the NBA in 2018 and has since evolved into a franchise cornerstone for the Oklahoma City Thunder. This analysis investigates:

- **Career trajectory analysis** with detailed performance trends
- **Shooting evolution** including shot charts and spatial analysis  
- **Advanced metrics** (PER, TS%, Usage Rate, etc.)
- **Predictive modeling** for future performance
- **Shot selection and efficiency** across different zones and situations
- **Year-over-year development** in all major statistical categories


## 🔧 Key Features

### **Comprehensive EDA (Exploratory Data Analysis)**
- Career performance dashboard with 9-panel visualization
- Statistical trend analysis across 7+ NBA seasons
- Performance consistency metrics and growth rate calculations
- Correlation analysis between different performance metrics

### **Shot Chart Analysis**
- Detailed shooting data from 2018-19 to 2024-25
- Spatial shooting analysis with court zone breakdowns
- Shot type evolution (Jump shots, layups, step-backs, etc.)
- Efficiency heatmaps and success rate tracking

### **Predictive Modeling**
- Linear regression models for 2025-26 season predictions
- Multiple scenario analysis (conservative, optimistic, trend-based)
- Model performance evaluation with R² and confidence intervals
- Risk factor assessment for prediction accuracy

### **Advanced Metrics**
- Effective Field Goal Percentage (eFG%) tracking
- Points per shot attempt analysis
- 3-point rate evolution over career
- Zone-based efficiency comparisons

## 🛠️ Technologies Used

- **Python 3.x**
- **NBA API** - Real-time NBA statistics
- **Basketball Reference API** - Historical player data
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Matplotlib/Seaborn** - Data visualization
- **Scikit-learn** - Machine learning models
- **Jupyter Notebook** - Interactive analysis environment

## Key Functions

### `SGA_functions.py` contains:

- `get_players_stats(player_id, season)` - Retrieve basic season statistics
- `get_shot_chart(player_id, year)` - Fetch detailed shot chart data
- `draw_court()` - NBA court visualization utility
- `calculate_per_game_totals()` - Convert totals to per-game averages
- `basketball_reference_adv_data()` - Advanced metrics from Basketball Reference
- Various helper functions for data processing and analysis

## Getting Started

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn
pip install nba_api
pip install scikit-learn
```

### Running the Analysis
1. Clone this repository
2. Install required dependencies
3. Open `SGA.ipynb` in Jupyter Notebook
4. Run cells sequentially to reproduce the analysis

## Key Insights

### Career Highlights
- **Scoring Evolution**: From 10.8 PPG (rookie year) to 30+ PPG (recent seasons)
- **Efficiency Improvement**: Consistent growth in shooting percentages
- **Role Development**: Transition from role player to franchise cornerstone
- **Shot Selection**: Evolution from primarily assisted shots to creating own offense

### Statistical Trends
- Strong positive correlation between usage rate and scoring efficiency
- Consistent improvement in clutch time performance
- Notable development in 3-point shooting accuracy
- Elite performance in mid-range shooting zones

## 2025-26 Predictions

Based on linear regression analysis of career data:
- **Predicted PPG**: [Model output based on trend analysis]
- **Shooting Efficiency**: Continued improvement expected
- **Playmaking**: Enhanced assist numbers projected
- **Model Confidence**: High confidence in core metrics (R² > 0.8)

## Visualizations

The analysis includes:
- **Career dashboard** - 9-panel comprehensive overview
- **Shot charts** - Season-by-season shooting patterns
- **Trend analysis** - Performance evolution over time
- **Predictive charts** - Future performance projections
- **Efficiency heatmaps** - Zone-based shooting analysis

## Future Work

- Integration of defensive metrics analysis
- Team impact and on/off court statistics
- Playoff performance deep dive
- Comparison with other elite guards
- Real-time dashboard updates

## Notes

- Data sourced from official NBA API and Basketball Reference
- Analysis covers regular season performance only
- Some advanced metrics may have limited historical data
- Predictions are based on historical trends and shoul
