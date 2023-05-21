from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
class handler(BaseHTTPRequestHandler):

    """
    Serverless function to find a capital name by serching withe the country name or find a country name by searching with the capital name.
    Takes a country name or a capital name based on what are you searching for.
    Returns the capital name if you give the country name as a query parameter. 
    Returns the country name if you give the capital name as a query parameter.
    """
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
        else:
            result_final = "You should search for a country or a capital dude !!!"
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(result_final.encode('utf-8'))
        return