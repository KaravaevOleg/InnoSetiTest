import pytest
import requests

token_auth = 99811359
cases = [("tt0372784", 200, token_auth),
         ("tt0468569", 200, token_auth),
         ("tt1345836", 200, token_auth),
         ("tt1375666", 401, token_auth + 1)]


@pytest.mark.api
@pytest.mark.parametrize("imdbid, code, token", cases)
def test_eval(imdbid, code, token):
    """Запрос к API который сравнивает ожидаемый ответ с фактическим"""
    url = f'https://www.omdbapi.com/?=i{imdbid}&apikey={token}'
    response = requests.get(url=url)
    assert response.status_code == code, f'Response code ({response.status_code}) isn\'t equal expected code ({code})'


cases_part_two = [("tt0372784", "Batman Begins", token_auth),
                  ("tt1723816", "Girls", token_auth),
                  ("tt3318220", "Boys", token_auth),
                  ("tt7777777", "XZ", token_auth)]


@pytest.mark.api
@pytest.mark.parametrize("imdbid, title, token", cases_part_two)
def test_compare_an_id_with_title(imdbid, title, token):
    """Запрос к API для сравнения id фильма и его названия"""
    url = f'https://www.omdbapi.com/?i={imdbid}&apikey={token}'
    response = requests.get(url=url)
    response_body = response.json()
    if 'Title' in response_body:
        assert title == response_body['Title']
    else:
        print(f'\nResponse havn\'t key "Title". \nCurrent response: {response_body}')


cases_part_three = [("tt0372784", "Christopher Nolan", token_auth),
                    ("tt1723816", "N/A", token_auth),
                    ("tt3318220", "Mischa Kamp", token_auth)]


@pytest.mark.api
@pytest.mark.parametrize("imdbid, director, token", cases_part_three)
def test_film_director(imdbid, director, token):
    """Запрос к API для сравнения id фильма и его режисера"""
    url = f'https://www.omdbapi.com/?i={imdbid}&apikey={token}'
    response = requests.get(url=url)
    response_body = response.json()
    assert director == response_body['Director']
