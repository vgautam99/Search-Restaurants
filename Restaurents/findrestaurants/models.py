from django.db import models
from mongoengine import Document, fields


class Restaurant(Document):
    restaurant_id = fields.IntField(unique=True, required=True)
    restaurant_name = fields.StringField()
    cuisines = fields.ListField()
    average_cost = fields.IntField(min_value=0)
    currency = fields.StringField()
    has_table_booking = fields.StringField(default='No')
    has_online_delivery = fields.StringField(default='No')
    aggregate_rating = fields.FloatField(min_value=0.0, default=0.0)
    rating_color = fields.StringField()
    rating_text = fields.StringField()
    votes = fields.IntField(min_value=0)


class RestaurantLocation(Document):
    restaurant_id = fields.IntField(required=True)
    country_code = fields.IntField()
    city = fields.StringField()
    address = fields.StringField()
    locality = fields.StringField()
    locality_verbose = fields.StringField()
    longitude = fields.FloatField()
    latitude = fields.FloatField()


class RestaurantNearme(Document):
    restaurant_id = fields.IntField(unique=True, required=True)
    restaurant_name = fields.StringField()
    cuisines = fields.ListField()
    average_cost = fields.IntField(min_value=0)
    currency = fields.StringField()
    has_table_booking = fields.StringField(default='No')
    has_online_delivery = fields.StringField(default='No')
    aggregate_rating = fields.FloatField(min_value=0.0, default=0.0)
    rating_color = fields.StringField()
    rating_text = fields.StringField()
    votes = fields.IntField(min_value=0)
    city = fields.StringField()
    address = fields.StringField()
    locality = fields.StringField()