# IdeaHub-API
[![Build Status](https://travis-ci.org/Ogutu-Brian/IdeaHub-API.svg?branch=develop)](https://travis-ci.org/Ogutu-Brian/IdeaHub-API)
[![Coverage Status](https://coveralls.io/repos/github/Ogutu-Brian/IdeaHub-API/badge.svg?branch=develop)](https://coveralls.io/github/Ogutu-Brian/IdeaHub-API?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/89bcc1f9e85dbe1e1fbd/maintainability)](https://codeclimate.com/github/Ogutu-Brian/IdeaHub-API/maintainability)
### PROBLEM
* There are lots of people with ideas, brilliant minds, spread across all over the world.However, most of these people don’t have the resources necessary to make theseideas a success.
* There are lots of people in the world with skills in the world but they do not have anidea of what to build or where to use their skills.
* There are lots of people with resources in the world but they have neither the skillsnor ideas of how to use the resources to make the world a better place.
* There are platforms like SharkTank and other places where these people meet toshare the ideas and resources in order to build something great. However, manypeople in the world cannot afford to go to shark tank either.Conclusion: ​~This is the problem our product solves

# Requirements
* python 3
* pipenv
  - If you're on MacOS, you can install Pipenv easily with Homebrew:  
      `$ brew install pipenv`
  - Debian Buster+:  
      `$ sudo apt install pipenv`  
  - Fedora:  
      `$ sudo dnf install pipenv`
  - FreeBSD:  
      `$ pkg install py36-pipenv`

# Setting up the project
* Clone the repo :  
   `$ git clone https://github.com/Ogutu-Brian/IdeaHub-API.git`
* Navigate to the cloned folder  
   `$ cd IdeaHub-API/`
* Run:  
   `$ pipenv shell`  
   * This will create a virtual environment and pipfile for package requirements.
* Run:  
   `$ pipenv install` to install the packages in your environment.
* `$ touch .env`
* copy content of example_env.txt to .env and update the values to your own configs
* Run migrations  
   `$ python manage.py migrate`
* Start the server  
   `$ python manage.py runserver`


# Running Unit Tests
 ### Running unit tests with test coverage
 * `$ coverage run manage.py test -v 2`

### Checking coverage report
* $ coverage report
  
### Checking coverage report from html
* `$ coverage html`
* `$ cd htmlcov/`
* Launch the index html file

### Documentation
[Postman API documentation](https://documenter.getpostman.com/view/9068409/Szt8fAc2?version=latest)
