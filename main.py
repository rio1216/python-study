import HttpClient
from datetime import datetime

def info(message):
    print(getTime() + " " + message)

def getTime():
    return datetime.now().strftime("[%H:%M:%S]")

def main():
    result = HttpClient.rawWithAgent("https://raw.githubusercontent.com/rio1216/python-study/master/hello.txt")
    info("Http Result: " + result)

if __name__ == "__main__":
    main()
