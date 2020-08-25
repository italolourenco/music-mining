import pandas as pd
import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

s60DataSet = "data/musicReport-60.csv"
s70DataSet = "data/musicReport-70.csv"
s80DataSet = "data/musicReport-80.csv"
s90DataSet = "data/musicReport-90.csv"
s2000DataSet = "data/musicReport-2000.csv"
s2010DataSet = "data/musicReport-2010.csv"

musicCipher = [
    'A', 'Ab', 'A#', 'Am', 'A#m', 'Abm', 'A7',
    'B', 'Bb', 'Bm', 'Bbm', 'B7',
    'C', 'C#', 'Cm', 'C#m', 'C7',
    'D', 'Db', 'D#', 'Dm', 'D#m', 'Dbm', 'D7',
    'E', 'Eb', 'Em', 'Ebm', 'E7',
    'F', 'F#', 'Fm', 'F#m', 'F7',
    'G', 'Gb', 'G#', 'Gm', 'G#m', 'Gbm', 'G7'
]


def musicToken(text):

    tokens = word_tokenize(text.values[0])
    return tokens

def musicRemoveStopWords(text):

    stopWords = set(stopwords.words('portuguese'))
    wordsFiltered = []

    for word in text:
        if word not in stopWords:
            wordsFiltered.append(word)

    return wordsFiltered

def musicRemoveNumbers(text):

    regex = re.compile('[-|0-9]')
    filtered = [i for i in text if not regex.match(i)]
    return filtered

def musicRemoveSpecialCharacter(text):

    regex = re.compile(r'[-./?!,":;()```\']')
    filtered = [i for i in text if not regex.match(i)]
    return filtered

def musicRemoveCiphers(text):

    wordsFiltered = []

    for word in text:
        if word not in musicCipher:
            wordsFiltered.append(word)

    return wordsFiltered


def filterMusicText(text):

    textWithoutStopWords = musicRemoveStopWords(text)

    textWithoutCiphers = musicRemoveCiphers(textWithoutStopWords)

    textWithoutNumbers = musicRemoveNumbers(textWithoutCiphers)

    textWithoutSpecialCharacter = musicRemoveSpecialCharacter(textWithoutNumbers)

    return textWithoutSpecialCharacter

def stemming(tokens):
    stemmer = RSLPStemmer()
    pharse = []

    for word in tokens:
        pharse.append(stemmer.stem(word))
    
    return pharse


def main():

    # musicReports = [s60DataSet, s70DataSet, s80DataSet, s90DataSet, s2000DataSet, s2010DataSet]

    musicReports = [s60DataSet]

    for musicDataSet in musicReports:
        
        music_data = {}

        dfMusics = pd.read_csv(musicDataSet, sep=';')
        musicNames = list(dfMusics['Music'])

        for name in musicNames:
            musicData = dfMusics[dfMusics['Music'] == name]
            musicTokens = musicToken(musicData['Text'])
            filteredTokens = filterMusicText(musicTokens)
            print(musicData['Music'].values[0])
            print(filteredTokens)
            print("Stemming")
            print(stemming(filteredTokens))
        




if __name__ == '__main__':
	main()