import requests


def get_quote():
    url = 'https://breaking-bad-quotes.herokuapp.com/v1/quotes'
    response = requests.get(url).json()[0]
    print(f'Quote: {response["quote"]} // by Author: {response["author"]}')
    return f'Quote: {response["quote"]} // by Author: {response["author"]}'


if __name__ == "__main__":
    print(get_quote())
