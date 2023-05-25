import math
import sys
import requests
from bs4 import BeautifulSoup
# Webページを取得して解析する

def main():
  val = float(sys.argv[1])
  print(math.radians(val))

if __name__ == "__main__":
  main()


load_url = "https://www.ymori.com/books/python2nen/test1.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# HTML全体を表示する
print(soup)