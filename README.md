# IdeaHub-API
![](https://github.com/Ogutu-Brian/IdeaHub-API/workflows/Tests/badge.svg)

### PROBLEM
* There are lots of people with ideas, brilliant minds, spread across all over the world.However, most of these people don’t have the resources necessary to make theseideas a success.
* There are lots of people in the world with skills in the world but they do not have anidea of what to build or where to use their skills.
* There are lots of people with resources in the world but they have neither the skillsnor ideas of how to use the resources to make the world a better place.
* There are platforms like SharkTank and other places where these people meet toshare the ideas and resources in order to build something great. However, manypeople in the world cannot afford to go to shark tank either.Conclusion: ​~This is the problem our product solves

# Setting up the project
* Create a virtual environment and activate it
* $ cd IdeaHub-API/
* $ pip install -r requirements.txt
* $ touch .env
* copy content of example_env.txt to .env and update the values to your own configs
* python manage.py runserver


# Running Unit Tests
 ### Running unit tests with test coverage
 * $ coverage run manage.py test

### Checking coverage report
* $ coverage report
  
### Checking coverage report from html
* $ coverage html
* $ cd htmlcov/
* Launch the index html file

### Documentation
https://coverage.readthedocs.io/en/coverage-5.0.3/
