import numpy as np
student_scores = np.array([
    [78, 89, 92, 85],
    [92, 84, 79, 88],
    [87, 76, 90, 94],
    [90, 85, 88, 92]
])
subject_averages = np.mean(student_scores, axis=0)
highest_average_subject_index = np.argmax(subject_averages)
subject_names = ['Math', 'Science', 'English', 'History']
highest_average_subject = subject_names[highest_average_subject_index]
print("Average scores for each subject:", subject_averages)
print("Subject with the highest average score:", highest_average_subject)

