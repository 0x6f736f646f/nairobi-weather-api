from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def get_data():
    _transport = RequestsHTTPTransport(
        url='http://localhost:5000/graphql',
        use_json=True,
    )


    client = Client(
        transport=_transport,
        fetch_schema_from_transport=True,
    )
    query = gql("""

    query{
    findLocationData(location: "Juja"){
        uuid
        location
        region
        localtime
        tempC
        windKph
        windDegree
        windDir
        pressureMb
        precipMm
        humidity
        cloud
    }
    }
    """)

    return client.execute(query)