# Text Summarization Application

This application allows you to upload a PDF file, select summarization options, and generate a summary of the text contained in the PDF. The summary can then be downloaded in MP3 or PDF format.
This application is a web application and can be depoloyed on a real server.

## Project Contents
1. **Most important files** :

- `server.py` : Python script that launches the Flask server.
- `launch.sh` : Bash script that checks dependencies, starts the server, and opens the default web page in the browser.
- `templates/index.html` : Main HTML page of the application.

2. **Front-end** :
All the htlm pages are located in the templates folder (flask requirement).
In all this pages ther is :
-  The `index page` to welcome the custommer
-  The `main page` also call the interface page
-  The `about_us page` communicate about who are the authors
-  The `help page` to explain how does the page is working
For the repetitives parts of the page as the header and the footer, they were in the folder include and they are inculde with a js script. It stand for more modularity in the code.
The Css files use to edit the web page style are in the folder ./static/css.

3. **Back-end** :
Almost all the Back-end is inside the file summaryCreator.py 
This file is use to read the pdf, summerize it and to create the pdf and the mp3 files.
This file is inculde inside the file server.py. 
The file server.py is use to make a communication between the backend and the front-end.

4. **Other Files** :
The images used to illustrate our website are in the folder assets.
The folders toDowload and uploads are here to manage the PDF and MP3 files.


## Prerequisites

- Python 3

## Installation

1. **Clone the repository** :
   ```bash
   git clone <repo-url>
   cd <repo-name>
   ```
## Getting started

2. **Make the script executable** :
    ```bash
    chmod +x launch.sh
    ```
3. **Install Python dependencies (if not installed automatically)** :

Basicly all the packages python needed will be installed with the exeecutable launcher.sh. 
However, you can install the missing ones with pip install <**name of the deb**>

## Usage

1. **Run the script** :
 
    ```bash
    ./launch.sh
    ```
2. **Access the application** :

    The run.sh script launches the server in the background and automatically opens the application's web page in your default browser.
    You can also manually access the application by visiting http://127.0.0.1:5001/ in your browser.

3. **Using the web interface** :

-  Upload a PDF : Click on "Choose PDF File" to upload the PDF file you want to summarize.
    - By default, if there is  no pdf the Lasted_Used.pdf will be proceed. A pdf is inculde by default in the application.
- Select summarization options :
- Choose the type of summary: general, method-oriented, or goal-oriented.
    - Select the language for summarization: English, French, or German.
    - Enter your OpenAI key in the provided field.
- Launch the summary : Click on the "Launch summary" button to generate the summary.
- Preview the summary : The generated summary will appear in the disabled textarea labeled "The sum".
- Download files :
    - Download the summary in MP3 format by clicking "Download MP3".
    - Download the summary in PDF format by clicking "Download PDF".

4. **OpenAI Key** :

    To work, this project need to use the Open AI API
    In order to accedd it, you need to fullfill your openAI key in the requier container. Otherwise the summary can't be done.


