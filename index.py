import pandas as pd
import nltk

from nltk.tokenize import sent_tokenize, word_tokenize


songs60DataSet = "data/musicReport-60.csv"
songs70DataSet = "data/musicReport-70.csv"
songs80DataSet = "data/musicReport-80.csv"
songs90DataSet = "data/musicReport-90.csv"
songs2000DataSet = "data/musicReport-2000.csv"
songs2010DataSet = "data/musicReport-2010.csv"


def main():

    df_60songs = pd.read_csv(songs60DataSet, sep=';')
    print(df_60songs)




if __name__ == '__main__':
	main()