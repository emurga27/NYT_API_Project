from wordcloud import WordCloud
import matplotlib.pyplot as plt
import main_run
import streamlit_methods

def get_top_word_cloud(option):
    my_articles = main_run.get_top_stories(streamlit_methods.option)
    str1 = ''
    for i in my_articles['results']:
        str1 += i['abstract']

    wc = WordCloud().generate(str1)
    plt.figure(figsize=(15, 15))
    plt.imshow(wc)
    plt.axis('off')
    plt.show()

def get_popular_word_cloud(type, period):
    my_articles = main_run.get_most_popular_stories(type, period)
    str2 = ""
    for i in my_articles['results']:
        str2 += i['abstract']

    word_cloud_popular = WordCloud().generate(str2)
    plt.figure(figsize=(15, 15))
    plt.imshow(word_cloud_popular)
    plt.axis('off')
    plt.show()