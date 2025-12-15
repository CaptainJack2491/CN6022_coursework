```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, log10, floor

def create_spark_session():
    """Creates and returns a Spark session."""
    return SparkSession.builder \
        .appName("Hertzsprung-Russell Diagram Binning") \
        .getOrCreate()

def create_hr_diagram_bins(spark, data_path):
    """
    Loads Gaia data, calculates absolute magnitude, bins the data,
    and creates a 2D histogram for the H-R diagram.

    This query implements the logic for "Query 1.1: The Hertzsprung-Russell (H-R) Diagram Binning"
    from the project notes.
    """
    # Load the dataset.
    # The schema is inferred from the CSV header. For production jobs, it's better
    # to define the schema explicitly for performance and correctness.
    print(f"Loading data from {data_path}...")
    gaia_df = spark.read.csv(data_path, header=True, inferSchema=True)
    print("Data loaded successfully.")

    # Filter out rows where parallax is null, zero, or negative, as it's used in log calculation.
    # Also filter required magnitude and color columns.
    filtered_df = gaia_df.filter(
        (col("parallax").isNotNull()) & (col("parallax") > 0) &
        (col("phot_g_mean_mag").isNotNull()) &
        (col("bp_rp").isNotNull())
    )

    # 1. Mathematical Transformation: Calculate Absolute Magnitude
    # The formula is M = m - 5 * log10(100 / p), where m is apparent magnitude
    # and p is parallax. We use PySpark's built-in log10 function for this.
    df_abs_mag = filtered_df.withColumn(
        "absolute_magnitude",
        col("phot_g_mean_mag") - 5 * log10(100 / col("parallax"))
    )

    # 2. 2D Binning
    # We create discrete bins for both color (bp_rp) and absolute_magnitude
    # using the FLOOR function to group stars into buckets.
    binned_df = df_abs_mag.withColumn(
        "bp_rp_bin", (floor(col("bp_rp") / 0.25) * 0.25).cast("decimal(10, 2)")) \
        .withColumn(
        "absolute_magnitude_bin", floor(col("absolute_magnitude")).cast("integer"))

    # 3. Aggregation
    # We group by the two new bin columns and count the number of stars in each 2D bucket.
    print("Grouping and counting stars in each 2D bin...")
    hr_diagram = binned_df.groupBy("bp_rp_bin", "absolute_magnitude_bin") \
                          .count() \
                          .orderBy("bp_rp_bin", "absolute_magnitude_bin")
    print("Aggregation complete.")

    return hr_diagram

if __name__ == "__main__":
    spark = create_spark_session()

    # The project README specifies that data should be placed in the `data/` directory.
    # This script assumes the Gaia dataset is named 'gaia_dataset.csv' and is located there.
    # You may need to adjust this path based on your actual file name.
    GAIA_DATA_PATH = "data/gaia_dataset.csv"

    # Generate the H-R diagram data
    hr_diagram_bins = create_hr_diagram_bins(spark, GAIA_DATA_PATH)

    # Show a sample of the results
    print("--- Hertzsprung-Russell Diagram Bins (Sample) ---")
    hr_diagram_bins.show(20)

    # To save the output to a CSV file, you can uncomment the following lines:
    # print("Saving output to 'results/hr_diagram_bins.csv'...")
    # hr_diagram_bins.write.mode("overwrite").csv("results/hr_diagram_bins.csv", header=True)
    # print("Output saved successfully.")

    spark.stop()

```