from tkinter import *
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from PIL import ImageTk, Image





def ipl_predictor(current_score, wicketsfallen, overs_completed, scoreof_striker, scoreof_nonstriker):
   dataset = pd.read_csv('data/ipl.csv')
   X = dataset.iloc[:, [7,8,9,12,13]].values
   y = dataset.iloc[:, 14].values

   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

   

   lin = LinearRegression()
   lin.fit(X_train, y_train)





   #custom input
   new_prediction = lin.predict((np.array([[current_score, wicketsfallen, overs_completed, scoreof_striker, scoreof_nonstriker]])))
   return round(*new_prediction)



def odi_predictor(current_score, wicketsfallen, overs_completed, scoreof_striker, scoreof_nonstriker):
   dataset = pd.read_csv('data/odi.csv')
   X = dataset.iloc[:, [7,8,9,12,13]].values
   y = dataset.iloc[:, 14].values

   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

   

   lin = LinearRegression()
   lin.fit(X_train, y_train)





   #custom input
   new_prediction = lin.predict((np.array([[current_score, wicketsfallen, overs_completed, scoreof_striker, scoreof_nonstriker]])))
   return round(*new_prediction)



def t20_predictor(current_score, wicketsfallen, overs_completed, scoreof_striker, scoreof_nonstriker):
   dataset = pd.read_csv('data/t20.csv')
   X = dataset.iloc[:, [7,8,9,12,13]].values
   y = dataset.iloc[:, 14].values

   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

   

   lin = LinearRegression()
   lin.fit(X_train, y_train)





   #custom input
   new_prediction = lin.predict((np.array([[current_score, wicketsfallen, overs_completed, scoreof_striker, scoreof_nonstriker]])))
   return round(*new_prediction)











root = Tk()
root.title("Score Predictor App")
root.geometry("400x600")
root.configure(bg="#031e4a")
root.iconbitmap("logo.ico")
def predict_score():
   global fLabel

   if format.get()=="IPL":
      score = ipl_predictor(int(entry1.get()), int(entry2.get()), float(entry3.get()), int(entry4.get()), int(entry5.get()))

      fLabel = Label(frame, text="The Predicted Score is " + str(score))
      fLabel.pack()
   elif format.get()=="ODI":
      score = odi_predictor(int(entry1.get()), int(entry2.get()), float(entry3.get()), int(entry4.get()), int(entry5.get()))

      fLabel = Label(frame, text="The Predicted Score is " + str(score))

      fLabel.pack()
   elif format.get() == "T20":
      score = t20_predictor(int(entry1.get()), int(entry2.get()), float(entry3.get()), int(entry4.get()), int(entry5.get()))

      fLabel = Label(frame, text="The Predicted Score is " + str(score))

      fLabel.pack()
   
   




def predicting_again():
   fLabel.destroy()
   entry1.delete(0, END)
   entry2.delete(0, END)
   entry3.delete(0, END)
   entry4.delete(0, END)
   entry5.delete(0, END)



frame = LabelFrame(root, text="Score Predictor", padx=1, borderwidth=1, bg="#b0b7c2", pady=1)
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)




format = StringVar()
label0 = Label(frame, text="Please Select the Format:")
label0.pack(anchor=W)


formats = [
   "IPL", 
   "T20", 
   "ODI"
]
format.set(formats[2])

dropdown = OptionMenu(frame, format, *formats)
dropdown.pack()

label1 = Label(frame, text="Current Score:").pack(anchor=W, padx=5, pady=5)
entry1 = Entry(frame, width=35)
entry1.pack()

label2 = Label(frame, text="No of Wickets Fallen:").pack(anchor=W, padx=5, pady=5)
entry2 = Entry(frame, width=35)
entry2.pack()

label3 = Label(frame, text="No of overs Completed: ").pack(anchor=W,padx=5, pady=5)
entry3 = Entry(frame, width=35)
entry3.pack()

label4 = Label(frame, text="Score of the Stiker Batsman: ").pack(anchor=W,padx=5, pady=5)
entry4 = Entry(frame, width=35)
entry4.pack()

label5 = Label(frame, text="Score of the Non Stiker Batsman: ").pack(anchor=W,padx=5, pady=5)
entry5 = Entry(frame, width=35)
entry5.pack()

predict_button = Button(frame, text="Click to get the Predicted Score",command=predict_score, padx=5, pady=5, borderwidth=3).pack()

another_prediction = Button(frame, text="Click here to Predict Again", command=predicting_again, padx=5, pady=5).pack()


root.mainloop()



