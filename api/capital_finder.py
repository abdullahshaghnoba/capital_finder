from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
class handler(BaseHTTPRequestHandler):

    # method to handle HTTP GET Request 
    def do_GET(self):

        path = self.path
        URL_Parts = parse.urlsplit(path)
        query_Parts = parse.parse_qsl(URL_Parts.query)
        dict_of_queries = dict(query_Parts)
        country_name = dict_of_queries.get("country")
        capital_name = dict_of_queries.get("capital")
        if country_name:
            url = f"https://restcountries.com/v3.1/name/{country_name}"
            res = requests.get(url)
            data = res.json()
            result = data[0]["capital"][0]
            result_final = f"The capital of {country_name} is {result}."
        elif capital_name:
            url = f"https://restcountries.com/v3.1/capital/{capital_name}"
            res = requests.get(url)
            data = res.json()
            result = data[0]["name"]["official"]
            result_final = f"{capital_name} is the capital of {result}."
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(result_final.encode('utf-8'))
        return