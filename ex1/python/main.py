import os
import pandas as pd

def find_files():
    """Finds all files in the path"""
    paths = None
    try:
        paths = os.listdir()
    except FileNotFoundError:
        print("Faulty path, closing program")
        return None
    return paths

def main():
    files = find_files()
    dataframes = []
    for f in files:
        if '.' not in f:
            continue
        fname, ftype = f.split('.')
        if ftype == "csv":
            df = pd.read_csv(f, sep=',', encoding='utf-8')
            df.name = fname
            dataframes.append(df)

    for df in dataframes:
        print(df.name)
        print(df.info)


if __name__ == '__main__':
    main()
