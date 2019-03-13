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

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################


# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/bellybutton.sqlite"
# db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/World_Happiness_Life_Expectancy_db.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
#Base = automap_base()
# reflect the tables
#Base.prepare(db.engine, reflect=True)

engine2 = db.engine
#connection = engine.connect()


#metadata = MetaData()
#metadata.reflect(bind=db.engine)

# Save references to each table
# Samples_Metadata = Base.classes.sample_metadata
# Samples = Base.classes.samples
# # The database URI
# engine = create_engine("sqlite:///db/World_Happiness_Life_Expectancy_db.sqlite")

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)

# Save reference to the table
# Trip = Base.classes.trip
# Station = Base.classes.station

# # Create our session (link) from Python to the DB
# session = Session(engine)



@app.route("/")
def index():
    """Return the homepage."""
    
    # dist_city_sql = (f'SELECT DISTINCT city FROM station ')
    # dist_city = pd.read_sql(dist_city_sql, engine2.connect())
    # dist_city_list = dist_city["city"].values.tolist()
    dist_city_list = 'hello'
    # results = session.query(Station.city).distinct()
    # cities = [result[0] for result in results]

    return render_template("index.html")

@app.route("/visualization")
def index2():
    """Visualization Page."""
    
    # dist_city_sql = (f'SELECT DISTINCT city FROM station ')
    # dist_city = pd.read_sql(dist_city_sql, engine2.connect())
    # dist_city_list = dist_city["city"].values.tolist()
    dist_city_list = 'hello'
    # results = session.query(Station.city).distinct()
    # cities = [result[0] for result in results]

    return render_template("index2.html")


@app.route("/pandas")
def index_pandas():
    """Data Cleaning and Wrangling Page."""
    
    # dist_city_sql = (f'SELECT DISTINCT city FROM station ')
    # dist_city = pd.read_sql(dist_city_sql, engine2.connect())
    # dist_city_list = dist_city["city"].values.tolist()
    dist_city_list = 'hello'
    # results = session.query(Station.city).distinct()
    # cities = [result[0] for result in results]

    return render_template("Import-export-clean-data.html")


@app.route("/httpcats")
def index_HttpCats():
    """Http Cats Page."""
    
    # dist_city_sql = (f'SELECT DISTINCT city FROM station ')
    # dist_city = pd.read_sql(dist_city_sql, engine2.connect())
    # dist_city_list = dist_city["city"].values.tolist()
    dist_city_list = 'hello'
    # results = session.query(Station.city).distinct()
    # cities = [result[0] for result in results]

    return render_template("cats_index.html")

@app.route("/sandy_graph")
def index_sandyGraph():
    """Http Sandy's Graph Page."""
    
    # dist_city_sql = (f'SELECT DISTINCT city FROM station ')
    # dist_city = pd.read_sql(dist_city_sql, engine2.connect())
    # dist_city_list = dist_city["city"].values.tolist()
    # dist_city_list = 'hello'
    # results = session.query(Station.city).distinct()
    # cities = [result[0] for result in results]

    return render_template("graph.html")

@app.route("/index_jessie")
def map_visual():
   """Return the homepage."""
   return render_template("index_jessie.html")


@app.route("/2015/<feature>")
def end_station_data(feature):
    # Query for the top 10 most popular stations
    # results = session.query(Trip.end_station_name, func.count(Trip.end_station_id)).group_by(Trip.end_station_name).order_by(func.count(Trip.end_station_id).desc()).limit(20).all()
    
    # # Create lists from the query results
    # station_names = [result[0] for result in results]
    # end_station_id = [result[1] for result in results]
    
    # Query for the top 10 most popular stations
    selected_feature = feature

    if selected_feature == 'freedom':
        selected_feature = 'Freedom_2015'
    elif selected_feature == 'gdp':
        selected_feature = 'GDP_per_Capita_2015'
    

    # 'Region':'Region_2015',
    # 'Happiness Rank':'Happiness_Rank_2015',
    # 'Happiness Score':'Happiness_Score_2015',
    # 'Standard Error':'Standard_Error_2015',
    # 'Economy (GDP per Capita)':'GDP_per_Capita_2015',
    # 'Family':'Family_2015',
    # 'Health (Life Expectancy)':'Health_2015','Freedom':'Freedom_2015','Trust (Government Corruption)':'Government_Trust_2015','Generosity':'Generosity_2015','Dystopia Residual':'Dystopia_Residual_2015'

    happiness_2015_feature_sql =(f'SELECT Happiness_Score_2015, {selected_feature} '
                 'FROM World_Happiness_Report_2015_2016_2017_tb')

    happiness_2015_feature_df = pd.read_sql(happiness_2015_feature_sql, engine2.connect())

    # selected_city = city
    # station_end_ct_select = station_end_ct[station_end_ct["city"]==selected_city].nlargest(10, 'ct')

    happiness_2015_x = happiness_2015_feature_df["Happiness_Score_2015"].values.tolist()
    happiness_2015_y = happiness_2015_feature_df[selected_feature].values.tolist()
    
    # Generate the plot trace
    trace = {
        "x": happiness_2015_x,
        "y": happiness_2015_y,
        "type": "bar"
    }
    return jsonify(trace)

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
