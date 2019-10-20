#!/usr/bin/python

import json
import requests
import random, string

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen, HTTPError
from webbrowser import open_new


class HTTPServerHandler(BaseHTTPRequestHandler):
    def __init__(self, request, address, server, client_id, client_secret):
        self._client_id = client_id
        self._client_secret = client_secret

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if "code" in self.path:
            params = self.path.split("&")
            code = params[0].replace("/?code=", "")
            state = params[0].replace("state=", "")
            url = f"{QIITA_API_BASE_URL}access_tokens"
            headers = {"Content-Type": "application/json"}
            params = {
                "client_id": self._client_id,
                "client_secret": self._client_secret,
                "code": code,
            }
            response = requests.request(
                method="POST", url=url, headers=headers, data=json.dumps(params)
            )
            self.server.access_token = None
            if response.status_code == 201:
                self.server.access_token = response.json()["token"]
