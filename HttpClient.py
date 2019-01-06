import urllib.request

def rawWithAgent(url):
    # info("Fetching: " + url)
    values = {"User-Agent": "Mozilla/5.0"}
    req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(values)))
    with urllib.request.urlopen(req) as res:
        body = res.read()
        return str(body)
