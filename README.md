# ElectriDash - Team 75 Dash/Flask Application

This is a repository that contains the source code for the Dash application currently hosted [here](http://team75.us-east-1.elasticbeanstalk.com/)

## Running the app in a local development server

You will need to install the requirements and then run the app on port 8050, which assuming you have python 3.7 and the corresponding pip, should be done by running:
```
pip install -r requirements.txt
python application.py
```

## Main file structure
    root
    ├── ...
    ├── assets/             # color palette and stylesheets
    ├── database/           # "backend", this are all the data files along with the python scripts that process them and turn the data into awesome Graphs   
    ├── tabs/               # Dash UI components for each tab of the application, referenced from ui.py.
    │   └── tabs.py         # Centralized layout of the tabs
    │   └── tab_x.py        # Code for the ui of each specific tab x
    ├── EPM_datos_Uraba/    # project Jupyter Notebooks and files to explore and model data
    ├── model_outputs /     # Self explanatory
    ├── application.py      # flask application entry point
    ├── ui.py               # ui layout for the Dash appliation specified in appplication.py
    ├── Procfile            # used for AWS ElasticBeanstalk deployment (probably works with Heroku too)
    ├── requirements.txt    # project dependecies      
    └── ...

The ui 

## Contributing to the app
Contributing to the app is just editing the base ui layout file (ui.py), and the tabs that you want to modify, on the tabs folder.
