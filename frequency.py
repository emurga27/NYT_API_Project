import main_run
import matplotlib.pyplot as plt
import nltk
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

#nltk.download('punkt')
#nltk.download('stopwords')

def get_freq_dist(option):
    my_articles = main_run.get_top_stories(option)
    str1 = ''
    for i in my_articles['results']:
        str1 += i['abstract']

    words = word_tokenize(str1)
    words_without_punc = []
    for w in words:
        if w.isalpha():
            words_without_punc.append(w.lower())
    #print(words_without_punc) #for testing purposes
    sw = stopwords.words('english')
    words_withNo_sw = []
    for w in words_without_punc:
        if w not in sw:
            words_withNo_sw.append(w.lower())
    #print(words_withNo_sw) #for testing purposes
    frequence_dist = FreqDist(words_withNo_sw)
    most_comm_words = frequence_dist.most_common(10)
    return most_comm_words

#print(get_freq_dist("arts")) #for testing purposes