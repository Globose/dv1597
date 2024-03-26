import pandas as pd

def get_hashtags(tweet):
    i = 0
    hashtags = []
    while i < len(tweet):
        if tweet[i] == '#':
            i += 1
            hashtag = ""
            while i < len(tweet):
                if tweet[i].isalpha() or tweet[i].isnumeric():
                    hashtag += tweet[i]
                    i+=1
                else:
                    break
            if len(hashtag) > 0:
                hashtags.append(hashtag)
        i+=1
    return hashtags


def extract_hashtags(dataframe):
    """Extracts the set of hashtags from a dataframe of tweets."""
    hashtags_list = dataframe["tweet"].apply(get_hashtags).tolist()
    return set([word for tweet in hashtags_list for word in tweet])

def main():
    data_url = "test_data.csv"
    dataframe = pd.read_csv(data_url, sep=',', encoding='utf-8')
    hashtags = extract_hashtags(dataframe)
    print(hashtags)

if __name__ == '__main__':
    main()