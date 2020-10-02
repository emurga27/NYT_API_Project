import streamlit as st
import pandas as pd
import plotly.express as px
import frequency
import main_run
import word_cloud
from pprint import pprint

st.title('COP4813 - Web Application Programming')
st.header('Project 1')
st.subheader('Part A - The Stories API')
st.text('This app uses the Top Stories API to display the most common words used')
st.text('in the top current articles based on a specified topic selected by the user.')
st.text('The data is displayed as a line chart and as a wordcloud image.')
st.subheader('I. Topic Selection')
name = st.text_input('Please enter your name')
option = st.selectbox('Select a topic of your interest: ',
                      ['arts', 'automobiles', 'books', 'business', 'fashion', 'food',
                       'health', 'home', 'insider', 'magazine', 'movies', 'nyregion',
                       'obituaries', 'opinion', 'politics', 'realestate', 'science',
                       'sports', 'sundayreview', 'technology', 'theater', 't-magazine',
                       'travel', 'upshot', 'us', 'world']
                      )
st.write(f'Hi {name}, your topic is: {option}')

'''*********************************************************************************************'''
st.subheader('II. Frequency Distribution')
see_freq_distr = st.checkbox('Click here to generate a frquency distribution chart.')

most_common_freq_dist = frequency.get_freq_dist(option)
print(most_common_freq_dist)
my_table = pd.DataFrame(most_common_freq_dist) #create table
if see_freq_distr:
    dframe = pd.DataFrame({
        'words': my_table[0],
        'count': my_table[1]
    })
    fig = px.line(dframe, x='words', y='count', title='Top 10 Most Common Words')
    st.plotly_chart(fig)

'''*********************************************************************************************'''
st.subheader('III. Wordcloud')
see_wordcloud =st.checkbox('Click here to generate a wordcloud.')
if see_wordcloud:
    word_cloud.get_top_word_cloud(option)
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

'''*********************************************************************************************'''
st.subheader('Part B - Most Popular Articles')
st.text('Select if you want to see the most shared, emailed, or viewed articles.')

type = st.selectbox('Select your preferred set of articles',
                    ['', 'shared', 'emailed', 'viewed'])
period = st.selectbox('Select the period of time (days)',
                      ['', '1', '7', '30'])

if type and period:
    word_cloud.get_popular_word_cloud(type, period)
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)