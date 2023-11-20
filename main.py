import streamlit as st
import plotly_express as px
from data_extractor import get_files
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


#get diary data

diary_dict = get_files()
print(diary_dict)
dates = diary_dict['date']
diary_notes = diary_dict['diary']

#sentimental analysis using nltk library
analyzer = SentimentIntensityAnalyzer()
polarity_scores = []
for note in diary_notes:
    polarity_scores.append(analyzer.polarity_scores(note))
positive_scores = [score['pos'] for score in polarity_scores]
negative_scores = [score['neg'] for score in polarity_scores]
# plot graphs

st.title("Diary Tone")
st.subheader("Positivity")

x=[1,2]
y=[3,4]

figure = px.line(x=dates,y=positive_scores,labels={'x':'Dates','y':'Date'})
st.plotly_chart(figure)

# negativity graph
st.subheader("Negativity")

x=[1,2]
y=[3,4]

figure = px.line(x=dates,y=negative_scores,labels={'x':'Negativity','y':'Date'})
st.plotly_chart(figure)
