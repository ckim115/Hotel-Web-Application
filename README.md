# Hotel Web Application using Web Development
Team Name: CS Stars\
Team members: Charlene Khun, Christina Kim, Jared Soliven\
Emails: charlene.khun@sjsu.edu, christina.kim@sjsu.edu,  jared.soliven@sjsu.edu\
Problem: There needs to be a convenient way of finding nearby hotels and their amenities.\
Functionality: Our web application provides a space for people to check on nearby hotels, their descriptions, and a link to their website if any. It will also allow users to post reviews or ratings for hotels they have visited.\
What Application Covers: Our application covers web development. We plan to use Flask, Python and possibly a database.\
Description:
The project will result in a web application that lists out the nearby hotels in a certain radius around the user, preferably through a map. It will allow features such as reviewing and rating hotels, which can be done anonymously without a login feature, and the ability to save personal preferences given the user has logged into their account. Upon clicking on a hotel location, it would expand to present more information on the hotel, such as its general description amenities, its average cost per room, a link redirecting to the hotel’s official site, and other users’ reviews.\
We would use Flask, Python, and possibly a database for logins. We would also make use of existing APIs such as Hotel Prices, Hotel Content, and Google Places API to find nearby hotels and their details

Project requirements (Only for initial setup):

- 1) pip is installed
    - note: if you are unsure if you have pip installed, type "pip --version" in the terminal
    - if pip is not installed type:
        - for mac users: python3 -m pip install virtualenv
        - for win users: python -m pip install virtualenv

- 2) pull the latest version of this project
    - git pull

** Please do not push the venv (virtual environment) **

Project Initial Setup:

- 1) Go into the terminal and cd into this project directory

- 2) Check that you're in the correct directory.Once in this directory "Hotel-Web-Appplication", type ls and you should see "README.md, main.py, etc"

- 3) create a virtual environment
    - for mac users: python3 -m venv venv
    - for win users: python -m venv venv

- 4) activate virtual environment
    - for mac users: source venv/bin/activate
    - for win users: venv\Scripts\activate

- 5) install flask
    - type "pip install Flask"

- 6) test that everything is working
    - you should see a file called main.py in the directory
    - type "flask --app main run"
    - you should see that the program is "running on an ip"
    - copy that ip address into a browser and see if you can see a working webpage

- 7) close the server once you are done working
    - press ctrl+c to stop the server/program from running

Running the project after initial setup:

- Go into the Hotel-Web-Application directory
- type "flask --app main run"
- ctrl+c in the terminal when you are done with the program