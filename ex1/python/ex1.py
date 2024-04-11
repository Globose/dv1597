import pandas as pd
import re

def extract_hashtags(dataframe):
    """Extracts the set of hashtags from a dataframe of tweets."""
    g = lambda x: re.findall('#[A-Za-z0-9]*', x)
    hashtags_list = dataframe["tweet"].apply(g).tolist()
    return set([word for tweet in hashtags_list for word in tweet])

def main():
    data_url = "test_data.csv"
    dataframe = pd.read_csv(data_url, sep=',', encoding='utf-8')
    hashtags = extract_hashtags(dataframe)
    print(hashtags)

if __name__ == '__main__':
    main()