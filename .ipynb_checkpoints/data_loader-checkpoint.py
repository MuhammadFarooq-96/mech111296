from pyspark.sql import SparkSession

def load_data(file_path):
    # Initialize a Spark session
    spark = SparkSession.builder.appName("Data Loader").getOrCreate()
    
    # Load the dataset into a Spark DataFrame
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    
    return df