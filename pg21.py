import numpy as np
import pandas as pd
import scipy.stats as stats
def load_data(file_name):
    try:
        data = pd.read_csv(file_name)
        return data['Concentration'].values
    except FileNotFoundError:
        print("File not found. Please make sure 'rare_elements.csv' exists in the specified path.")
        exit(1)
def calculate_statistics(data):
    sample_mean = np.mean(data)
    sample_std_dev = np.std(data, ddof=1)  
    return sample_mean, sample_std_dev
def calculate_margin_of_error(sample_std_dev, desired_precision, sample_size):
    margin_of_error = (sample_std_dev / np.sqrt(sample_size)) * desired_precision
    return margin_of_error
def calculate_confidence_interval(sample_mean, margin_of_error):
    confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
    return confidence_interval
def main():
    data = load_data('rare_elements.csv')
    sample_size = int(input("Enter the sample size: "))
    confidence_level = float(input("Enter the confidence level (between 0 and 1): "))
    desired_precision = float(input("Enter the desired level of precision: "))
    sample_mean, sample_std_dev = calculate_statistics(data)
    margin_of_error = calculate_margin_of_error(sample_std_dev, desired_precision, sample_size)
    critical_z = stats.norm.ppf((1 + confidence_level) / 2)
    confidence_interval = calculate_confidence_interval(sample_mean, margin_of_error)
    print(f"Sample Mean: {sample_mean:.4f}")
    print(f"Margin of Error: {margin_of_error:.4f}")
    print(f"Critical Z-value: {critical_z:.4f}")
    print(f"Confidence Interval ({confidence_level * 100}%): ({confidence_interval[0]:.4f}, {confidence_interval[1]:.4f})")
if __name__ == "__main__":
    main()
