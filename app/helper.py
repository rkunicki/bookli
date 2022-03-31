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
