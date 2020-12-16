import requests


API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNWU0NDU3ODA0ZmFiODZkMjdkYTViM2RjOTE2OGJkNiIsInN1YiI6IjVmZDRmOTk1MmNlZmMyMDAzZTFkYWUxNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.onqQhBrrSb7-8x75xIczdx0CGk5_rmEmvL2Lx9PMnac"

def get_movies_list(list_type='popular'):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN} "
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies(how_many, list_type='popular'):
    data = get_movies_list(list_type)

    return data["results"][: how_many]


def get_image_url(path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"

    return f"{base_url}{size}/{path}"

        
def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN} "
    }
    response = requests.get(endpoint, headers=headers)

    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN} "
    }
    response = requests.get(endpoint, headers=headers)

    return response.json()['cast']


def get_backdrop(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN} "
    }
    response = requests.get(endpoint, headers=headers)

    return response.json()



