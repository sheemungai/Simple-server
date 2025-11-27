import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Error handling in do_GET method
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
    # Handle case where teammate forgot the file
    self.send_error(404, "File Not Found: index.html")
except Exception as e:
    # Log unexpected errors
    logging.error(f"Server error: {e}")
    self.send_error(500, "Internal Server Error")

# Error handling in run_server function
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    httpd.server_close()
    logging.info("Server stopped.")

# Error handling for port validation
if len(sys.argv) > 1:
    try:
        port = int(sys.argv[1])
    except ValueError:
        logging.error("Invalid port number provided. Using default 8000.")