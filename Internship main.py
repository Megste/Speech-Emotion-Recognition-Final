from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import tkinter.messagebox

nltk.download('vader_lexicon')
import speech_recognition as sr

def getaudio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        audio=r.listen(source)
        myText=r.recognize_google(audio)
    return myText

def analyze_sentiment(mainT):
  sia = SentimentIntensityAnalyzer()
  sentiment_scores = sia.polarity_scores(mainT)
  sentiment = ""
  if sentiment_scores['compound'] >= 0.05:
    sentiment = "positive"
  elif sentiment_scores['compound'] <= -0.05:
    sentiment = "negative"
  else:
    sentiment = "neutral"
  return sentiment, sentiment_scores

def main():
    mainT=getaudio()
    emotion=analyze_sentiment(mainT)
    print(emotion[0])
    sentiment_label.config(text=f"Sentiment: {emotion[0]}")
    if emotion[0]=="negative":
        text="Sorry to hear that."
        print(text)
    elif emotion[0]=="positive":
        text="Glad to hear that."
        print(text)
    else:
        text="I understand."
        print(text)
    sentiment_text.config(text=text)


       
from tkinter import *
# tkinter GUI
root= Tk()

#Make a Canvas (i.e, a screen for your project
canvas1 = Canvas(root, width = 400, height = 400)
canvas1.pack()
canvas1.configure(bg='red')
img = PhotoImage(file="C:/Users/megst/Downloads/spiderverse.png")
#img = PhotoImage(file="C:/Users/shiva/Downloads/b.png")

canvas1.create_image(1,1, anchor=NW, image=img)

label1 = Label(root, text='SPEECH EMOTION RECOGNITION',font=("Helvetica", 16),bg='lightblue')
canvas1.create_window(200, 50, window=label1)

button1 = Button (root, text='Record Voice',command=main, bg='orange',font=("Helvetica", 16))
canvas1.create_window(185, 100, window=button1)

# Create a label for sentiment result
sentiment_result = Label(root, text='Sentiment Result:',font=("Helvetica", 16),bg='lightgreen')
canvas1.create_window(200, 150, window=sentiment_result)

# Create a label to display sentiment
sentiment_label = Label(root, text='', font=("Helvetica", 14), bg='orange')
canvas1.create_window(200, 200, window=sentiment_label)

# Create a label to display sentiment text
sentiment_text = Label(root, text='', font=("Helvetica", 12), bg='pink')
canvas1.create_window(200, 250, window=sentiment_text)

root.mainloop()
