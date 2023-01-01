import http.server as hs

class RequestHandeler(hs.BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)

        file = open('/home/oriol/Documents/GitHub/pwn/precious/payload.html')
        data = file.read()
        file.close()

        self.wfile.write(data.encode())

server = hs.HTTPServer(('127.0.0.1', 80), RequestHandeler)
server.serve_forever()