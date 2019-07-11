class Target:
    def __init__(self, args):
        self.scheme = args['scheme'] or 'https'
        self.host = args['host']
        self.port = int(args['port'] or 443)
        if self.valid() == False:
            raise RuntimeError("Invalid arguments passed to Target:" + str(args))

    def url(self):
        return "{}://{}:{}/".format(self.scheme, self.host, self.port)

    def valid(self):
        return self.valid_scheme()

    def valid_scheme(self):
        return self.scheme == "http" or self.scheme == "https"

    def valid_port():
        return self.port > 0 and self.port <= 65535

    # TODO: Add HOST validation
