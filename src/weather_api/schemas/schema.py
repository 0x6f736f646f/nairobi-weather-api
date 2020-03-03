from models.model import Weather, db
from graphene import String, Field, Boolean
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

class WeatherObject(SQLAlchemyObjectType):
    class Meta:
        model = Weather
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_weather_data = SQLAlchemyConnectionField(WeatherObject)
    find_location_data = graphene.Field(lambda: WeatherObject, location = graphene.String())
    
    def resolve_find_location_data(self, info, location):
        data = Weather.query.filter_by(location=location).order_by(Weather.uuid.desc()).first()
        return data
    
our_schema = graphene.Schema(query=Query)