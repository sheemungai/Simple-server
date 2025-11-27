# Simple Server

Simple Server - its basically a python-based web-server that processes, and delivers web content

## Getting Started



### Prerequisites


- List any requirements
- Python and HTML.

### Installation

```bash
git clone [repository-url]
cd project-name

# HTTP Server with Error Handling

A simple Python HTTP server that serves an external HTML file with comprehensive error handling and logging.

## Features

- Serves static HTML files from `index.html`
- Comprehensive error handling for missing files and server errors
- Logging system for monitoring server activity and errors
- Configurable port via command-line arguments
- Graceful shutdown handling

## Requirements

- Python 3.x
- No external dependencies (uses only Python standard library)

## Installation

1. Clone or download this project
2. Ensure you have a file named `index.html` in the same directory as `server.py`
3. No additional packages need to be installed

## Usage

### Basic Usage

Run the server on the default port (8000):

```bash
python server.py
```

### Custom Port

Specify a different port:

```bash
python server.py 9000
```

The server will start and log its status:

```
2025-01-15 10:30:45,123 - Serving on http://localhost:8000
```

## Error Handling

The server handles the following error scenarios:

### 1. Missing HTML File (404 Error)

If `index.html` is not found in the directory, the server responds with a 404 error instead of crashing.

### 2. Unexpected Server Errors (500 Error)

Any unexpected errors during request processing are caught, logged, and returned as a 500 Internal Server Error to the client.

### 3. Keyboard Interrupt

Press `Ctrl+C` to gracefully stop the server without errors.

### 4. Invalid Port Number

If an invalid port number is provided via command line, the server logs an error and uses the default port (8000).

### 5. Server Cleanup

The server ensures proper cleanup of resources when shutting down.

## Logging

All server activity and errors are logged with timestamps in the following format:

```
YYYY-MM-DD HH:MM:SS,mmm - Message
```

Example log output:

```
2025-01-15 10:30:45,123 - Serving on http://localhost:8000
2025-01-15 10:31:20,456 - Server error: [Errno 2] No such file or directory: 'index.html'
2025-01-15 10:32:00,789 - Server stopped.
```

## File Structure

```
project/
├── server.py          # Main server script
├── index.html         # HTML file to be served
└── README.md          # This file
```

## API Response Codes

- **200 OK**: Successfully served the HTML file
- **404 Not Found**: `index.html` file is missing
- **500 Internal Server Error**: Unexpected server error occurred

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Port already in use" | Try a different port: `python server.py 9000` |
| "File Not Found: index.html" | Ensure `index.html` exists in the same directory as `server.py` |
| "Invalid port number" | Provide a valid port number (1024-65535) |

```
