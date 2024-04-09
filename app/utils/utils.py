from random import random


def calculate_distance(src_long, src_lat, dest_lon, dest_lat):
    x = pow(src_long - dest_lon, 2)
    y = pow(src_lat - dest_lat, 2)
    return pow(x + y, 0.5)


def calculate_trip_price(distance):
    base_price = 100.0
    return base_price * distance


def generate_user_ids(id_length=10):
    user_id = ''.join(str(random.randint(0, 9)) for _ in range(id_length))
    return user_id
