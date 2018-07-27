######### Necessary packagees ############

try:
    from Tkinter import *
    import Tkinter as tk

except ImportError:
    from tkinter import *
    import tkinter as tk

import tkMessageBox
import tkSimpleDialog
from flask import Flask, redirect, url_for
from flask import jsonify
from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
from flask import Flask, Response, request
import flask

####################################################



#####################################################
################   SERVER SIDE       ################
################    MAIN LOGIC       ################
#####################################################




input=0
app = Flask(__name__)
@app.route('/', methods=['GET','POST']) # both redirect to same page i.e., home page
@app.route('/Convert', methods=['GET','POST'])
def Convert():
    global input
    if(request.method=='POST'): # match on the request is POST
        input=request.data #data format is string here
        
        if(input[0]=='1'): #matching the check mark inserted by client for appropiate conditions
            input=input[1:]  # removing the check mark to extract original data 
            input=float(input)#convert the original data into float
         # redirecting
            return redirect(url_for('Convertfahrenheit',para=input))
        if(input[0]=='2'): #matching the check mark inserted by client for appropiate conditions
            input=input[1:]  # removing the check mark to extract original data
            input=float(input)#convert the original data into float
            return redirect(url_for('Convertcelsius', para=input)) # redirecting
        if(input[0]=='3'): #matching the check mark inserted by client for appropiate conditions
            input=input[1:]  # removing the check mark to extract original data
            input=float(input)#convert the original data into float
            return redirect(url_for('Convertkelvin', para=input)) # redirecting
        if(input[0]=='4'): #matching the check mark inserted by client for appropiate conditions
            input=input[1:]  # removing the check mark to extract original data
            input=float(input)    #convert the original data into float
            return redirect(url_for('Convertrankine', para=input))  # redirecting
    return "Temperature Conversion Program  " ### printing the values on the web page

@app.route('/Convertfahrenheit/<para>', methods=['GET','POST'])  
def Convertfahrenheit(para):
     ### conversion logic refer : https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature  ### 
    cel= (float(para)-32.0) * (5.0/9.0)
    ranki=float(para) + 459.67
    kel= (float(para) + 459.67) *(5.0/9.0)
    return "celsius={} rankine={}, kelvin={} " .format(cel, ranki, kel) ### printing the values on the web page


@app.route('/Convertcelsius/<para>', methods=['GET','POST'])  
def Convertcelsius(para):  
      ### conversion logic refer : https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature  ### 
    farh=float(para) * (9.0/5.0) +32.0
    ranki=(float(para)+273.15)*(9.0/5.0)
    kel=  float(para) + 273.15
    return "rankine={} fahrenheit={}, kelvin={} " .format(ranki, farh, kel) ### printing the values on the web page


@app.route('/Convertrankine/<para>',methods=['GET','POST'])  
def Convertrankine(para):
      ### conversion logic refer : https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature  ### 
    cel  = (float(para) - 491.67) * (5.0/9.0)   
    fah= float(para) - 459.67    
    kel = float(para) * (5.0/9.0)   
    return "celsius={} fahrenheit={}, kelvin={} " .format(cel, fah, kel) ### printing the values on the web page


@app.route('/Convertkelvin/<para>', methods=['GET','POST'])  
def Convertkelvin(para):
      ### conversion logic refer : https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature  ### 
    cel = float(para) - float(273.15) 
    fah= (float(para))*(9.0/5.0)- 459.67
    ranki=float(para)*(9.0/5.0)
          
    return "celsius={} fahrenheit={}, rankine={} " .format(cel, fah, ranki)  ### printing the values on the web page

####### main function to operate the web server at local host (127.0.0.1) #######
if __name__ == "__main__":
    app.run(host="127.0.0.1")



