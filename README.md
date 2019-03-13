# Project Happiness

#### Github Page
https://xliu510.github.io/Happiness/index.html

#### Heroku App
https://world-happiness-inc.herokuapp.com/

## Project Description
1) Find factors that is related to happiness. 
2) Make interactive dashboard. 
3) Apply multivariable linear regression to model the relationships between the datasets and make happiness predictions.
4) Utilize training & testing technique for model fitting.

### Landing Page

![LandingPageBookClosed](images/Project03_LandingPage_Capture_Book_Closed.PNG)

![LandingPageBookOpen](images/Project03_LandingPage_Capture_Book_Open.PNG)



# To Run Project:

- Go to **Flask** folder
- Run the following in the folder where app.py is located
```
export FLASK_DEBUG=1
export FLASK_ENV=development
export FLASK_APP=app.py
flask run
```
- Open another terminal window
- Run the following in the folder where index.html is located
```
python -m http.server
```
- Visit project at localhost:5000
**Enjoy!**
