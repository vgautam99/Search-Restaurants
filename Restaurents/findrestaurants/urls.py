from django.urls import path
from findrestaurants.views import FindRestaurants

urlpatterns = [
    path('create_mongodb', FindRestaurants.as_view({'post':'create'})),
    path('', FindRestaurants.as_view({'get':'list'})),
    path('all_restaurants_near_me', FindRestaurants.as_view({'get':'all_restaurant_near_me'}), name='all_restaurants_near_me'),
    path('restaurant_near_me', FindRestaurants.as_view({'get':'restaurant_near_me'}), name='restaurant_near_me'),
]
