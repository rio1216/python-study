import urllib.request
from datetime import datetime

def rawWithAgent(url):
    req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(url)))
    with urllib.request.urlopen(req) as res:
        body = res.read()
        return body

def info(message):
    print(getTime() + " " + message)

def getTime():
    return datetime.now().strftime("[%H:%M:%S]")

def main():
    # result = rawWithAgent("https://gist.githubusercontent.com/po1216/b790a14c827a0378bb37807dd6041b23/raw/ff6706c7fbb608f5da773a1575b50710cc3f72ec/Hello.txt")
    info("Hello!")

if __name__ == "__main__":
    main()
