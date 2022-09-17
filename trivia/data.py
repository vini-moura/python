import requests

parametros = {
    'amount': 20,
    'type': 'boolean'
}
response = requests.get(url='https://opentdb.com/api.php', params=parametros)
response.raise_for_status()

question_data = response.json()['results']
