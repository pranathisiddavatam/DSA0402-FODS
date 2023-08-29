import numpy as np
from scipy import stats
drug_group = np.array([10, 12, 9, 8, 11, 10, 9, 9, 11, 10, 9, 8, 11, 12, 10, 11, 9, 10, 11, 10, 
                       9, 10, 11, 10, 9, 8, 11, 10, 9, 10, 12, 11, 10, 9, 10, 11, 10, 9, 8, 11, 
                       10, 12, 11, 10, 9, 10, 11, 10])
placebo_group = np.array([5, 6, 4, 7, 5, 6, 4, 5, 7, 5, 6, 4, 5, 7, 5, 6, 4, 7, 5, 6, 
                          4, 5, 7, 5, 6, 4, 5, 7, 5, 6, 4, 5, 7, 5, 6, 4, 7, 5, 6, 
                          4, 5, 7, 5, 6, 4, 5, 7])
confidence_level = 0.95
def calculate_confidence_interval(data):
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)  
    n = len(data)
    z_score = stats.norm.ppf((1 + confidence_level) / 2)  
    margin_of_error = z_score * (std_dev / np.sqrt(n))
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    return lower_bound, upper_bound
lower_bound_drug, upper_bound_drug = calculate_confidence_interval(drug_group)
lower_bound_placebo, upper_bound_placebo = calculate_confidence_interval(placebo_group)
print(f"95% Confidence Interval for Drug Group: ({lower_bound_drug:.4f}, {upper_bound_drug:.4f})")
print(f"95% Confidence Interval for Placebo Group: ({lower_bound_placebo:.4f}, {upper_bound_placebo:.4f})")
