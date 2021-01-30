import requests
import os

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNWU0NDU3ODA0ZmFiODZkMjdkYTViM2RjOTE2OGJkNiIsInN1YiI6IjVmZDRmOTk1MmNlZmMyMDAzZTFkYWUxNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.onqQhBrrSb7-8x75xIczdx0CGk5_rmEmvL2Lx9PMnac"

def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies_list(list_type='popular'):
    return call_tmdb_api(f"movie/{list_type}")

def get_movies(how_many, list_type='popular'):
    data = get_movies_list(list_type)
    return data["results"][: how_many]

def get_image_url(path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{path}"


def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")


def get_single_movie_cast(movie_id):
    response = call_tmdb_api(f"movie/{movie_id}/credits")
    return response['cast']


def get_backdrop(movie_id):
    return call_tmdb_api(f"/movie/{movie_id}/images")

