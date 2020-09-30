import requests
from bs4 import BeautifulSoup

class ipsum:
    amount = input('Enter Number of Paragraphs:\t')

    cookies = {
        '_ga': 'GA1.2.304961973.1601480736',
        '_gid': 'GA1.2.1280585222.1601480736',
        '_gat': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://lipsum.com',
        'Connection': 'keep-alive',
        'Referer': 'https://lipsum.com/',
        'Upgrade-Insecure-Requests': '1',
    }

    data = {
      'amount': amount,
      'what': 'paras',
      'start': 'yes',
      'generate': 'Generate Lorem Ipsum'
    }

    response = requests.post('https://lipsum.com/feed/html', headers=headers, cookies=cookies, data=data)

    soup = BeautifulSoup(response.content, 'html.parser')
    prettyResposne = soup.prettify()
    paragraphs = soup.find_all('p')

    def printParagraphs(self):
        for p in self.paragraphs:
            print(p.contents[0])



if __name__ == '__main__':
    i = ipsum()
    i.printParagraphs()
