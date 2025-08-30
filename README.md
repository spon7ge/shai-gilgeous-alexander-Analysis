# 🏀 Anthony Edwards Career Analysis (2020–2025)

Welcome! This repository contains a comprehensive analysis of Anthony Edwards' NBA career from his rookie season in 2020 through the current 2024-25 season. The goal of this project is to explore the development, performance trends, and key statistical insights of one of the NBA's most explosive young stars.

## Overview

Anthony Edwards was selected 1st overall in the 2020 NBA Draft and has rapidly developed into a franchise cornerstone for the Minnesota Timberwolves. This analysis investigates:

- **Career trajectory analysis** with detailed performance trends across 5 seasons
- **Shooting evolution** including efficiency metrics and spatial analysis  
- **Advanced metrics** (TS%, eFG%, Usage Rate, Net Rating, PIE, etc.)
- **Machine learning predictions** for 2025-26 season performance
- **Shot selection and efficiency** across different zones and game situations
- **Year-over-year development** in all major statistical categories
- **Pace and usage analysis** showing performance in different game contexts

## 🔧 Key Features

### **Comprehensive EDA (Exploratory Data Analysis)**
- Career performance dashboard with 6-panel advanced metrics visualization
- Statistical trend analysis across Anthony Edwards' NBA career (2020-2025)
- Performance consistency metrics and growth rate calculations
- Correlation analysis between different performance metrics
- Usage Rate vs True Shooting% efficiency analysis

### **Multi-Season Data Integration**
- Consolidated dataset combining seasons S21-S25 with proper SEASON_ID formatting
- Player-season aggregation with mean statistics across all available metrics
- Advanced data handling with proper pace metric treatment (averaging vs summing)
- Comprehensive feature engineering for machine learning applications

### **Advanced Shooting Analysis**
- Shooting efficiency evolution tracking (FG%, 3P%, TS%, eFG%)
- Volume vs efficiency relationship analysis
- 3-point attempt rate progression over career
- Shot distribution visualization with clean styling (white background, black edges)

### **Machine Learning Prediction Model**
- Linear regression models trained on entire NBA dataset (player_season_means)
- Predicts Points, Assists, and Rebounds for 2025-26 season
- Feature engineering including career progression and previous season performance
- Model validation with R² scores and confidence metrics
- Handles missing data with proper NaN treatment and feature validation

### **Advanced Metrics Dashboard**
- **Shooting Efficiency**: FG%, eFG%, True Shooting% evolution
- **Offensive Impact**: Offensive Rating and Usage Rate correlation
- **Two-Way Performance**: Net Rating analysis (positive/negative impact)
- **Usage vs Efficiency**: Critical analysis of Edwards' ability to maintain efficiency with increased usage
- **Playmaking Development**: Assist rate and assist-to-turnover ratio trends
- **Overall Impact**: Player Impact Estimate (PIE) progression

## 🛠️ Technologies Used

- **Python 3.x**
- **NBA API** - Real-time NBA statistics and shot chart data
- **Basketball Reference API** - Historical player data
- **Pandas** - Data manipulation and multi-season aggregation
- **NumPy** - Numerical computations and statistical analysis
- **Matplotlib/Seaborn** - Data visualization with professional styling
- **Scikit-learn** - Machine learning models and prediction
- **Jupyter Notebook** - Interactive analysis environment

## Key Functions

### `ant_functions.py` contains:

- `get_players_stats(player_id, season)` - Retrieve basic season statistics
- `get_shot_chart(player_id, year)` - Fetch detailed shot chart data with coordinates
- `draw_court()` - NBA court visualization utility
- `calculate_per_game_totals()` - Convert totals to per-game averages
- `basketball_reference_adv_data()` - Advanced metrics from Basketball Reference
- Various helper functions for data processing and analysis

## Data Structure

### Season Files:
- **S21.csv** - 2020-21 season (Rookie year)
- **S22.csv** - 2021-22 season
- **S23.csv** - 2022-23 season  
- **S24.csv** - 2023-24 season
- **S25.csv** - 2024-25 season

### Key Dataset Features:
- **SEASON_ID** formatting (e.g., "2020-21", "2021-22")
- Advanced metrics: EFG_PCT, TS_PCT, OFF_RATING, DEF_RATING, NET_RATING, USG_PCT, PIE
- Pace metrics: PACE, E_PACE, PACE_PER40 (properly averaged, not summed)
- Shooting data: FG_PCT, FG3_PCT, FT_PCT with volume statistics
- Playmaking: AST_PCT, AST_TOV ratio analysis

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
3. Open `Ant.ipynb` in Jupyter Notebook
4. Run cells sequentially to reproduce the analysis
