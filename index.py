import pandas as pd
import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer

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

def toLowerCase(text):
    wordsToLowerCase = []

    for word in text:
        wordLowerCase = word.lower()
        wordsToLowerCase.append(wordLowerCase)

    return wordsToLowerCase

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

    textWithLowerCase = toLowerCase(textWithoutSpecialCharacter)

    return textWithLowerCase

def stemming(tokens):

    stemmer = RSLPStemmer()
    pharse = []

    for word in tokens:
        pharse.append(stemmer.stem(word))
    
    return pharse

def lemmatization(tokens):

    lemaFunction = WordNetLemmatizer()
    pharse = []

    for word in tokens:
        pharse.append(lemaFunction.lemmatize(word))
    
    return pharse


def generateReports(dfMusics, clearData, stemmingData, lematizedData, decade):

    dfClearData = pd.DataFrame(clearData, columns = ['Text'])
    dfMusics['Text'] = dfClearData['Text']
    dfMusics.to_csv('output/clearData/musicReport-ClearData-' + decade + '.csv', index=False)

    dfStemmingData = pd.DataFrame(stemmingData, columns = ['Text'])
    dfMusics['Text'] = dfStemmingData['Text']
    dfMusics.to_csv('output/stemmingData/musicReport-StemmingData-' + decade + '.csv', index=False)

    dfLematizedData = pd.DataFrame(lematizedData, columns = ['Text'])
    dfMusics['Text'] = dfLematizedData['Text']
    dfMusics.to_csv('output/lematizedData/musicReport-LematizedData-' + decade + '.csv', index=False)


def main():

    musicReports = [(s60DataSet, '60'), (s70DataSet, '70'), (s80DataSet, '80'), 
                    (s90DataSet, '90'), (s2000DataSet, '2000'), (s2010DataSet, '2010')]

    for musicDataSet in musicReports:

        dataSetPath = musicDataSet[0]
        decade = musicDataSet[1]
        
        clearData = { 'Text': [] }
        stemmingData  = { 'Text': [] }
        lematizedData = { 'Text': [] }

        dfMusics = pd.read_csv(dataSetPath, sep=';')
        musicNames = list(dfMusics['Music'])

        for name in musicNames:

            musicData = dfMusics[dfMusics['Music'] == name]
            musicTokens = musicToken(musicData['Text'])
            filteredTokens = filterMusicText(musicTokens)

            lematizedTokens = lemmatization(filteredTokens)
            stemmingTokens = stemming(filteredTokens)

            clearData['Text'].append(filteredTokens)
            stemmingData['Text'].append(stemmingTokens)
            lematizedData['Text'].append(lematizedTokens)

        
        generateReports(dfMusics, clearData, stemmingData, lematizedData, decade)

if __name__ == '__main__':
	main()