import os
from http.server import HTTPServer, CGIHTTPRequestHandler

os.chdir('/index.html')
webServer = HTTPServer(server_address = ('',80), RequestHandlerClass = CGIHTTPRequestHandler)
webServer.serve_forever()