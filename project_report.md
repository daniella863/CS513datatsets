# CS513 Final Project Report
**Historical Menu Analysis: Top Dishes and Price Trends Over Time**

---

## Executive Summary

This project analyzes historical American menu data spanning 160+ years (1852-2012) to identify the most frequently appearing dishes and track their price evolution over time. Using data cleaning techniques and statistical analysis on the NYC Public Library's "What's on the Menu?" collection, we discovered that **Coffee** and **Tea** dominated American menus consistently across all decades, with Coffee showing dramatic price inflation of +2900% from the 1850s to 2010s.

**Key Finding**: The top 5 most frequent dishes (Coffee, Tea, Celery, Olives, Radishes) remained remarkably consistent, but their relative popularity and pricing patterns reveal fascinating insights into American dining culture and economic history.

---

## 1. Introduction & Research Question

### Research Question
**"What are the top 5 most frequently appearing dishes and their median prices per decade in historical American menus from 1850s-2010s?"**

### Motivation
Understanding historical dining patterns provides insights into:
- American culinary culture evolution
- Economic trends through food pricing
- Social changes reflected in menu offerings
- Historical inflation patterns in everyday items

### Dataset Overview
- **Source**: NYC Public Library "What's on the Menu?" digital collection
- **Scope**: 17,545 historical menus, 1.3M+ menu items, 423K+ dishes
- **Time Period**: 1852-2012 (17 decades)
- **Geographic Coverage**: Primarily American establishments

---

## 2. Methodology

### 2.1 Data Cleaning Approach
1. **Source Selection**: Used pre-cleaned versions of core files (`MenuItem-cleaned.csv`, `Dish-cleaned.csv`)
2. **Scope Refinement**: Focused on top 5 most frequent dishes globally
3. **Price Normalization**: Converted price ranges to averages (e.g., $0.10-$0.20 → $0.15)
4. **Temporal Grouping**: Organized data by decades for trend analysis
5. **Data Filtering**: Restricted to 1850-2020 date range, removed invalid records

### 2.2 Analysis Framework
```python
# Core analysis logic
for decade in sorted(df['decade'].unique()):
    decade_data = df[df['decade'] == decade]
    dish_stats = decade_data.groupby('dish_name').agg({
        'dish_id': 'count',  # frequency
        'avg_price': lambda x: np.median(x.dropna()) if x.notna().any() else None
    })
    top_5 = dish_stats.nlargest(5, 'frequency')
```

### 2.3 Statistical Measures
- **Frequency Analysis**: Count of appearances per decade
- **Price Analysis**: Median prices (more robust than mean for historical data)
- **Trend Analysis**: Decade-over-decade changes

---

## 3. Results & Analysis

### 3.1 Global Top 5 Dishes (All-Time)
1. **Coffee** - 8,484 total appearances
2. **Tea** - 4,769 total appearances  
3. **Celery** - 4,690 total appearances
4. **Olives** - 4,553 total appearances
5. **Radishes** - 3,346 total appearances

### 3.2 Historical Trends by Era

#### Early Period (1850s-1890s): Coffee Dominance
- **Coffee**: 34-53% of menu appearances
- **Price Stability**: Coffee consistently $0.10-$0.20
- **Dining Style**: Simple offerings, limited variety

#### Golden Age (1900s-1940s): Diversification
- **Peak Activity**: 1900s had 11,554 total records (highest)
- **Celery Surge**: Became #1 dish in 1910s (30.7% of records)
- **Price Increases**: Gradual inflation across all items

#### Modern Era (1950s-2010s): Beverage Focus
- **Coffee & Tea Dominance**: 90%+ of top dish appearances
- **Menu Simplification**: Other dishes became rare
- **Dramatic Inflation**: Coffee $0.15 (1950s) → $3.00 (2010s)

### 3.3 Price Evolution Analysis

| Decade | Coffee Price | Tea Price | Notable Trend |
|--------|-------------|-----------|---------------|
| 1850s  | $0.10       | $0.10     | Baseline pricing |
| 1900s  | $0.10       | $0.10     | Price stability |
| 1930s  | $0.18       | $0.25     | Depression-era increases |
| 1980s  | $0.68       | $0.68     | Modern pricing begins |
| 2010s  | $3.00       | $3.00     | Contemporary prices |

**Coffee Price Inflation**: +2900% over 160 years

---

## 4. Key Findings & Insights

### Finding 1: Remarkable Consistency
**Coffee** and **Tea** appeared in the top 5 dishes for all 17 decades analyzed, showing extraordinary consistency in American dining preferences.

### Finding 2: Celery's Golden Age  
**Celery** dominated the 1910s, representing 30.7% of all top dish appearances that decade - likely reflecting period health trends and dining customs.

### Finding 3: Economic Indicators
Food pricing closely mirrors broader economic trends:
- **Stability**: 1850s-1920s relatively stable
- **Depression Impact**: 1930s price increases
- **Modern Inflation**: Dramatic acceleration post-1980s

### Finding 4: Menu Evolution
Early menus featured diverse appetizers (celery, olives, radishes), while modern menus increasingly focus on beverages only.

---

## 5. Data Quality & Limitations

### Strengths
- ✅ Large sample size (25,363 relevant records)
- ✅ Long time span (160+ years)  
- ✅ Robust statistical methods (median calculations)
- ✅ Pre-cleaned data reduces inconsistencies

### Limitations
- ⚠️ Price data available for only 24.8% of records
- ⚠️ No inflation adjustment to constant dollars
- ⚠️ Potential geographic bias (NYC-centric collection)
- ⚠️ Dish name variations not fully consolidated

---

## 6. Technical Implementation

### Tools Used
- **Python/Pandas**: Data manipulation and analysis
- **SQLite**: Efficient multi-table joins
- **NumPy**: Statistical calculations
- **CSV Processing**: Data import/export

### Code Architecture
- `script.py`: Main analysis engine (124 lines)
- `data_dictionary.md`: Comprehensive documentation  
- `data_cleaning_workflow.md`: Process documentation
- `README.md`: Project overview and instructions

---

## 7. Conclusions

This analysis successfully answers the research question by identifying the top 5 most frequently appearing dishes and tracking their price evolution across 17 decades. The results reveal both the consistency of American dining preferences (coffee and tea's dominance) and the dramatic economic changes reflected in food pricing.

**Primary Insights**:
1. **Cultural Consistency**: Basic beverages and appetizers remained popular for 160+ years
2. **Economic Reflection**: Food prices serve as excellent indicators of broader economic trends  
3. **Menu Evolution**: Shift from diverse appetizer culture to beverage-focused offerings
4. **Inflation Documentation**: Dramatic price increases in everyday items over time

### Future Research Directions
- Geographic analysis of regional food preferences
- Inflation-adjusted price comparisons
- Correlation with historical events and economic cycles
- Expanded dish consolidation using semantic analysis

---

## 8. References & Data Sources

**Primary Dataset**: 
New York Public Library. "What's on the Menu?" Digital Collection. 
http://menus.nypl.org/

**Analysis Period**: 1852-2012 (17 decades)
**Record Count**: 25,363 menu items analyzed
**Date Completed**: August 2025

---

*This report represents original analysis conducted for CS513 Data Cleaning and Analysis course requirements.*
