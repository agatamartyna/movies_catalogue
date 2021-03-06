from flask import Flask, render_template, request
import tmdb_client
from random import choice

app = Flask(__name__)


@app.context_processor
def utility_processor():
    def tmbd_image_url(path, size):
        return tmdb_client.get_image_url(path, size)
    return {"tmdb_image_url": tmbd_image_url}


@app.route('/')
def homepage():
    lists = ["now_playing", "popular", "top_rated", "upcoming"]
    selected_list = request.args.get('list_type', "popular")
    if selected_list not in lists:
        selected_list = "popular"
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list, )
    return render_template("homepage.html", movies=movies,
                           current_list=selected_list, lists=lists)


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    backdrop_images = tmdb_client.get_backdrop(movie_id)
    random_backdrop = choice(backdrop_images['backdrops'])
    return render_template("movie_details.html", movie=details,
                           cast=cast, random_backdrop=random_backdrop)


if __name__ == "__main__":
    app.run(debug=True)


