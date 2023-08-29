import pandas as pd
data = {
    'post_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'likes': [50, 120, 80, 35, 35, 90, 150, 150, 110, 110]
}
df = pd.DataFrame(data)
likes_freq = df['likes'].value_counts().reset_index()
likes_freq.columns = ['Likes', 'Frequency']
likes_freq = likes_freq.sort_values(by='Likes')
print(likes_freq)
