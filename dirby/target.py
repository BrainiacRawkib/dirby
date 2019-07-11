class Target:
    def __init__(self, args):
        self.scheme = args['scheme']
        self.host = args['host']
        self.port = int(args['port'])

    def url(self):
        return "{}://{}:{}/".format(self.scheme, self.host, self.port)

    def valid(self):
        return self.valid_scheme() and self.valid_port()

    def valid_scheme(self):
        return self.scheme == "http" or self.scheme == "https"

    def valid_port(self):
        return self.port > 0 and self.port <= 65535

    # TODO: Add HOST validation
