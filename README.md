# CS513 Project: Historical Menu Analysis

## Overview
This project analyzes historical American menu data from the "What's on the Menu?" dataset to answer the research question: **"What are the top 5 most frequently appearing dishes and their median prices per decade?"**

## Research Question
**What are the top 5 most frequently appearing dishes and their median prices per decade in historical American menus (1850s-2010s)?**

## Dataset
- **Source**: NYC Public Library's "What's on the Menu?" collection
- **Time Period**: 1852-2012 (17 decades)
- **Records**: 25,363 menu items for analysis
- **Original Data**: 1.3M+ menu items, 423K+ dishes, 17K+ menus

## Key Findings
1. **Coffee** and **Tea** were the most consistent dishes, appearing in top 5 for all 17 decades
2. **Coffee** showed dramatic price inflation: $0.10 (1850s) → $3.00 (2010s) = +2900%
3. **Celery** dominated the 1910s, becoming the #1 dish that decade
4. Early periods (1850s-1890s) showed coffee dominance (34-53% of records)
5. Modern era (1950s+) increasingly dominated by coffee and tea only

## Files
- `script.py` - Main analysis script (run this!)
- `data_dictionary.md` - Comprehensive data documentation
- `Dish-cleaned.csv` - Cleaned dish data
- `MenuItem-cleaned.csv` - Cleaned menu item data
- `Menu.csv`, `MenuPage.csv` - Supporting menu metadata

## How to Run
```bash
python script.py
```

## Methodology
1. **Data Cleaning**: Pre-cleaned CSV files to remove inconsistencies
2. **Top 5 Selection**: Identified globally most frequent dishes
3. **Decade Analysis**: Calculated frequency and median prices per decade
4. **Price Handling**: Averaged price ranges (e.g., $0.10-$0.20 → $0.15)

## Results Summary
The analysis reveals fascinating trends in American dining over 160+ years, showing the dominance of simple beverages and appetizers, with dramatic price inflation reflecting broader economic changes.

---
**CS513 Data Cleaning and Analysis Project**
