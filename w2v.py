import pandas as pd
import fasttext
import numpy as np
import csv

ft = fasttext.load_model('cc.ru.300.bin')
data = pd.read_csv('films.csv')

vectors=[]
for i in range(len(data)):
    plot=data['description'][i]
    vectors.append(plot)
    list=ft.get_sentence_vector(plot)
    vectors.append(list)
    break


with open('vectors.csv', 'w', newline='') as f:
    csv.writer(f).writerows(vectors)

#print(ft.get_sentence_vector(data['description'][0]))





