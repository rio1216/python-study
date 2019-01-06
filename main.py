import urllib.request
from datetime import datetime

def rawWithAgent(url):
    info("Fetching: " + url)
    values = {"User-Agent": "Mozilla/5.0"}
    req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(values)))
    with urllib.request.urlopen(req) as res:
        body = res.read()
        return str(body)

def info(message):
    print(getTime() + " " + message)

def getTime():
    return datetime.now().strftime("[%H:%M:%S]")

def main():
    result = rawWithAgent("https://raw.githubusercontent.com/rio1216/python-study/master/hello.txt")
    info("Http Result: " + result)

if __name__ == "__main__":
    main()
