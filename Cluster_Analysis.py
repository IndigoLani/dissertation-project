#import dependencies
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import gensim
import warnings

#hide runtime warnings
#warnings.filterwarnings("ignore")

# Load gensim model file
filename = "gensim_file"
model = gensim.models.Word2Vec.load(filename)
print("Gensim model: COMPLETE")

# Read in CSV file and encode to UTF-8
df = pd.read_csv('./sarcasm_training_data.csv', encoding="UTF-8")
original_df = pd.DataFrame(df)

# Correct data format
final_data = []
for i, row in df.iterrows():
    comment_vectorized = []
    comment = row
    comment_all_words = comment.split(sep=" ")

    for comment_w in comment_all_words:
        try:
            comment_vectorized.append(list(model[comment_w]))
        except Exception as e:
            pass
    try:
        comment_vectorized = np.asarray(comment_vectorized)
        comment_vectorized_mean = list(np.mean(comment_vectorized, axis=0))
    except Exception as e:
        comment_vectorized_mean = list(np.zeros(100))
        pass
    try:
        len(comment_vectorized_mean)
    except:
        comment_vectorized_mean = list(np.zeros(100))

    temp_row = np.asarray(comment_vectorized_mean)

    final_data.append(temp_row)
X = np.asarray(final_data)

print('Convert to array: COMPLETE') 

# Use KMeans to perform clustering
clf = KMeans(n_clusters=4, n_jobs=-1, max_iter=50000, random_state=1)
clf.fit(X)
print('Clustering: COMPLETE')

# Save the csv file and provide labels
comment_label = clf.labels_
comment_cluster_df = pd.DataFrame(original_df)
comment_cluster_df['comment_label'] = np.nan
comment_cluster_df['comment_label'] = comment_label

print('Saving...')
comment_cluster_df.to_csv('./cluster_output.csv', index=False)
