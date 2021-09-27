import os
import time
import pandas as pd


def extract_data():
    init = time.time()

    df = pd.DataFrame()

    for hospital in ['A', 'B']:
        PATH = f'data/raw/training_set{hospital}/training/'
        files = os.listdir(PATH)

        for file in files:
            temp = pd.read_csv(PATH + file, sep='|') \
                .rename(str.lower, axis=1) \
                .assign(id=file.split('.')[0])

            df = pd.concat([df, temp])

    end = time.time()

    print(round(end - init, 4))
    print(df.shape)

    df.to_csv('data/interim/sepsis_full_data.csv', index=False)
