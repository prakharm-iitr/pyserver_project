Documentation to setup the webserver for parsing RSS feeds on a website.

Requirements:
	1. Python (v3.8 at the time of testing)
	   check with following commands in the command prompt->
	    Linux  : python3 --version
	    Windows: py --version
	    
Dependencies: (Install temporarily using the steps in next section)
	1. Django server
	2. feedparser module

Setup the environment: (Change directory to rss_reader to easily delete everything in the end)
	1. Make a new virtual environment for Python with the following command in terminal:
		python3 -m venv project
	2. Activate the environment (from the same directory as above):
		source project/bin/activate
	3. Install the dependencies:
		pip install django
		pip install feedparser
		
Starting the server:
	Run the command: python3 manage.py runserver
	From the rss_reader directory (manage.py is located in this directory)
	The server will be accessible on localhost on port 8000, or the URL '127.0.0.1:8000"
