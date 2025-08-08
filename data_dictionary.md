# Data Dictionary: top_5_dishes_for_cleaning.csv

## Overview
This dataset contains 25,363 menu item records for the top 5 most frequently appearing dishes in historical American menus (1852-2012). The data has been extracted and prepared for data cleaning analysis to answer the research question: **"What are the top 5 most frequently appearing dishes and their median prices per decade in historical menus?"**

## Column Descriptions

### Dish Information
- **`dish_id`** (Integer): Unique identifier for each dish type from the original Dish table
- **`dish_name`** (Text): Original name of the dish as it appears in historical menus
  - Examples: "Coffee", "Tea", "Celery", "Olives", "Radishes"
  - Note: This column may contain spelling variations and inconsistencies that require cleaning

### Pricing Information
- **`price`** (Float): Base price or starting price of the menu item in original currency
- **`high_price`** (Float): Ending price for items listed as price ranges (may be NULL)
- **`avg_price`** (Float): **Calculated average price** using the following logic:
  ```
  IF high_price IS NOT NULL AND high_price > 0:
      avg_price = (price + high_price) / 2.0
  ELSE:
      avg_price = price
  ```
  
  **Examples:**
  - Single price: Coffee $0.10 → avg_price = $0.10
  - Price range: Coffee $0.10-$0.20 → avg_price = $0.15
  - Price range: Coffee $0.05-$0.15 → avg_price = $0.10

### Temporal Information
- **`date`** (Date): Original menu date in YYYY-MM-DD format
- **`year`** (Integer): Extracted year from the menu date
- **`decade`** (Integer): Calculated decade (year rounded down to nearest 10)
  - Examples: 1895 → 1890, 1923 → 1920, 2005 → 2000

### Menu Context
- **`location`** (Text): Geographic location where the menu was used
  - Examples: "Waldorf Astoria", "Hotel Manhattan", "Norddeutscher Lloyd Bremen"
- **`venue`** (Text): Type of establishment or venue category
  - Examples: "COMMERCIAL", "RESTAURANT", "RAILROAD"

## Data Quality Notes

### Price Data Coverage
- **Total records**: 25,363
- **Records with price data**: 6,287 (24.8%)
- **Missing price data**: Common in earlier decades and certain venue types

### Temporal Distribution 
The dataset is heavily concentrated in the early 20th century:
- **Peak period**: 1900s-1910s (17,171 records, 67.7% of total)
- **Earliest record**: 1852
- **Latest record**: 2012
- **Data quality**: Best coverage 1880s-1960s

### Top 5 Dishes Breakdown
1. **Coffee**: 8,277 records (32.6%)
2. **Celery**: 4,643 records (18.3%)
3. **Tea**: 4,604 records (18.1%)
4. **Olives**: 4,516 records (17.8%)
5. **Radishes**: 3,323 records (13.1%)

### Known Limitations
⚠️ **Important**: This dataset uses individual `dish_id` values, which fragments related dishes:
- Multiple IDs exist for the same dish concept (e.g., "Coffee" vs "COFFEE" vs "Iced Coffee")
- True dish frequencies are higher than shown here
- Results represent conservative estimates of dish popularity
- Future analysis should consolidate dish name variations for more accurate results

## Data Cleaning Recommendations

### Primary Cleaning Task
Focus on the **`dish_name`** column to:
1. Standardize capitalization (e.g., "Coffee" vs "COFFEE")
2. Fix spelling variations and typos
3. Ensure consistent naming across decades
4. Create a new `cleaned_dish_name` column with standardized values

### Analysis Workflow
1. **Extract**: Data already extracted using `simple_dish_extraction.py`
2. **Clean**: Use OpenRefine to clean the `dish_name` column
3. **Analyze**: Run `analyze_final_results.py` to generate final decade-by-decade analysis

## Expected Outcomes

After cleaning, this dataset will enable analysis of:
- Top 5 most frequent dishes per decade (with acknowledged limitations)
- Median price trends over time for the selected dish IDs
- Historical dining pattern evolution for major dish categories
- Price inflation analysis for common menu items

**Note**: Results should be interpreted as conservative estimates due to dish ID fragmentation in the source data.

## Technical Notes

### Data Sources
- **Menu.csv**: Menu metadata and dates
- **MenuPage.csv**: Menu page structure
- **MenuItem.csv**: Individual menu item records with pricing
- **Dish.csv**: Dish definitions and frequency statistics

### Extraction Criteria
- Top 5 dishes selected by global frequency from Dish.times_appeared
- Filtered to records with valid dates (1850-2020)
- Includes all venues and locations globally
- No geographic restrictions applied

### File Size
- **Size**: ~1.6 MB
- **Format**: UTF-8 CSV with header row
- **Suitable for**: OpenRefine, Excel, Python/R analysis
