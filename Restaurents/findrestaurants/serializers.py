from rest_framework_mongoengine.serializers import DocumentSerializer
from findrestaurants.models import Restaurant, RestaurantLocation, RestaurantNearme


class FindRestaurantsSerializers(DocumentSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class ShowRestaurantsSerializers(DocumentSerializer):
    class Meta:
        model = Restaurant
        exclude = ['id', 'restaurant_id']


class RestaurantLocationSerializer(DocumentSerializer):
    class Meta:
        model = RestaurantLocation
        fields = '__all__'


class ShowRestaurantLocationSerialzer(DocumentSerializer):
    class Meta:
        model = RestaurantLocation
        exclude = ['id', 'restaurant_id']


class ShowRestaurantNearMeSerializer(DocumentSerializer):
    class Meta:
        model = RestaurantNearme
        exclude = ['restaurant_id']