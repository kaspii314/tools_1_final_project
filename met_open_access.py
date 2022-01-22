#!/Users/kaspii/github/tool1_final_project/.tool1_final_venv/bin/python

from ast import Assert
import hashlib
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

def load_data(inpath, infile, sep=','):
    df = pd.read_csv(inpath + infile, sep=sep, low_memory=False)
    # df_clean = df.apply(lambda x: re.sub('\s+',' ',str(x)) if x.dtype == "object" else x)       # remove extra spaces, newlines, tabs
    # return df_clean
    return df

def main(sources):
    # define variables
    data_path = os.path.join(os.getcwd(), 'data', '')
    
    # # download data
    # for source in sources:
    #     get_data(source=sources[source], outpath=data_path)

    # load and clean data
    df = load_data(inpath=data_path, infile=sources['data']['file'])
    test = df['Dimensions'].tolist()
    print(test)

    # s = 'ï»¿Object Number,Is Highlight,Is Timeline Work,Is Public Domain,Object ID,Gallery Number,Department,AccessionYear,Object Name,Title,Culture,Period,Dynasty,Reign,Portfolio,Constituent ID,Artist Role,Artist Prefix,Artist Display Name,Artist Display Bio,Artist Suffix,Artist Alpha Sort,Artist Nationality,Artist Begin Date,Artist End Date,Artist Gender,Artist ULAN URL,Artist Wikidata URL,Object Date,Object Begin Date,Object End Date,Medium,Dimensions,Credit Line,Geography Type,City,State,County,Country,Region,Subregion,Locale,Locus,Excavation,River,Classification,Rights and Reproduction,Link Resource,Object Wikidata URL,Metadata Date,Repository,Tags,Tags AAT URL,Tags Wikidata URL'
    # print(s.encode('utf-8-sig'))

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
            'file': 'MetObjects_test.csv',
            'checksum': '68d26f76485ccd066d45b6044d0954f1508e431a21c4ef7133f45c46931d4773' 
        }
    }

    main(sources=sources)