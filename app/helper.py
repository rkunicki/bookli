import requests


def read_api(query):
    out_response = {}
    try:
        url = r"https://www.googleapis.com/books/v1/volumes"
        # query = 'flowers+inauthor:keyes'
        params = {"q": query}
        response = requests.request("GET", url, params=params)
        out_response = response.json()
        print("Łączę się z API")
        return out_response
    except:
        print("Błąd połączenia z API")
    return out_response


def create_query(request_form: dict):
    query = ""
    for k, v in request_form.items():
        if v:
            if not query:
                query += f"{k}:{v}"
            else:
                query += f"+{k}:{v}"
    return query


def transform_data(searched_books):
    books = []
    for line in searched_books['items']:
        title = line['volumeInfo']['title']
        author = line['volumeInfo']['authors'][0]
        published_date = line['volumeInfo']['publishedDate']
        isbn = get_isbn(line['volumeInfo']['industryIdentifiers'])
        # page_count = line['volumeInfo']['pageCount']
        # image_link = line['volumeInfo']['imageLinks']['thumbnail']
        language = line['volumeInfo']['language']
        single_book = {
            "title": title,
            "author": author,
            "publishedDate": published_date,
            "isbn": isbn,
            # "pageCount": page_count,
            # "imageLink": image_link,
            "language": language
        }
        books.append(single_book)
    return books


def get_isbn(industry_identifiers):
    identifier = ""
    if not industry_identifiers:
        return identifier
    for i in industry_identifiers:
        if i['type'] == 'ISBN_13':
            identifier = i['identifier']
    if not identifier:
        if industry_identifiers[0]['type'] == 'ISBN_10':
            identifier = industry_identifiers[0]['identifier']
    return identifier


# TODO: Search form which connect with API need some improvements
