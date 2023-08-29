import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
control_group = [85, 88, 84, 79, 91, 86, 87, 83, 80, 82]
treatment_group = [78, 92, 89, 95, 90, 93, 96, 85, 88, 91]
t_stat, p_value = stats.ttest_ind(control_group, treatment_group)
alpha = 0.05
plt.figure(figsize=(8, 5))
plt.boxplot([control_group, treatment_group], labels=['Control', 'Treatment'])
plt.title('Box Plot of Control vs. Treatment Groups')
plt.ylabel('Values')
plt.axhline(np.mean(control_group), color='red', linestyle='--', label='Control Mean')
plt.axhline(np.mean(treatment_group), color='green', linestyle='--', label='Treatment Mean')
plt.legend()
plt.text(1.2, 95, f'p-value: {p_value:.4f}', fontsize=12, color='blue')
plt.show()
if p_value < alpha:
    print("Reject the null hypothesis. The new treatment has a statistically significant effect.")
else:
    print("Fail to reject the null hypothesis. The new treatment does not have a statistically significant effect.")
