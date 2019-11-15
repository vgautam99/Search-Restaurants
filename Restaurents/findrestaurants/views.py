import geocoder
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from findrestaurants.serializers import FindRestaurantsSerializers, ShowRestaurantsSerializers, ShowRestaurantNearMeSerializer
from findrestaurants.models import Restaurant, RestaurantLocation
from findrestaurants.utils import convert_csv_mongodb, convert_location_csv_to_mongodb, calculate_distance
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
)


class FindRestaurants(ModelViewSet):
    serializer_class = FindRestaurantsSerializers
    queryset = Restaurant.objects.all()
    lookup_field = 'restaurant_name'

    def create(self, request, *args, **kwargs):
        restaurant_details = request.data['restaurant_details']
        restaurant_location = request.data['restaurant_location']
        convert_csv_mongodb(restaurant_details)
        convert_location_csv_to_mongodb(restaurant_location)
        return Response({'message': 'DB created successfully'}, status=HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = Restaurant.objects.all()
        serializer = FindRestaurantsSerializers(queryset, many=True)
        # return Response(serializer.data, status=HTTP_200_OK)
        return render(request, 'index.html', {'queryset': queryset})

    def restaurant_near_me(self, request, *args, **kwargs):
        cuisines_list = self.request.query_params.get('q').split(',')
        restaurant_list = list()
        g = geocoder.ip('me')
        my_latitude = 14.565443 #g.latlng[0]
        my_longitude = 121.027535 #g.latlng[1]
        for restaurant in Restaurant.objects.all():
            restaurant_cuisines_list = restaurant.cuisines
            if set(cuisines_list) & set(restaurant_cuisines_list):
                restaurant_location = RestaurantLocation.objects.filter(restaurant_id=restaurant.restaurant_id).first()
                restaurant_latitude = restaurant_location.latitude
                restaurant_longitude = restaurant_location.longitude
                distance_kms = calculate_distance(my_latitude, my_longitude, restaurant_latitude, restaurant_longitude)
                if distance_kms < 60:
                    restaurant.city = restaurant_location.city
                    restaurant.address = restaurant_location.address
                    restaurant.locality = restaurant_location.locality
                    restaurant.distance = round(distance_kms,2)
                    restaurant_list.append(restaurant)
        if restaurant_list:
            serializer = ShowRestaurantNearMeSerializer(restaurant_list, many=True)
            # return Response(serializer.data, status=HTTP_200_OK)
            return render(request, 'index.html', {'restaurant_list': restaurant_list})
        else:
            return Response({'no restaurant found near your location'}, status=HTTP_422_UNPROCESSABLE_ENTITY)

    def all_restaurant_near_me(self, request, *args, **kwargs):
        g = geocoder.ip('me')
        my_latitude = 14.565443                     #g.latlng[0]
        my_longitude = 121.027535                   #g.latlng[1]
        near_me_restaurant_list = list()
        for restaurant in Restaurant.objects.all():
            restaurant_location = RestaurantLocation.objects.filter(restaurant_id=restaurant.restaurant_id).first()
            restaurant_latitude = restaurant_location.latitude
            restaurant_longitude = restaurant_location.longitude
            distance_kms = calculate_distance(my_latitude, my_longitude, restaurant_latitude, restaurant_longitude)
            if distance_kms < 60:
                restaurant.city = restaurant_location.city
                restaurant.address = restaurant_location.address
                restaurant.locality = restaurant_location.locality
                restaurant.distance = round(distance_kms,2)
                near_me_restaurant_list.append(restaurant)
        if near_me_restaurant_list:
            # serializer = ShowRestaurantNearMeSerializer(near_me_restaurant_list, many=True)
            # return Response(serializer.data, status=HTTP_200_OK)
            return render(request, 'index.html', {'restaurant_list': near_me_restaurant_list})
        else:
            return Response({'no restaurant found near your location'}, status=HTTP_404_NOT_FOUND)






