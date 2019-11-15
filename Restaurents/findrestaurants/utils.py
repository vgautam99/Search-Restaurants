import pandas as pd
from findrestaurants.serializers import FindRestaurantsSerializers, RestaurantLocationSerializer
from math import sin, cos, sqrt, atan2, radians


def convert_csv_mongodb(file):
    df = pd.read_csv(file)
    df = df.fillna(value=0)
    for i in range(len(df.index)):
        d = dict()
        d['restaurant_id'] = df.loc[i, 'Restaurant ID']
        d['restaurant_name'] = df.loc[i, 'Restaurant Name']
        d['cuisines'] = df.loc[i, 'Cuisines']
        if df.loc[i, 'Cuisines'] == 0:
            d['cuisines'] = []
        else:
            d['cuisines'] = df.loc[i, 'Cuisines'].split()
        d['average_cost'] = df.loc[i, 'Average Cost for two']
        d['currency'] = df.loc[i, 'Currency']
        d['has_table_booking'] = df.loc[i, 'Has Table booking']
        d['has_online_delivery'] = df.loc[i, 'Has Online delivery']
        d['aggregate_rating'] = df.loc[i, 'Aggregate rating']
        d['rating_color'] = df.loc[i, 'Rating color']
        d['rating_text'] = df.loc[i, 'Rating text']
        d['votes'] = df.loc[i, 'Votes']
        serializer = FindRestaurantsSerializers(data=d)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return 0


def convert_location_csv_to_mongodb(file):
    df = pd.read_csv(file)
    df = df.fillna(value=0)
    for i in range(len(df.index)):
        d = dict()
        d['restaurant_id'] = df.loc[i, 'Restaurant ID']
        d['country_code'] = df.loc[i, 'Country Code']
        d['city'] = df.loc[i, 'City']
        d['address'] = df.loc[i, 'Address']
        d['locality'] = df.loc[i, 'Locality']
        d['locality_verbose'] = df.loc[i, 'Locality Verbose']
        d['longitude'] = df.loc[i, 'Longitude']
        d['latitude'] = df.loc[i, 'Latitude']
        serializer = RestaurantLocationSerializer(data=d)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return 0


def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6373.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance
