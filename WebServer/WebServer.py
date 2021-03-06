#########      Necessary packages        ############


from flask import jsonify, Flask


######################################################

#####################################################
################   SERVER SIDE       ################
################   MAIN LOGIC        ################
#####################################################

inputs=0
vara=0
app = Flask(__name__)
#routing or mapping the URL
@app.route('/', methods=['GET','POST']) # both redirect to same page i.e., home page
@app.route('/convert/', methods=['GET','POST'])
def convert():
    return "Temperature Conversion Program  " ### printing the values on the web page


@app.route('/convert/fahrenheit/', methods=['GET','POST'])
@app.route('/convert/fahrenheit/<para>/', methods=['GET','POST'])  
def fahrenheit(para=None):
     ### conversion logic refer : https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature  ### 
    if(para==None):
        return "please enter some value"
    para=para.replace(" ","")
    para = para.replace(",", "")
    if(para.isdigit()): #checking the number is digit or not 
        cel= (float(para)-32.0) * (5.0/9.0)
        ranki=float(para) + 459.67
        kel= (float(para) + 459.67) *(5.0/9.0)
        return jsonify(celsius=cel, rankine=ranki, kelvin=kel)
    try: #checking number is float or not
        cel= (float(para)-32.0) * (5.0/9.0)
        ranki=float(para) + 459.67
        kel= (float(para) + 459.67) *(5.0/9.0)
        return jsonify(celsius=cel, rankine=ranki, kelvin=kel)
    except ValueError: #handling exception if data is not float
        return "Please enter some integer or real number !! "

@app.route('/convert/celsius/', methods=['GET','POST']) 
@app.route('/convert/celsius/<para>/', methods=['GET','POST'])  
def celsius(para=None):  
      ### conversion logic refer : https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature  ### 
    if(para==None):
        return "please enter some value"
    para=para.replace(" ","")
    para = para.replace(",", "")
    if(para.isdigit()):
        farh=float(para) * (9.0/5.0) + 32.0
        ranki=(float(para)+273.15)*(9.0/5.0)
        kel=  float(para) + 273.15
        return jsonify(rankine=ranki, kelvin=kel, fahrenheit=farh)
    try:
        farh=float(para) * (9.0/5.0) +32.0
        ranki=(float(para)+273.15)*(9.0/5.0)
        kel=  float(para) + 273.15
        return jsonify(rankine=ranki, kelvin=kel, fahrenheit=farh)
    except ValueError:
        return "Please enter some integer or real number !! "    


@app.route('/convert/rankine/',methods=['GET','POST'])  
@app.route('/convert/rankine/<para>/',methods=['GET','POST'])
def rankine(para=None):
      ### conversion logic refer : https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature  ### 
    if(para==None):
        return "please enter some value"
    para=para.replace(" ","")
    para = para.replace(",", "")
    if(para.isdigit()):
        cel  = (float(para) - 491.67) * (5.0/9.0)   
        fah= float(para) - 459.67    
        kel = float(para) * (5.0/9.0)   
        return jsonify(fahrenheit=fah, celsius=cel, kelvin=kel)
    try:
        cel  = (float(para) - 491.67) * (5.0/9.0)   
        fah= float(para) - 459.67    
        kel = float(para) * (5.0/9.0)   
        return jsonify(fahrenheit=fah, celsius=cel, kelvin=kel)
    except ValueError:
        return "Please enter some integer or real number !! "    

@app.route('/convert/kelvin/', methods=['GET','POST'])
@app.route('/convert/kelvin/<para>/', methods=['GET','POST'])  
def kelvin(para=None):
      ### conversion logic refer : https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature  ### 
    if(para==None):
        return "please enter some value"
    para=para.replace(" ","")
    para = para.replace(",", "")
    if(para.isdigit()):
        cel = float(para) - float(273.15) 
        fah= (float(para))*(9.0/5.0)- 459.67
        ranki=float(para)*(9.0/5.0)
              
        return jsonify(celsius=cel, fahrenheit=fah, rankine=ranki)
    try:
        cel = float(para) - float(273.15) 
        fah= (float(para))*(9.0/5.0)- 459.67
        ranki=float(para)*(9.0/5.0)
              
        return jsonify(celsius=cel, fahrenheit=fah, rankine=ranki)
    except ValueError:
        return "Please enter some integer or real number !! "  

####### main function to operate the web server at local host (127.0.0.1) #######
if __name__ == "__main__":
    app.run(host="localhost") # Debug= True when u are in developer mode
