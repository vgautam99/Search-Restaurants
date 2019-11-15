
![alt text](https://github.com/vgautam99/Search-Restaurants/blob/master/Restaurents/staticfiles/images/homepage.png)


Note: To test apis uncomment return statements in views.py
Note: Please activate Virtual Enviroment first.

APIs

1. http://127.0.0.1:8000/find/create_mongodb   (Method: post)

Postman body form data:
    restaurant_details:restaurantsa9126b3.csv
    restaurant_location:restaurant_addc9a1430.csv

Description: This api is used to convert csv file to mongodb database.


2. http://127.0.0.1:8000/       (Method: get)

Description: this url is homepage, here all restaurants are present.

Response:
[
    {
        "id": "5dbecd40c458e448933fb34e",
        "restaurant_id": 6317637,
        "restaurant_name": "Le Petit Souffle",
        "cuisines": [
            "French,",
            "Japanese,",
            "Desserts"
        ],
        "average_cost": 1100,
        "currency": "Botswana Pula(P)",
        "has_table_booking": "Yes",
        "has_online_delivery": "No",
        "aggregate_rating": 4.8,
        "rating_color": "Dark Green",
        "rating_text": "Excellent",
        "votes": 314
    },
    {
        "id": "5dbecd41c458e448933fb3b1",
        "restaurant_id": 17284390,
        "restaurant_name": "The Catch Seafood Room & Oyster Bar",
        "cuisines": [
            "Seafood,",
            "Tapas,",
            "Bar",
            "Food"
        ],
        "average_cost": 40,
        "currency": "Dollar($)",
        "has_table_booking": "No",
        "has_online_delivery": "No",
        "aggregate_rating": 3.8,
        "rating_color": "Yellow",
        "rating_text": "Good",
        "votes": 250
    }
]


3. http://127.0.0.1:8000/all_restaurants_near_me    (Method: get)

Description: this api will return restaurants near your location based on geoip.

Response:

[
    {
        "id": "5dbecd40c458e448933fb34e",
        "restaurant_name": "Le Petit Souffle",
        "cuisines": [
            "French,",
            "Japanese,",
            "Desserts"
        ],
        "average_cost": 1100,
        "currency": "Botswana Pula(P)",
        "has_table_booking": "Yes",
        "has_online_delivery": "No",
        "aggregate_rating": 4.8,
        "rating_color": "Dark Green",
        "rating_text": "Excellent",
        "votes": 314,
        "city": "Makati City",
        "address": "Third Floor, Century City Mall, Kalayaan Avenue, Poblacion, Makati City",
        "locality": "Century City Mall, Poblacion, Makati City"
    },
    {
        "id": "5dbecd40c458e448933fb363",
        "restaurant_name": "The Food Hall by Todd English",
        "cuisines": [
            "American,",
            "Asian,",
            "Italian,",
            "Seafood"
        ],
        "average_cost": 1800,
        "currency": "Botswana Pula(P)",
        "has_table_booking": "Yes",
        "has_online_delivery": "No",
        "aggregate_rating": 4.5,
        "rating_color": "Dark Green",
        "rating_text": "Excellent",
        "votes": 618,
        "city": "Taguig City",
        "address": "Fifth Floor, SM Aura Premier, C5 Corner 26th Street, Bonifacio Global City, Taguig City",
        "locality": "SM Aura Premier, Bonifacio Global City, Taguig City"
    }
]


4. http://127.0.0.1:8000/restaurant_near_me      (Method: get)

query parameter: French,Japanese,Desserts

Description: this api will return restaurant near your location based on cuisines you search.

[
    {
        "id": "5dbecd40c458e448933fb34e",
        "restaurant_name": "Le Petit Souffle",
        "cuisines": [
            "French,",
            "Japanese,",
            "Desserts"
        ],
        "average_cost": 1100,
        "currency": "Botswana Pula(P)",
        "has_table_booking": "Yes",
        "has_online_delivery": "No",
        "aggregate_rating": 4.8,
        "rating_color": "Dark Green",
        "rating_text": "Excellent",
        "votes": 314,
        "city": "Makati City",
        "address": "Third Floor, Century City Mall, Kalayaan Avenue, Poblacion, Makati City",
        "locality": "Century City Mall, Poblacion, Makati City"
    },
    {
        "id": "5dbecd40c458e448933fb362",
        "restaurant_name": "NIU by Vikings",
        "cuisines": [
            "Seafood,",
            "American,",
            "Mediterranean,",
            "Japanese"
        ],
        "average_cost": 3000,
        "currency": "Botswana Pula(P)",
        "has_table_booking": "Yes",
        "has_online_delivery": "No",
        "aggregate_rating": 4.7,
        "rating_color": "Dark Green",
        "rating_text": "Excellent",
        "votes": 535,
        "city": "Taguig City",
        "address": "Sixth Floor, SM Aura Premier, C5 Road Corner 26th Street, Bonifacio Global City, Taguig City",
        "locality": "SM Aura Premier, Bonifacio Global City, Taguig City"
    }
]
 
