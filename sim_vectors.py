from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

data = pd.read_csv('vectors.csv')




a = ft.get_sentence_vector(data[0])
b = ft.get_sentence_vector(data[0])
cosine = cosine_similarity(a.reshape(1, -1), b.reshape(1, -1))
print(cosine)
