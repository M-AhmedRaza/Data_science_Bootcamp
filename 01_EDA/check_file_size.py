import pandas as pd

def main():
    file_path = '01_EDA\PlayStore_EDA_compl.ipynb'
    df = pd.read_json(file_path)
    df['cell_size'] = df['cells'].apply(lambda x: len(x['source']))
    df_sorted = df.sort_values('cell_size', ascending=False)

    print("Top 5 largest cells:")
    print(df_sorted.head(5))

if __name__ == '__main__':
    main()