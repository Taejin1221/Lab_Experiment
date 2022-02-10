import os
import pandas as pd

file_list = [i for i in os.listdir() if 'Similar' in i]
for file in file_list:
    df = pd.read_csv(file, header = 0)

    df = df.head(10)
    df.pop(df.keys()[0])

    new_file_name = 'MSE_of_' + file.split('(')[1].split(')')[0][:-4] + '.csv'
    df.to_csv(new_file_name)