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
vara=0
app = Flask(__name__)
@app.route('/', methods=['GET','POST']) # both redirect to same page i.e., home page
@app.route('/Convert', methods=['GET','POST'])
def Convert():
    global input, vara
    if(request.method=='POST'): # match on the request is POST
        input=request.data #data format is string here
        input.replace(" ","")
        if(input.isspace()):
            root = tk.Tk()  # to hide the root window 
            root.withdraw() 
            tkMessageBox.showinfo(title="Server-Warning!", message="User doesn't enter any value : ENTER SOME DATA INSTEAD OF SPACE")
            return redirect(url_for('Convert'))
        if(input!='' ): #checking value is not empty : Action No action
            lastindex=input[-1]
            if(lastindex=='f' or lastindex== 'F' ): #matching the check mark inserted by client for appropiate conditions
                input=input[:-1]  # removing the check mark to extract original data 
                # redirecting
                return redirect(url_for('Convertfahrenheit',para=input))
            if(lastindex=='c' or lastindex=='C'): #matching the check mark inserted by client for appropiate conditions
                input=input[:-1]  # removing the check mark to extract original data
                # redirecting
                return redirect(url_for('Convertcelsius', para=input)) # redirecting
            if(lastindex=='k' or lastindex=='K'): #matching the check mark inserted by client for appropiate conditions
                input=input[:-1]  # removing the check mark to extract original data
                # redirecting
                return redirect(url_for('Convertkelvin', para=input)) # redirecting
            if(lastindex=='r' or lastindex=='R'): #matching the check mark inserted by client for appropiate conditions
                input=input[:-1]  # removing the check mark to extract original data
                # redirecting
                return redirect(url_for('Convertrankine', para=input))  # redirecting
            if(lastindex!='f' and lastindex!= 'F' and lastindex!='c' and lastindex!='C' and lastindex!='k' and lastindex!='K' and lastindex!='r' and lastindex!='R'):
                
                # redirecting
                return redirect(url_for('ConvertTemperature', para=input))
    return "Temperature Conversion Program  " ### printing the values on the web page

@app.route('/Convertfahrenheit/<para>', methods=['GET','POST'])  
def Convertfahrenheit(para):
     ### conversion logic refer : https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature  ### 
    if(para.isdigit()): #checking the number is digit or not 
        cel= (float(para)-32.0) * (5.0/9.0)
        ranki=float(para) + 459.67
        kel= (float(para) + 459.67) *(5.0/9.0)
        return "celsius={} rankine={}, kelvin={} " .format(cel, ranki, kel) ### printing the values on the web page
    try: #checking number is float or not
        cel= (float(para)-32.0) * (5.0/9.0)
        ranki=float(para) + 459.67
        kel= (float(para) + 459.67) *(5.0/9.0)
        return "celsius={} rankine={}, kelvin={} " .format(cel, ranki, kel) ### printing the values on the web page
    except ValueError: #handling exception if data is not float
        return "Please enter some integer or real number !! "    

@app.route('/Convertcelsius/<para>', methods=['GET','POST'])  
def Convertcelsius(para):  
      ### conversion logic refer : https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature  ### 
    if(para.isdigit()):
        farh=float(para) * (9.0/5.0) +32.0
        ranki=(float(para)+273.15)*(9.0/5.0)
        kel=  float(para) + 273.15
        return "rankine={} fahrenheit={}, kelvin={} " .format(ranki, farh, kel) ### printing the values on the web page
    try:
        farh=float(para) * (9.0/5.0) +32.0
        ranki=(float(para)+273.15)*(9.0/5.0)
        kel=  float(para) + 273.15
        return "rankine={} fahrenheit={}, kelvin={} " .format(ranki, farh, kel) ### printing the values on the web page
    except ValueError:
        return "Please enter some integer or real number !! "    

@app.route('/Convertrankine/<para>',methods=['GET','POST'])  
def Convertrankine(para):
      ### conversion logic refer : https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature  ### 
    if(para.isdigit()): 
        cel  = (float(para) - 491.67) * (5.0/9.0)   
        fah= float(para) - 459.67    
        kel = float(para) * (5.0/9.0)   
        return "celsius={} fahrenheit={}, kelvin={} " .format(cel, fah, kel) ### printing the values on the web page
    try:
        cel  = (float(para) - 491.67) * (5.0/9.0)   
        fah= float(para) - 459.67    
        kel = float(para) * (5.0/9.0)   
        return "celsius={} fahrenheit={}, kelvin={} " .format(cel, fah, kel) ### printing the values on the web page
    except ValueError:
        return "Please enter some integer or real number !! "    


@app.route('/Convertkelvin/<para>', methods=['GET','POST'])  
def Convertkelvin(para):
      ### conversion logic refer : https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature  ### 

    if(para.isdigit()):
        cel = float(para) - float(273.15) 
        fah= (float(para))*(9.0/5.0)- 459.67
        ranki=float(para)*(9.0/5.0)
              
        return "celsius={} fahrenheit={}, rankine={} " .format(cel, fah, ranki)  ### printing the values on the web page
    try:
        cel = float(para) - float(273.15) 
        fah= (float(para))*(9.0/5.0)- 459.67
        ranki=float(para)*(9.0/5.0)
              
        return "celsius={} fahrenheit={}, rankine={} " .format(cel, fah, ranki)  ### printing the values on the web page
    except ValueError:
        return "Please enter some integer or real number !! "  



@app.route('/ConvertTemperature/<para>', methods=['GET','POST'])  
def ConvertTemperature(para):
    return "Please enter the temperature in some valid temperature unit !! "



####### main function to operate the web server at local host (127.0.0.1) #######
if __name__ == "__main__":
    app.run(host="127.0.0.1")



