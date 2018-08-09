Configuration:
-------------
The program works well on any system. There is no such system requirement but its good to have Linux operating system because most troubleshooting step solution is in Linux only.

Installation instructions:
--------------------------

* Any python version greater than or equal to 2.6
* Install the packages mentioned on the top of a program using 
  pip install package-name [for python 2]
  pip3 install package-name [for python 3]

Operating instructions:
-----------------------

Step 1: First run the file on the folder WebServer.
         Command: python WebServer.py
Step 2: Open the URL shown on the terminal window in a web browser.
Step 3: Edit the URL in the web browser like if you want to check the temperature conversion of
   	one unit into other units.
    	For Example: If you want to see the conversion of 212 fahrenheit into other scales then
            	     you need edit the URL like http://localhost:5000/convert/fahrenheit/212/ 
            	     in place of 212, you can write an integer, real or string.
Note: We consider only four temperature units, i.e., fahrenheit, kelvin, celsius, and rankine.
Step 4: User can change the temperature units also to see the variations in the output.

Troubleshooting:
---------------

Copy the error and paste into google and refer the StackOverflow link

