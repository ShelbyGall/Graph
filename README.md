# Brain Book
Since I keep forgetting things due to breaks in development, im going to use the top part of this markdown document as a sort of brain book for how im developing this project. Basically everything above the "Graph" header is going to be brain book material that I will later condense as necessary to become the final README.md

- GUI
    - im cooked basically
- CICD pipeline
- optimizations

# Graph
A simple Graph implementation in python

# How to Run
### For Development 
we are using python venv for project package management

1. Activate virtual environment

- Windows (powershell)
`env/Scripts/activate.bat or env/Scripts/activate`
or
`source env/Scripts/activate`

- Mac/Linux (bash)
`source env/bin/activate`
**NOTE: to make sure youre in the virtual environment, run the command pip list. You should see very few packages since this will only show the current packages installed in the project environment rather than all the packages installed on your system**

2. Deactivate virtual environment
- Windows/Mac/Linux
`deactivate`

3. Saving list of requirements for the package to a txt file for easy use on other machines
`pip freeze > requirements.txt`

4. Creating a virtual environment and installing the package requirements
- `python3 -m venv env`
- `source env/Scripts/activate`
- `pip install -r requirements.txt`
