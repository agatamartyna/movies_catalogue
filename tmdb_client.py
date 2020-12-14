import requests
from random import sample

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNWU0NDU3ODA0ZmFiODZkMjdkYTViM2RjOTE2OGJkNiIsInN1YiI6IjVmZDRmOTk1MmNlZmMyMDAzZTFkYWUxNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.onqQhBrrSb7-8x75xIczdx0CGk5_rmEmvL2Lx9PMnac"
    headers = {
        "Authorization": f"Bearer {api_token} "
    }
    response = requests.get(endpoint, headers=headers)

    return response.json()


def get_movies(how_many):
    data = get_popular_movies()

    return sample(data["results"], how_many)


def get_poster_url(poster_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"

    return f"{base_url}{size}/{poster_path}"


def get_movie_info():
    data = get_popular_movies()['results']
    movies = []
    for item in data:
        d = dict(title=item['title'], poster_path=get_poster_url(item['poster_path']))
        movies.append(d)

    return movies


if __name__ == "__main__":
    print(get_movies(8))




