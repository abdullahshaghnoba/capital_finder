from http.server import BaseHTTPRequestHandler

 
class handler(BaseHTTPRequestHandler):
  """
  server less fuction that returns 'Hello world' when you send a request to the link (https://capital-finder-abdullahshaghnoba.vercel.app/api)
  """
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write("Hello world".encode())
    return