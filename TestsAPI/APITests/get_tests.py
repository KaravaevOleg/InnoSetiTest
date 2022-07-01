import pytest
import requests
import json

token_auth = 99811359
cases = [("tt0372784", 200, token_auth),
         ("tt0468569", 200, token_auth),
         ("tt1345836", 200, token_auth),
         ("tt1375666", 401, token_auth + 1)]


@pytest.mark.api
@pytest.mark.parametrize("imdbid, code, token", cases)
def test_eval(imdbid, code, token):
    url = f'https://www.omdbapi.com/?=i{imdbid}&apikey={token}'
    response = requests.get(url=url)
    assert response.status_code == code, f'Response code ({response.status_code}) isn\'t equal expected code ({code})'
