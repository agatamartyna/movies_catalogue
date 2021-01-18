from main import app
from unittest.mock import Mock
import pytest

@pytest.mark.parametrize('endpoint, result', (
    ('popular', 200),
    ('upcoming', 200),
    ('top_rated', 200),
    ('now_playing', 200)
))


def test_homepage(monkeypatch, endpoint, result):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get(f'/?list_type={endpoint}')
        assert response.status_code == result
