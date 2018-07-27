
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
	input1, input2, input3, input4= 0,0,0,0
	input1=tkSimpleDialog.askfloat("Value","Please enter temperature in fahrenheit ") # used because to handle the exception i.e, by mistake user not send string data  
	if(input1!=None):
		
		input1="1"+str(input1) # adding check mark to tell web server that it is the temperature in fahrenheit
 		r = requests.post("http://127.0.0.1:5000/Convert", data=input1)		
		input1=input1[1:] # remove check mark
		flag1=1
		if(flag1==1): # stop unnecessary callings to pop-up windows
			root = tk.Tk()
	    	root.withdraw() 
	    	tkMessageBox.showinfo(title="WebServer-Instruction", message="Please enter the URL \"http://127.0.0.1:5000/Convertfahrenheit/"+str(input1)+"\" in the web browser")
	input2=tkSimpleDialog.askfloat("Value","Please enter temperature in celsius")
	if(input2!=None):
		input2="2"+str(input2) # adding check mark to tell web server that it is the temperature in celsius
		r = requests.post("http://127.0.0.1:5000/Convert", data=input2)
		input2=input2[1:]
		flag2=1
		if(flag2==1):
			root = tk.Tk()
	    	root.withdraw() 
	    	tkMessageBox.showinfo(title="WebServer-Instruction", message="Please enter the URL \"http://127.0.0.1:5000/Convertcelsius/"+str(input2)+"\" in the web browser")
	input3=tkSimpleDialog.askfloat("Value","Please enter temperature in kelvin")
	if(input3!=None):
		input3="3"+str(input3) # adding check mark to tell web server that it is the temperature in kelvin
		r = requests.post("http://127.0.0.1:5000/Convert", data=input3)
		input3=input3[1:]
		flag3=1
		if(flag3==1):
			root = tk.Tk()
	    	root.withdraw() 
	    	tkMessageBox.showinfo(title="WebServer-Instruction", message="Please enter the URL \"http://127.0.0.1:5000/Convertkelvin/"+str(input3)+"\" in the web browser")


	input4=tkSimpleDialog.askfloat("Value","Please enter temperature in rankine")
	if(input4!=None):
		input4="4"+str(input4) # adding check mark to tell web server that it is the temperature in rankine
		r = requests.post("http://127.0.0.1:5000/Convert", data=input4)
		input4=input4[1:]   
		flag4=1
		if(flag4==1):
			root = tk.Tk()
	    	root.withdraw() 
	    	tkMessageBox.showinfo(title="WebServer-Instruction", message="Please enter the URL \"http://127.0.0.1:5000/Convertrankine/"+str(input3)+"\" in the web browser")



######################################
######################################
######################################




