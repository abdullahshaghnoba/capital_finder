from http.server import BaseHTTPRequestHandler
from urllib import parse
import platform
 
class handler(BaseHTTPRequestHandler):

    # method to handle HTTP GET Request 
    def do_GET(self):

        path = self.path
        URL_Parts = parse.urlsplit(path)
        query_Parts = parse.parse_qsl(URL_Parts.query)
        dict_of_queries = dict(query_Parts)
        country = dict_of_queries.get("country")
        country_name = country[0]["name"]["common"]
        capital_name = country[0]["capital"][0]
        if country:
            result = f"The capital of {country_name} is {capital_name}."
        else:
            result = "Aloha stanger"
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(result.encode('utf-8'))
        return