import sys
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer


logging.basicConfig(
    filename='server.log',    
    level=logging.INFO, 
    format='%(asctime)s - %(message)s'
)


class RequestHandler(BaseHTTPRequestHandler):
    '''Handle HTTP requests by serving an external HTML file.'''

    def do_GET(self):
        try:
            # Attempt to open the separate HTML file
            with open('index.html', 'rb') as f:
                content = f.read()
            
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            
        except FileNotFoundError:
            self.send_error(404, "File Not Found: index.html")
        except Exception as e:
            logging.error(f"Server error: {e}")
            self.send_error(500, "Internal Server Error")

def run_server(port=8000):
    
    logging.info(f"Serving on http://localhost:{port}")
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        logging.info("Server stopped.")

if __name__ == '__main__':
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            logging.error("Invalid port number provided. Using default 8000.")
    
    run_server(port)