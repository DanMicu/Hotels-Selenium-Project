# Hotels-Selenium-Project
This is my final project for the IT Factory automation testing exam

For this project I decided to test various functionality features on the ca.hotels.com website which include tests to the home page, the search results page and the sign in page

# Prerequisites:
1. Install python on your laptop/pc
2. Install Pycharm on your laptop/pc
3. Install git on your laptop/pc

# Steps in order to import the project:
1. Open Pycharm and create a new project with a Virtualenv environment
2. Import the project using the repository link by typing git clone (repo link) in the terminal
3. Install all required packages found within the requirements.txt file which can be done by typing pip install -r requirements.txt in the terminal
4. Last step would be to type behave in the terminal in order to run the tests 

# Short explanation of the files found within the project:
The main folder is the features folder which includes:
  - "Pages" folder with 4 python files, one for each page tested
  - “Steps” folder with 3 python files, one for each page tested, excluding the home page
  - “Browser.py” file which has the Browser class where our driver and other important functions are stored
  - "Environment.py" with the code we want to run before and after each test
  - Three files with the extension .feature are also present, within which we have the scenarios written in Gherkin syntax that we need in order to run our tests
  - "Reports" folder with several HTML reports of the tests run in this project, which you can open from the file location
  - Folders like .gitignore, requirements.txt, README.md and behave.ini are also present in the project
  
  # Report results screenshot:
  ![HTMLREPORT](https://user-images.githubusercontent.com/108822285/207373141-fbc3938b-861f-4a24-81f6-edd35537ec69.png)

  # Recording of the tests being executed:
    
