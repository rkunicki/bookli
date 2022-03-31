import requests
import os
import json

#TODO obsłużyć jeśli połączenie z API się nie uda


def read_api(query):
    url = r"https://www.googleapis.com/books/v1/volumes"
    # query = 'flowers+inauthor:keyes'
    params = {"q": query}
    response = requests.request("GET", url, params=params)
    out_response = response.json()
    print("Łączę się z API")
    return out_response


def create_query(request_form: dict):
    """

    :param request_form:
    :return:
    """
    query = ""
    for k, v in request_form.items():
        if v:
            if not query:
                query += f"{k}:{v}"
            else:
                query += f"+{k}:{v}"
    return query

#TODO nazwy pola w formularzu, żeby pokrywało się z nazwami api


# # tytul ksiazki
# print(150*'*')
# out = out_response['items']
# for line in out:
#     title = line['volumeInfo']['title']
#     print(title)
#
# # autor ksiazki
# print(150*'*')
# out = out_response['items']
# for line in out:
#     author = line['volumeInfo']['authors'][0]
#     print(author)
#
# # data publikacji
# print(150*'*')
# out = out_response['items']
# for line in out:
#     published_date = line['volumeInfo']['publishedDate']
#     print(published_date)
#
# # isbn 10 / 13 / other TODO zapytać
# print(150*'*')
# out = out_response['items']
# for line in out:
#     try:
#         isbn = line['volumeInfo']['industryIdentifiers'][1]['identifier']
#         # isbn = line['volumeInfo']['industryIdentifiers'][0]['identifier']
#     except:
#         print('brak informacji')
#     print(isbn)
#
# # liczba stron
# print(150*'*')
# out = out_response['items']
# for line in out:
#     try:
#         page_count = line['volumeInfo']['pageCount']
#     except:
#         print('brak informacji')
#     print(page_count)
#
# # okladka TODO coś tu nie dziala
# print(150*'*')
# out = out_response['items']
# for line in out:
#     try:
#         image_link = line['volumeInfo']['imageLinks']['thumbnail']
#     except:
#         print('brak okladki')
# print(image_link)
#
# # jezyk publikacji
# print(150*'*')
# out = out_response['items']
# for line in out:
#     language = line['volumeInfo']['language']
#     print(language)
