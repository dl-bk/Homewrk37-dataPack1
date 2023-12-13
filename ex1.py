# Маємо певний словник з назвами країн і столиць. Назва
# країни використовується як ключ, назва столиці — як значення. Реалізуйте: додавання, видалення, пошук, редагування,
# збереження та завантаження даних (використовуючи стиснення та розпакування).

import pickle
import gzip

countries_capitals = {
    'Netherlands': 'Amsterdam',
    'Austria': 'Vienna',
    'Norway': 'Oslo',
    'France': 'Paris',
    'Germany': 'Berlin'
}

def add_data(key, value, dct):
    dct[key] = value
    print(f"{key}: {value} added")

def remove_data(key, dct):
    del dct[key]
    print(f"country {key} removed")

def search_country(country, dct):
    for key, value in dct.items():
        if key == country:
            print(f"{key}: {value}")
            return
    return False

def save_data(file, dct):
    with gzip.open(file, "wb") as wfile:
        pickle.dump(dct, wfile)
    print("data saved")

def load_data(file):
    try:
        with gzip.open(file, "rb") as rfile:
           countries_capitals = pickle.load(rfile)
        print("data loaded")
    except FileNotFoundError:
        print("File not found")


print(countries_capitals)

save_data("countries.pkl.gz", countries_capitals)
add_data("Slovakia", "Bratislava", countries_capitals)

print(countries_capitals)
save_data("countries.pkl.gz", countries_capitals)
load_data("countries.pkl.gz")

print(countries_capitals)
search_country('Norway', countries_capitals)
remove_data('Norway', countries_capitals)