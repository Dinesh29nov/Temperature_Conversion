
######### Necessary packagees ############

from flask import Flask, render_template, request
import random, socket, threading
import requests 
try:
    from Tkinter import *
    import Tkinter as tk

except ImportError:
    from tkinter import *
    import tkinter as tk

import tkMessageBox
import tkSimpleDialog
####################################################



#####################################################
################   CLIENT SIDE       ################
################    MAIN LOGIC       ################
#####################################################



while(1): #infinite while loop for sending infinite reading of temperature	

	root = tk.Tk()  # to hide the root window 
 	root.withdraw()	
	tkMessageBox.showinfo(title="Instruction", message="Please enter the temperature")
	input=0
	input=tkSimpleDialog.askstring("Value","Please enter temperature  ") # used because to handle the exception i.e, by mistake user not send string data  
	r = requests.post("http://127.0.0.1:5000/Convert", data=input)
	if(input==None or input==''): #value is not null or not 
		continue
	input.replace(" ","") #eliminate whitespaces
	if(input.isspace()): #check enter is only spaces
		root = tk.Tk()  # to hide the root window 
		root.withdraw()	
		tkMessageBox.showinfo(title="Client-Warning!", message="Please enter some value instead of space :: REFRESH THE BROWSER TO SEE THE ERROR MESSAGE")
		continue
	if(input[-1]=='R' or input[-1]=='r'):
		input=input[:-1]
		root = tk.Tk()
		root.withdraw() 
		tkMessageBox.showinfo(title="Instruction", message="Please enter the URL \"http://127.0.0.1:5000/Convertrankine/"+str(input)+"\" in the web browser")
		continue
	if(input[-1]=='K' or input[-1]=='k'):
		input=input[:-1]
		root = tk.Tk()
		root.withdraw() 
		tkMessageBox.showinfo(title="Instruction", message="Please enter the URL \"http://127.0.0.1:5000/Convertkelvin/"+str(input)+"\" in the web browser")
		continue
	if(input[-1]=='C' or input[-1]=='c'):
		input=input[:-1]
		root = tk.Tk()
		root.withdraw() 
		tkMessageBox.showinfo(title="Instruction", message="Please enter the URL \"http://127.0.0.1:5000/Convertcelsius/"+str(input)+"\" in the web browser")
		continue
	if(input[-1]=='f' or input[-1]=='F'):
		input=input[:-1]
		root = tk.Tk()
		root.withdraw() 
		tkMessageBox.showinfo(title="Instruction", message="Please enter the URL \"http://127.0.0.1:5000/Convertfahrenheit/"+str(input)+"\" in the web browser")
		continue
	if(input[-1]!='f' and input[-1]!='F' and input[-1]!='R' and input[-1]!='r' and input[-1]!='K' and input[-1]!='k' and input[-1]!='C' and input[-1]!='c'):
		root = tk.Tk()
		root.withdraw() 
		tkMessageBox.showinfo(title="Instruction", message="Please enter the URL \"http://127.0.0.1:5000/ConvertTemperature/"+str(input)+"\" in the web browser")
		continue



######################################
######################################
######################################




