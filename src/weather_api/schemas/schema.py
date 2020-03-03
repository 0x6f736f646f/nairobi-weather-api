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
    
our_schema = graphene.Schema(query=Query)