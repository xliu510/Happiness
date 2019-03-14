import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import inspect
from sqlalchemy import MetaData
from sqlalchemy import Table

from flask import Flask, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/World_Happiness_Life_Expectancy_db.sqlite"
db = SQLAlchemy(app)


engine2 = db.engine



@app.route("/")
def index():
    """Return the homepage."""

    return render_template("index.html")



@app.route("/visualization")
def index2():
    """Visualization Page."""

    return render_template("index2.html")

@app.route("/tensorflow")
def tensorflow():
    """Image Classification Page."""

    return render_template("image_test.html")


@app.route("/flaskcode")
def flaskcode():
    """Flask Code Page."""

    return render_template("flask.html")


@app.route("/pandas")
def index_pandas():
    """Data Cleaning and Wrangling Page."""

    return redirect("https://xliu510.github.io/Happiness_JN/")



@app.route("/httpcats")
def index_HttpCats():
    """Http Cats Page."""
    
    return redirect("https://xliu510.github.io/Happiness/cats_index.html")


@app.route("/tableau")
def tableau_link():
    """Tableau Page."""
    
    return redirect("https://public.tableau.com/profile/xing7154#!/vizhome/Happiness_15525426932400/CountryMap")


@app.route("/sandy_graph")
def index_sandyGraph():
    """Http Sandy's Graph Page."""
    
    return render_template("graph.html")



@app.route("/index_jessie")
def map_visual():
   """Bubble Plot"""
   return render_template("index_jessie.html")


@app.route("/happiness_score")
def map_score():
   """Happiness Score Map"""
   return render_template("plot_happiness_score.html")

@app.route("/happiness_rank")
def map_rank():
   """Happiness Rank Map"""
   return render_template("plot_happiness_rank.html")

@app.route("/happiness_kmeans")
def map_kmeans():
   """Happiness Kmeans Map"""
   return render_template("plot_happiness_kmeans_clustering.html")

@app.route("/region/happiness")
def happiness_region():

    #select query

    avg_happiness_region_select = ('SELECT region_2015, avg(happiness_score_2015) as avg_happiness_2015 '
                               ', avg(life_expectancy) as avg_life_2015 '
                               ', avg(hw.value) as avg_whr_2015 '
                              'FROM World_Happiness_Life_Expectancy_tb hl'
                               ' JOIN weekly_hours_avg_worked_job_df_2015_2017_tb hw ON hl.country = hw.country '
                              'GROUP BY region_2015')


    #read query into dataframe
    avg_happiness_region_df = pd.read_sql(avg_happiness_region_select, engine2.connect())

    
    #convert dataframe to list
    happiness_region = avg_happiness_region_df["Region_2015"].values.tolist()
    happiness_score = avg_happiness_region_df["avg_happiness_2015"].values.tolist()
    happiness_life = avg_happiness_region_df["avg_life_2015"].values.tolist()
    happiness_work = avg_happiness_region_df["avg_whr_2015"].values.tolist()

    #create happiness object
    happiness = {
        "region": happiness_region,
        "happiness": happiness_score,
        "life": happiness_life,
        "work": happiness_work
        }

    #return as json object
    return jsonify(happiness)



@app.route("/barplot/<feature>")
def graph_barplot(feature):

    selected_feature = None

    if feature == 'adultmortality':
        selected_feature = 'adult_mortality'
    elif feature == 'lifeexpectancy':
        selected_feature = 'life_expectancy'
    elif feature == 'gdp':
        selected_feature = 'gdp_per_capita_2015'
    elif feature == 'family':
        selected_feature = 'family_2015'
    elif feature == 'health':
        selected_feature = 'health_2015'
    elif feature == 'freedom':
        selected_feature = 'freedom_2015'
    elif feature == 'income':
        selected_feature = 'income'
  


    #select query
    happiness_region_select = ('SELECT country, happiness_score_2015 '
                           f', {selected_feature} as Second_Feature '
                            'FROM World_Happiness_Life_Expectancy_tb '
                            'ORDER BY happiness_score_2015 DESC LIMIT 50')

    #read query into dataframe
    happiness_region_df = pd.read_sql(happiness_region_select, engine2.connect())
    
    #convert dataframe to dictionary
    happiness_region_dict = happiness_region_df.to_dict('records')

    #return as json object
    return jsonify(happiness_region_dict)
    
    


if __name__ == "__main__":
    app.run()
