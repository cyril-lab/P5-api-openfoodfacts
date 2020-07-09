### OPEN FOOD FACTS PROGRAM

Author : VERNHES Cyril

#### Description :

This program downloads products from the open Food Facts website using its API. 
The data is saved in a local mysql database. 
The program runs in a terminal and allows you to choose a substitute product 
and save it in the local database. 

#### Prerequisites :

To work, the program requires the minimum versions of : 

Python 3.8 : https://www.python.org/downloads/

Mysql-connector-python 8.0.20 : https://dev.mysql.com/downloads/connector/python/

Requests 2.24.0 : https://fr.python-requests.org/en/latest/user/install.html

Pip 20.0.2 : https://pypi.org/project/pip/

Git : to download the project.

#### Start program and virtual environment : 

Download the project with Git and open the command line and go to project path :

###### Create the directory of virtualenv files named venv :
`python3 -m venv venv`

###### Activate the virtual environment
`venv\Scripts\activate.bat`

###### Install the libraries
`pip install -r requirements.txt`

###### Start program :
`python3 launch.py`

###### Stop virtual environment :
`deactivate`

#### Configurations :

You can change the categories and the maximum number of products downloaded in the files named : config/config.py

#### Controls :

To access to the desired menu, simply type the number corresponding to your choice.

Press "q" to return to the main menu.
Press "s" or "p" in the product menu and in the substitute menu for navigate.
Press "y" or "n" to validate or not the registration of the substitute product.
