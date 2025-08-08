import pandas as pd
import sqlite3
import numpy as np

def main():

    print("What's on The Menu? Dish Analysis")
    print("=" * 55)

    conn = sqlite3.connect(':memory:')

    menu_df = pd.read_csv('Menu.csv')
    menupage_df = pd.read_csv('MenuPage.csv')
    menuitem_df = pd.read_csv('MenuItem-cleaned.csv')
    dish_df = pd.read_csv('Dish-cleaned.csv')

    menu_df.to_sql('Menu', conn, index=False)
    menupage_df.to_sql('MenuPage', conn, index=False)
    menuitem_df.to_sql('MenuItem', conn, index=False)
    dish_df.to_sql('Dish', conn, index=False)
    
    print(f"Loaded {len(menu_df):,} menus, {len(menuitem_df):,} menu items, {len(dish_df):,} dishes")
    
    top_dishes_query = """
    SELECT id, name, times_appeared, menus_appeared
    FROM Dish 
    WHERE times_appeared > 0
    ORDER BY times_appeared DESC 
    LIMIT 5
    """
    
    top_dishes = pd.read_sql_query(top_dishes_query, conn)
    print("Top 5 dishes:")
    for i, row in top_dishes.iterrows():
        print(f"   {i+1}. {row['name']:<20} ({row['times_appeared']:,} times)")
    
    print("\nExtracting detailed data for analysis...")
    dish_ids = top_dishes['id'].tolist()
    dish_ids_str = ','.join(map(str, dish_ids))
    
    detailed_query = f"""
    SELECT 
        d.id as dish_id,
        d.name as dish_name,
        mi.price,
        mi.high_price,
        CASE 
            WHEN mi.high_price IS NOT NULL AND mi.high_price > 0 
            THEN (CAST(mi.price AS REAL) + CAST(mi.high_price AS REAL)) / 2.0
            ELSE CAST(mi.price AS REAL)
        END as avg_price,
        m.date,
        CAST(strftime('%Y', m.date) AS INTEGER) as year,
        (CAST(strftime('%Y', m.date) AS INTEGER) / 10) * 10 as decade,
        m.location,
        m.venue
    FROM MenuItem mi
    JOIN MenuPage mp ON mi.menu_page_id = mp.id
    JOIN Menu m ON mp.menu_id = m.id  
    JOIN Dish d ON mi.dish_id = d.id
    WHERE mi.dish_id IN ({dish_ids_str})
        AND m.date IS NOT NULL
        AND strftime('%Y', m.date) BETWEEN '1850' AND '2020'
    ORDER BY d.times_appeared DESC, m.date
    """
    
    analysis_data = pd.read_sql_query(detailed_query, conn)
    conn.close()
    
    # Save the final cleaned dataset
    final_dataset = 'final_cleaned_dataset.csv'
    analysis_data.to_csv(final_dataset, index=False)
    print(f"Final cleaned dataset saved to: {final_dataset}")
    
    print(f"\nDataset summary:")
    print(f"Total records: {len(analysis_data):,}")
    print(f"Date range: {analysis_data['year'].min()}-{analysis_data['year'].max()}")
    print(f"Records with prices: {analysis_data['avg_price'].notna().sum():,}")

    print(f"\nTop 5 Dishes by Decade")
    print("=" * 55)
    
    df = analysis_data[(analysis_data['decade'] >= 1850) & (analysis_data['decade'] <= 2020)]
    
    print(f"Dataset: {len(df):,} records across {df['decade'].nunique()} decades")
    print(f"Price data: {df['avg_price'].notna().sum():,} records ({100*df['avg_price'].notna().mean():.1f}%)")
    
    results = []
    
    for decade in sorted(df['decade'].unique()):
        decade_data = df[df['decade'] == decade]
        
        # Count frequency and calculate median price for each dish
        dish_stats = decade_data.groupby('dish_name').agg({
            'dish_id': 'count',  # frequency
            'avg_price': lambda x: np.median(x.dropna()) if x.notna().any() else None
        }).rename(columns={'dish_id': 'frequency', 'avg_price': 'median_price'})
        
        # Get top 5 by frequency
        top_5 = dish_stats.nlargest(5, 'frequency')
        
        for rank, (dish_name, row) in enumerate(top_5.iterrows(), 1):
            results.append({
                'decade': int(decade),
                'rank': rank,
                'dish_name': dish_name,
                'frequency': row['frequency'],
                'median_price': row['median_price']
            })
    
    results_df = pd.DataFrame(results)
    
    for decade in sorted(results_df['decade'].unique()):
        decade_results = results_df[results_df['decade'] == decade]
        total_records = len(df[df['decade'] == decade])

        print(f"{decade}s ({total_records:,} total records):")
        print("   " + "-" * 45)
        
        for _, row in decade_results.iterrows():
            price_str = f"${row['median_price']:.2f}" if pd.notna(row['median_price']) else "No price"
            freq_pct = 100 * row['frequency'] / total_records
            print(f"   {row['rank']}. {row['dish_name']:<15} {row['frequency']:>4}x ({freq_pct:4.1f}%) - {price_str}")

    return results_df

if __name__ == "__main__":
    results = main()
