import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
        print("--- Data Loaded Successfully ---")
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return None

def analyze_top_countries(data):
    print("\n--- Top 10 Happiest Countries (2015) ---")
    
    top_10 = data[['Country', 'Happiness Score']].sort_values(by='Happiness Score', ascending=False).head(10)
    top_10.reset_index(drop=True, inplace=True)
    top_10.index += 1
    print(top_10)
    print("---------------------------------")

def create_pairplot(data):
    print("\nGenerating pairplot...")
    
    plot_columns = ['Happiness Score', 'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)']
    
    g = sns.pairplot(data[plot_columns], kind='reg', plot_kws={'scatter_kws': {'alpha': 0.5}})
    g.fig.suptitle('Pairplot of Key Happiness Factors (2015)', y=1.02)
    
    plt.savefig('happiness_pairplot_2015_noclean.png', bbox_inches='tight')
    print("Saved 'happiness_pairplot_2015_noclean.png'")
    plt.close()

def create_scatter_plots(data):
    print("Generating individual scatter plots...")
    
    plt.figure(figsize=(10, 6))
    sns.regplot(x='Economy (GDP per Capita)', y='Happiness Score', data=data)
    plt.title('Happiness Score vs. GDP per Capita (2015)')
    plt.xlabel('Economy (GDP per Capita)')
    plt.ylabel('Happiness Score')
    plt.savefig('happiness_vs_gdp_2015_noclean.png')
    print("Saved 'happiness_vs_gdp_2015_noclean.png'")
    plt.close()

    plt.figure(figsize=(10, 6))
    sns.regplot(x='Family', y='Happiness Score', data=data)
    plt.title('Happiness Score vs. Social Support (2015)')
    plt.xlabel('Social Support (Family)')
    plt.ylabel('Happiness Score')
    plt.savefig('happiness_vs_social_support_2015_noclean.png')
    print("Saved 'happiness_vs_social_support_2015_noclean.png'")
    plt.close()
    
    plt.figure(figsize=(10, 6))
    sns.regplot(x='Health (Life Expectancy)', y='Happiness Score', data=data)
    plt.title('Happiness Score vs. Healthy Life Expectancy (2015)')
    plt.xlabel('Healthy Life Expectancy')
    plt.ylabel('Happiness Score')
    plt.savefig('happiness_vs_life_expectancy_2015_noclean.png')
    print("Saved 'happiness_vs_life_expectancy_2015_noclean.png'")
    plt.close()

if __name__ == "__main__":
    
    filepath = '2015.csv'
    
    main_data = load_data(filepath)
    
    if main_data is not None:
        analyze_top_countries(main_data)
        create_pairplot(main_data)
        create_scatter_plots(main_data)
        
        print("\n--- Analysis Complete! ---")