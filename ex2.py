# Маємо певний словник з назвами музичних груп (виконавців) та альбомів. Назва групи використовується як ключ,
# назва альбомів — як значення. Реалізуйте: додавання, видалення, пошук, редагування, збереження та завантаження
# даних (використовуючи стиснення та розпакування)

import pickle
import gzip

bands_albums = {
    'Queen': 'A Night at the Opera',
    'The Beatles': 'Abbey Road',
    'Led Zeppelin': 'IV',
    'Pink Floyd': 'The Dark Side of the Moon',
    'Rolling Stones': 'Exile on Main St.'
}

def add_data(key, value, dct):
    dct[key] = value
    print(f"{key}: {value} added")

def remove_data(key, dct):
    del dct[key]
    print(f"band {key} removed")

def search_country(band, dct):
    for key, value in dct.items():
        if key == band:
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
           bands_albums = pickle.load(rfile)
        print("data loaded")
    except FileNotFoundError:
        print("File not found")

print(bands_albums)

save_data("bands.pkl.gz", bands_albums)
add_data("Some band", "some album", bands_albums)

print(bands_albums)
save_data("bands.pkl.gz", bands_albums)
load_data("bands.pkl.gz")

print(bands_albums)
search_country('Some band', bands_albums)
remove_data('Some band', bands_albums)