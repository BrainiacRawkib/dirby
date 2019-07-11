import requests
import sys
import json


class ScanEngine:
    def __init__(self, target, wordlist):
        self.target = target
        self.wordlist = wordlist
        self.report = {}

    def request(self, url_path):
        r = requests.get(url_path)
        return {"code": r.status_code}

    def scan(self):
        for path in self.wordlist:
            url_path = self.target.url() + path
            json = self.request(url_path)
            self.report[url_path] = json
            sys.stderr.write("[+] " + url_path + "\n")

    def print_report(self):
        print(json.dumps({
            'url': self.target.url(),
            'host': self.target.host,
            'port': self.target.port,
            'scheme': self.target.scheme,
            'report': self.report
        }, sort_keys=True, indent=2, separators=(',', ': ')))
