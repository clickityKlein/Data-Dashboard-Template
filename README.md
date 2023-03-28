# Data Dashboard Template
This template lays the foundation for creating a dashboard that can be uploaded
to a webpage using basic HTML, Flask, Plotly, and Bootstrap.

Discussed below (in this README), are the basics of this template and 
the process for uploading the webpage to a server. In this case,
the webpage was uploaded through a heroku server.

This was designed following a Udacity course project, but was completed outside
the Udacity environment. Both upload pathways will be detailed.


## Table of Contents
- [Libraries Used](#libraries-used)
- [Project Motivation](#project-motivation)
- [File Descriptions](#file-descriptions)
- [Directory Tree: Before](#directory-before)
- [Directory Tree: After](#directory-after)
- [Before the Upload](#before-the-upload)
- [Ready to Upload](#ready-to-upload)
- [Future Considerations](#future-considerations)


## Libraries Used
Note that once the app is ready to be uploaded, a requirements.txt file will be 
created. This file will be created in a virtual environment, a common recommendation. 
However, the following libraries are paramount to this template construction prior to 
a server upload.

- Flask
- Numpy
- Pandas
- Plotly

Additionally, the HTML file calls in a Bootstrap template. The Bootsrap website
features many templates which provide a front-end framework, essentially 
eliminating the need for CSS or Javascript.

[Table of Contents](#table-of-contents)

## Project Motivation
The initial objective was to practice creating a dashboard and uploading the
dashboard to a server to be reached like any other website.

However, the initial exercise supplied the following two opportunities:
1. Create a dashboard template that is quick to duplicate for multiple uses.
2. Create a detailed account of template creation and the upload process.

For the second point above, both the initial template creation and the upload
process came with their share of troubleshooting. Documenting the entire
troubleshooting process and sharing what was found will help not only recreate
this exact webpage, but hopefully other users finding the same issues.

[Table of Contents](#table-of-contents)

## File Descriptions
There will be three "sets" of files available in this repository:
1. Before the upload to a server phase
2. After the upload to a server phase
3. Supporting files and images for this repository and README

Visually, it'll help to examine the directory trees for the files and folders created 
for each phase. The files and folders locations and nomenclature can be confusing, so 
hopefully these maps will help.

Note that the pycache folders are automatically created.


## Directory Tree: Before

![Directory Tree Level B1](Images/directory_tree1.png)

![Directory Tree Level B2](Images/directory_tree2.png)

![Directory Tree Level B3](Images/directory_tree3.png)


## Directory Tree: After

![Directory Tree Level A1](Images/directory_tree4.png)

![Directory Tree Level A2](Images/directory_tree5.png)

![Directory Tree Level A3](Images/directory_tree6.png)

[Table of Contents](#table-of-contents)

## Before The Upload
Referring to first of six images above, there will be 3 main folders and 1 main python file.

- The **data** folder contains any csv files
- The **myapp** folder contains 2 main folders, **static** and **templates**, and 
2 main files, **\_\_init\_\_.py** and **routes.py**
- The **\_\_init\_\_.py** file imports Flask
- The **routes.py** file tells the webpage how to use and render the 
**wrangle_data.py** file (see below)
- The **static** folder contains the **img** folder, which contains any images used
- The **templates** folder contains the webpage itself, **index.html**
- The **index.html** is the webpage design
- The **wrangling_scripts** folder contains a python file called **wrangle_data.py**
- The **wrangle_data.py** file is used to import, clean and plot data
- The **myapp.py** file will allow a terminal to access the flask app, deploying a
development server into a web browswer (only accessible to the user)

These notes won't dive too deep into the other python files, but it's important to
draw attention to the **myapp.py** file.

**myapp.py**
```python
# simple script to run the web application
from myapp import app
app.run()
```

The **app.run()** portion of the code is a necessary method to deploy the
application locally.

Once it's time to test the webpage (deploy locally), in a terminal, type the 
following command:
```
python myapp.py
```

If everything is setup properly, a URL should be created and will look like:
```
http://127.0.0.1:5000/
```

Copy and past the URL into a browswer, and this will deploy a dashboard locally.

This is where the user can test any code or file edits before deploying to a server.


[Table of Contents](#table-of-contents)


## Ready to Upload
[Table of Contents](#table-of-contents)


## Future Considerations
[Table of Contents](#table-of-contents)