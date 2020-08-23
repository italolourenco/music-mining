import pandas as pd
import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

s60DataSet = "data/musicReport-60.csv"
s70DataSet = "data/musicReport-70.csv"
s80DataSet = "data/musicReport-80.csv"
s90DataSet = "data/musicReport-90.csv"
s2000DataSet = "data/musicReport-2000.csv"
s2010DataSet = "data/musicReport-2010.csv"


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

def calcFreqDist(tokens):
    freqDist = nltk.FreqDist(filtered_tokens)
    for k,v in freqDist.items():
        linha = k+';'+str(v)+';;;;'
        print(linha)


def main():

    musicReports = [s60DataSet, s70DataSet, s80DataSet, s90DataSet, s2000DataSet, s2010DataSet]

    for musicDataSet in musicReports:
        
        music_data = {}

        dfMusics = pd.read_csv(musicDataSet, sep=';')
        musicNames = list(dfMusics['Music'])

        for name in musicNames:
            musicData = dfMusics[dfMusics['Music'] == name]
            musicToken = musicToken(musicData['Text'])
            filteredTokens = filterMusicText(musicToken)
        




if __name__ == '__main__':
	main()