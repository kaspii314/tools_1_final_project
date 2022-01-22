#!/Users/kaspii/github/tool1_final_project/.tool1_final_venv/bin/python

import pandas as pd
from pip import main

def load_data(input_file, sep=','):
    df = pd.read_csv(input_file, sep=sep, low_memory=False)
    return df

def main(intput_file):
    df = load_data(input_file)
    print(df['Dimensions'].iloc[[815]])

if __name__ == '__main__':
    input_file = 'data/MetObjects.csv'

    main(input_file)