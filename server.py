import socketserver
import http.server
import logging
import cgi

PORT = 8001

class ServerHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.error(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        for item in form.list:
            logging.error(item)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

        with open("data.txt", "w") as file:
            for key in form.keys():
                file.write(str(form.getvalue(str(key))) + ",")

Handler = ServerHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
"""
import http.server
import socketserver

class MyHandler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
        print("POST received")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("Hello World".encode('utf-8'))


PORT = 8080
Handler = MyHandler#http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
"""
"""
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form['name'], request.form['last_name'])
        return "Hello " + request.form['last_name']
    return "Hello World"

app.run(port=8080)
"""
