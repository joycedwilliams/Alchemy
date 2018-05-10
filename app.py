import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Works up til here!!
print(Base.classes.keys())
# Save reference to the table
measurements = Base.classes.measurement
station = Base.classes.stations

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
    )


@app.route("/api/v1.0/precepitation")
def precipitation():
    """Query for the dates and temperature observations from the last year"""
    # Query all dates
    dates_results = session.query(measurement.date).all()

    # Query all temperatures
    temps_results = session.query(measurement.tobs).all()
    
    # Convert list of tuples into normal list
    all_results = list(np.ravel(dates_results))
    all_results2 = list(np.ravel(temp_results))

    # Create a dictionary from the row data and append to a list of
    # dates and temperatures
    all_weather = []
    for temp in temp_results:
        measurement_dict = {}
        measurement_dict["date"] = measurement.date
        measurement_dict["tobs"] = measurement.tobs
        all_weather.append(measurement_dict)   
    
    return jsonify(all_weather)

if __name__ == '__main__':
    app.run(debug=True)


@app.route("/api/v1.0/stations")
def names():
    """Return a list of stations"""
    # Query all stations
    station_results = session.query(station.station).all()

    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def measurement():
    """Return a json list of Temperature Observations (tobs) for the previous year"""
    # Query all the temperatures
    temps_results = session.query(measurement.tobs).all()

    
@app.route("/api/v1.0/<start>")
def measurement():
    """Return a json list of Temperature Observations (tobs) for the previous year"""
    # Query all the temperatures
    temps_results = session.query(measurement.tobs).all()
    
    # Create a dictionary from the row data and append to a list of
    # dates and temperatures
    all_temps = []
    for temp in temp_results:
        temp_dict = {}
        temp_dict["min. temp"] = min.measurement.tobs
        temp_dict["avg. temp"] = mean.mesurement.tobs
        temp_dict["max. temp"] = max.mesurement.tobs
        all_temps.append(temp_dict)   
    
@app.route("/api/v1.0/<start>/<end>")
def measurement():
    """Return a json list of Temperature Observations (tobs) for the previous year"""
    # Query all the temperatures
    temps_results = session.query(measurement.tobs).all()
    
    # Create a dictionary from the row data and append to a list of
    # dates and temperatures
    all_temps = []
    for temp in temp_results:
        temp_dict = {}
        temp_dict["min. temp"] = min.measurement.tobs
        temp_dict["avg. temp"] = mean.mesurement.tobs
        temp_dict["max. temp"] = max.mesurement.tobs
        all_temps.append(temp_dict) 

    return jsonify(all_temps)


if __name__ == '__main__':
    app.run(debug=True)
