import pandas as pd

# Filter stars in HYG dataset based on magnitude and save filtered data to new CSV file
def filter_stars(input_file, output_file, magnitude_threshold):
    try:
        # Read HYG dataset with pandas
        data = pd.read_csv(input_file)

        # Filter dataframe to only include starts with magnitude greater than or equal to threshold
        filtered_data = data[data['absmag'] >= magnitude_threshold]

        # Save filtered data to new CSV file
        filtered_data.to_csv(output_file, index=False)

        print("Filtered data saved succesfully.")
    
    except Exception as e:
        print(f"An error occured: {e}")

# Dataset file paths
input_file = 'data/hygdata_v37.csv'
output_file = 'data/hygdata_v37_filtered.csv'

# Filter stars to 6.5 threshold (visible stars)
filter_stars(input_file, output_file, 6.5)