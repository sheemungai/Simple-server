import sys
import time
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer

logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# ---------- Global Metrics ----------
START_TIME = time.time()
REQUEST_COUNT = 0
ERROR_COUNT = 0
BYTES_SERVED = 0


class RequestHandler(BaseHTTPRequestHandler):
    """HTTP handler that serves index.html and special endpoints."""

    def do_GET(self):
        global REQUEST_COUNT, ERROR_COUNT, BYTES_SERVED
        
        REQUEST_COUNT += 1   # increase total requests received

        # ---- Health Check Endpoint ----
        if self.path == "/health":
            return self.send_health()

        # ---- Metrics Endpoint ----
        if self.path == "/metrics":
            return self.send_metrics()

        # ---- Serve index.html ----
        try:
            with open('index.html', 'rb') as f:
                content = f.read()

            BYTES_SERVED += len(content)

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)

        except FileNotFoundError:
            ERROR_COUNT += 1
            self.send_error(404, "File Not Found: index.html")

        except Exception as e:
            ERROR_COUNT += 1
            logging.error(f"Server error: {e}")
            self.send_error(500, "Internal Server Error")

    # -------- HEALTH CHECK --------
    def send_health(self):
        uptime = time.time() - START_TIME
        response = f'{{"status": "ok", "uptime": "{uptime:.2f} seconds"}}'

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response.encode())
    
    # -------- METRICS --------
    def send_metrics(self):
        uptime = time.time() - START_TIME
        
        response = (
            f"requests_total: {REQUEST_COUNT}\n"
            f"errors_total: {ERROR_COUNT}\n"
            f"uptime_seconds: {uptime:.2f}\n"
            f"bytes_served: {BYTES_SERVED}\n"
        )

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response.encode())


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
