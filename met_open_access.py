#!/Users/kaspii/github/tool1_final_project/.tool1_final_venv/bin/python

from ast import Assert
import hashlib
import numpy as np
import pandas as pd
import os
import re
import requests

def get_data(source, outpath):
    # get data and output to file
    try:
        r = requests.get(source['url'] + source['file'])
        r.raise_for_status()
        r.encoding = 'UTF-8'
        with open(outpath + source['file'], 'w') as f:
            f.write(r.text)
    except requests.exceptions.RequestException as e:
        print('Requests Error:', e)

    # validate data file
    if 'checksum' in source:
        try:
            with open(outpath + source['file'],"rb") as f:
                bytes = f.read()                                        # read entire file in as bytes
                readable_hash = hashlib.sha256(bytes).hexdigest()
            assert source['checksum'] == readable_hash                  # compare SHA256 hash
        except AssertionError:
            print('SHA256 Error:', source['checksum'], readable_hash)  

def get_year(years, min_max='min'):
    if len(years) == 0:                                                 # leave nulls alone
        return ''
    elif years.isnumeric():                                             # leave years that are already years alone
        return years
    elif re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}', years):                 # YYYY-MM-DD -> YYYY
        return years[0:4]
    else:                                                               # year ranges
        years_clean = re.sub('-', ' ', years)
        years_lst = [ int(year) for year in years_clean.split() if year.isnumeric() ]
        if min_max == 'min' and len(years_lst) > 0:
            return(min(years_lst))
        elif min_max == 'max' and len(years_lst) > 0:
            return(max(years_lst))
        else:
            return ''

def load_data(inpath, infile, sep=','):
    df = pd.read_csv(inpath + infile, sep=sep, low_memory=False)
    df_clean = pd.DataFrame()

    # clean data
    for column in df.columns:
        df_clean[column] = df[column]
        df_clean[column] = df_clean[column].apply(lambda x: str(x).strip())                  # remove leading and trailing whitespace
        df_clean[column] = df_clean[column].apply(lambda x: re.sub('\s+',' ',str(x)))        # remove carriage returns, line feeds, and extra spaces
        df_clean[column] = df_clean[column].apply(lambda x: str(x).replace('|','-'))         # consistent text separators for other data cleaning functions

    # clean up year columns
    df_clean['accession_year_clean'] = df_clean['AccessionYear'].apply(lambda x: str(x)[0:4])
    df_clean['artist_begin_date_clean'] = df_clean['Artist Begin Date'].apply(lambda x: get_year(str(x), 'min'))
    df_clean['artist_end_date_clean'] = df_clean['Artist End Date'].apply(lambda x: get_year(str(x), 'max'))

    for column in df_clean.columns:
        df_clean[column] = df_clean[column].apply(lambda x: str(x).replace('nan', ''))
    df_clean.to_csv(inpath + 'MetObjects_clean.csv', index=False, sep='|')
    return df_clean

def main(data_path, sources):
    # # download data
    # for source in sources:
    #     get_data(source=sources[source], outpath=data_path)

    # load and clean data
    df = load_data(inpath=data_path, infile=sources['data']['file'])

if __name__ == '__main__':
    # Enforcing specific commit (cc6310135aeafd01fb03588929fb9d00c5cbc606) from Jan 17, 2022 because data is manually input with no tagged releases.
    sources = {
        'license': {
            'url': 'https://raw.githubusercontent.com/metmuseum/openaccess/cc6310135aeafd01fb03588929fb9d00c5cbc606/',
            'file': 'LICENSE'
        },
        'readme': { 
            'url': 'https://raw.githubusercontent.com/metmuseum/openaccess/cc6310135aeafd01fb03588929fb9d00c5cbc606/', 
            'file': 'README.md' 
        }, 
        'data': { 
            'url': 'https://media.githubusercontent.com/media/metmuseum/openaccess/cc6310135aeafd01fb03588929fb9d00c5cbc606/', 
            'file': 'MetObjects.csv',
            'checksum': '68d26f76485ccd066d45b6044d0954f1508e431a21c4ef7133f45c46931d4773' 
        }
    }

    # Define where you want the data to live and mkdir if necessary
    data_path = os.path.join(os.getcwd(), 'data', '')
    if not os.path.exists(data_path):
        os.mkdir(data_path)

    main(data_path=data_path, sources=sources)