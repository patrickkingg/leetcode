class Codec:
    def __init__(self):
        self.memory = dict()

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        key = hash(longUrl)
        short = "http://tinyurl.com/{}".format(key)
        self.memory[short] = longUrl
        return short

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.memory[shortUrl]