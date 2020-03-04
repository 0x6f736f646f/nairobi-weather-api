from sqlalchemy import create_engine  
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from models.model import Weather, app
from Utility.get_data import fetch_data

def insert_db(data):
    db_string = app.config['SQLALCHEMY_DATABASE_URI']

    db = create_engine(db_string)  
    base = declarative_base()
    Session = sessionmaker(db)  
    session = Session()
    base.metadata.create_all(db)

    # Create 
    data = Weather(
        location = data['location']['name'],
        region = data['location']['region'],
        localtime = data['location']['localtime'],
        temp_c = data['current']['temp_c'],
        wind_kph = data['current']['wind_kph'],
        wind_degree = data['current']['wind_degree'],
        wind_dir = data['current']['wind_dir'],
        pressure_mb = data['current']['pressure_mb'],
        precip_mm = data['current']['precip_mm'],
        humidity = data['current']['humidity'],
        cloud = data['current']['cloud']
    )  
    session.add(data)  
    session.commit()

def cron():
    with open('Utility/locations.txt', "r+") as f:
        file_data = f.readlines()
    for i in range(0, len(file_data), 1):
        data = fetch_data(file_data[i])
        insert_db(data)
