from flask import Flask
from flask_graphql import GraphQLView
from schemas.schema import our_schema
from models.model import app
import time, atexit
from apscheduler.schedulers.background import BackgroundScheduler
from Utility.job import cron

app.secret_key = os.environ['APP_SECRET_KEY']
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=our_schema, graphiql=True))

@app.route('/')
def index():
    return "GraphQL server is listening on /graphql"


scheduler = BackgroundScheduler()
scheduler.add_job(func=cron, trigger="interval", minutes=5)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    app.run()

