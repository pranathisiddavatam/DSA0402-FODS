import numpy as np
import scipy.stats as stats
design_A = [0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0]
design_B = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
t_stat, p_value = stats.ttest_ind(design_A, design_B)
alpha = 0.05
if p_value < alpha:
    result = "reject the null hypothesis"
else:
    result = "fail to reject the null hypothesis"
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"Conclusion: Based on a significance level of {alpha}, we {result}.\n")
if p_value < alpha:
    print("There is a statistically significant difference in the mean conversion rates between website design A and B.")
else:
    print("There is no statistically significant difference in the mean conversion rates between website design A and B.")
