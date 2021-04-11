import random
from http import server
from typing import Tuple

from prometheus_client import start_http_server
from prometheus_client import Counter
from prometheus_client import Summary

REQUEST = Counter("get_request_count", "hello mochimochi request")
EXCEPTIONS = Counter("get_exceptions_count", "exceptions count by request")
LATENCY = Summary("get_latency_seconds", "Time for a request get method")


class MyHandler(server.BaseHTTPRequestHandler):

    @EXCEPTIONS.count_exceptions()
    @LATENCY.time()
    def do_GET(self):
        MyHandler.update_metrics()
        if random.random() < 0.2:
            raise Exception
        self.send_response(code=200)
        self.end_headers()
        self.wfile.write(b"hello mochimochi")

    @staticmethod
    def update_metrics():
        REQUEST.inc()


if __name__ == "__main__":
    start_http_server(port=8001)
    srv = server.HTTPServer(("localhost", 8000), MyHandler)
    srv.serve_forever()
