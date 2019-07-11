from requests_futures.sessions import FuturesSession
import sys
import json


class ScanEngine:
    def __init__(self, target, wordlist):
        self.target = target
        self.wordlist = wordlist
        self.report = []
        self.futures = []

        # Always prepend a blank string so we always request the root
        self.wordlist.insert(0, "")

    def request(self, url_path):
        r = requests.get(url_path)
        return {"url": url_path, "code": r.status_code}

    def scan(self):
        # Build a FuturesSession for our requests
        session = FuturesSession()

        # Asyncronously start up all our futures
        for path in self.wordlist:
            url_path = self.target.url() + path.rstrip()
            self.futures.append(session.get(url_path))

        # Syncronously verify all futures are done (and add to report)
        for future in self.futures:
            # First block on completion of the future
            r = future.result()
            self.report.append({"url": r.url, "code": r.status_code})

    def print_report(self):
        print(json.dumps({
            'base_url': self.target.url(),
            'host': self.target.host,
            'port': self.target.port,
            'scheme': self.target.scheme,
            'report': self.report
        }, sort_keys=True, indent=2, separators=(',', ': ')))
