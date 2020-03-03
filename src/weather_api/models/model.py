from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from config import app, db


class Weather(db.Model):
    __tablename__ = 'weather'
    uuid = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    location = db.Column(db.String(256))
    region = db.Column(db.Text)
    localtime = db.Column(db.String)
    temp_c = db.Column(db.Float)
    wind_kph = db.Column(db.Float)
    wind_degree = db.Column(db.Float)
    wind_dir = db.Column(db.Text)
    pressure_mb = db.Column(db.Float)
    precip_mm = db.Column(db.Float)
    humidity = db.Column(db.Float)
    cloud = db.Column(db.Float)

    def __repr__(self):
        return 'Weather %r' % self.location
