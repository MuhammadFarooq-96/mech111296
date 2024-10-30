import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(spark_df):
    # Convert Spark DataFrame to Pandas for EDA
    df = spark_df.toPandas()

    # Basic Info
    print("Dataset Information:")
    print(df.info())
    
    print("\nSummary Statistics:")
    print(df.describe())

    # Check for missing values
    missing_values = df.isnull().sum()
    print("\nMissing Values:")
    print(missing_values)

    # Check for duplicates
    duplicates = df.duplicated().sum()
    print("\nNumber of Duplicate Rows:", duplicates)

    # Visualizations
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Ordered Quantity'].dropna(), kde=True)
    plt.title("Distribution of Ordered Quantity")
    plt.show()

    # Correlation heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()
