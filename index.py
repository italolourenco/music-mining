import pandas as pd
import nltk
import re


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords



# Pré-Processamento dos dados (OK)
# Indexação


songs60DataSet = "data/musicReport-60.csv"
songs70DataSet = "data/musicReport-70.csv"
songs80DataSet = "data/musicReport-80.csv"
songs90DataSet = "data/musicReport-90.csv"
songs2000DataSet = "data/musicReport-2000.csv"
songs2010DataSet = "data/musicReport-2010.csv"


def musicToken(text):
    tokens = word_tokenize(text.values[0])
    return tokens

def musicRemoveStopWords(text):

    stopWords = set(stopwords.words('portuguese'))
    wordsFiltered = []

    for w in text:
        if w not in stopWords:
            wordsFiltered.append(w)

    return wordsFiltered

def musicRemoveNumbers(text):
    regex = re.compile('[-|0-9]')
    filtered = [i for i in text if not regex.match(i)]
    return filtered

def musicRemoveSpecialCharacter(text):

    regex = re.compile(r'[-./?!,":;()\']')
    filtered = [i for i in text if not regex.match(i)]
    return filtered

def filterMusicText(text):

    textWithoutStopWords = musicRemoveStopWords(text)

    textWithoutNumbers = musicRemoveNumbers(textWithoutStopWords)

    textWithoutSpecialCharacter = musicRemoveSpecialCharacter(textWithoutNumbers)

    return textWithoutSpecialCharacter




def main():

    music_data = {}

    df_60songs = pd.read_csv(songs60DataSet, sep=';')
    music_names = list(df_60songs['Music'])

    for name in music_names:
        print(name)
        print('\n')
        music_data = df_60songs[df_60songs['Music'] == name]
        music_token = musicToken(music_data['Text'])
        filtered_tokens = filterMusicText(music_token)
        fdist = nltk.FreqDist(filtered_tokens)
        for k,v in fdist.items():
            linha = k+';'+str(v)+';;;;'
            print(linha)
        




if __name__ == '__main__':
	main()