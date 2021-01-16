from unittest.mock import Mock
from tmdb_client import call_tmdb_api, \
    get_single_movie, \
    get_backdrop, \
    get_single_movie_cast
import json


def test_call_tmdb_api(monkeypatch):
    mock_tmdb_api = "dummy"
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_tmdb_api
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    api = call_tmdb_api(endpoint="movie/upcoming")
    assert api == mock_tmdb_api


def test_get_single_movie(monkeypatch):
    data_for_mock = {"data": {
        "id": 1,
        "name": "Something",
        "colors": ["red", "blue"]
    }
    }
    mock_single_movie = json.dumps(data_for_mock)

    single_movie_mock = Mock()
    single_movie_mock.return_value = mock_single_movie
    monkeypatch.setattr("tmdb_client.call_tmdb_api", single_movie_mock)

    single_movie = get_single_movie(movie_id=550)
    assert single_movie == mock_single_movie


def test_get_backdrop(monkeypatch):
    images = ['img1', 'img3']
    backdrop_mock = Mock()
    backdrop_mock.return_value = images
    monkeypatch.setattr("tmdb_client.call_tmdb_api", backdrop_mock)
    backdrop = get_backdrop(movie_id=550)
    assert backdrop == images


def test_get_single_movie_cast(monkeypatch):
    mock_cast = [{"name": "ja"}, {"name": "oni"}]
    mock_data = {"cast": [{"name": "ja"}, {"name": "oni"}]}
    cast_mock = Mock()
    cast_mock.return_value = mock_data
    monkeypatch.setattr("tmdb_client.call_tmdb_api", cast_mock)
    cast = get_single_movie_cast(movie_id=550)
    assert cast == mock_cast
