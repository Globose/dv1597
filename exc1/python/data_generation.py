from random import randrange as rr

def load_lorem():
    A = []
    with open('lorem.txt', 'r') as file:
        for f in file:
            tstring = f.replace(',', '').replace('.', '').replace('\n','').replace('"','').lower()
            words = tstring.split(' ')
            for w in words:
                if len(w) > 3:
                    A.append(w)
    return A

def get_tweets(n):
    words = load_lorem()
    tweets = []
    for _ in range(n):
        result = ""
        w1 = words[rr(len(words))]
        result += w1[0].upper() + w1[1:]
        nextbig = False

        it = rr(4,15)
        for i in range(it):
            wn = words[rr(len(words))]
            if nextbig:
                wn = wn[0].upper() + wn[1:]
                nextbig = False
            if rr(100) < 20:
                wn = "#"+wn
            if rr(100) < 20 and i < it-1:
                if rr(100) < 50:
                    wn += "."
                    nextbig = True
                else:
                    wn += ","
            result += " " + wn
        if rr(10) < 3:
            result += "!"
        elif rr(10) < 7:
            result += "."
        tweets.append(result)
    return tweets

def main():
    tweets = get_tweets(2000)
    data = []
    # header = "tweet,likes,retweets"
    header = "tweet"
    data.append(header)
    for t in tweets:
        date = f"{rr(1,25)}/{rr(1,13)}-{rr(1800,2026)}"
        likes = str(rr(13000))
        retweets = str(rr(1200))
        # data.append("\""+t+'\",'+likes+","+retweets)
        data.append("\""+t+'\"')

    with open('test_data.csv', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))


if __name__ == '__main__':
    main()