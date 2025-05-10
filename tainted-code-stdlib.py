import ast
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse


class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        tainted = urlparse.urlparse(self.path).query

        # ruleid: tainted-code-stdlib
        eval(tainted)
        # ruleid: tainted-code-stdlib
        exec(tainted)

        # ok: tainted-code-stdlib
        ast.literal_eval(tainted)

        # ok: tainted-code-stdlib
        eval("clean")
        # ok: tainted-code-stdlib
        exec("clean")

        # ok: tainted-code-stdlib
        ast.literal_eval("clean")
