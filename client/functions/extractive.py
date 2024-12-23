import nltk 
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize 

def extractive(text):
    stopWords = set(stopwords.words("english")) 
    words = word_tokenize(text) 
       
    freqTable = dict() 
    for word in words: 
        word = word.lower() 
        if word in stopWords or word in string.punctuation: 
            continue
        if word in freqTable: 
            freqTable[word] += 1
        else: 
            freqTable[word] = 1
       
    sentences = sent_tokenize(text) 
    sentenceValue = dict() 
       
    for sentence in sentences: 
        for word, freq in freqTable.items(): 
            if word in sentence.lower(): 
                if sentence in sentenceValue: 
                    sentenceValue[sentence] += freq 
                else: 
                    sentenceValue[sentence] = freq 
       
       
       
    sumValues = 0
    for sentence in sentenceValue: 
        sumValues += sentenceValue[sentence] 
       
    average = int(sumValues / len(sentenceValue)) 
       
    summary = '' 
    prompts = []
    for sentence in sentences: 
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.5 * average)): 
            summary += sentence + " "
            prompts.append(sentence)

    return summary, sentenceValue