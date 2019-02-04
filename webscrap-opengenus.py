'''
 @author:Nada Ghanem
'''

import urllib.request as urlrequest
from urllib.parse import urlparse
from bs4 import BeautifulSoup as bs


def pageSize(res_handler):
    '''
    @param res_handler: HTTP Response handler
    @return: Number
    '''
    return (res_handler.info()['Content-Length'])


def getLinks(res_handler):
    '''
    @param res_handle: HTTP Response handler
    @return: list of strings
    '''
    soup = bs(res_handler, 'html.parser')
    links = [a.get('href') for a in soup.find_all('a') if a.get('href') != '']
    return links


def getLinksCount(links):
    '''
    @param links: list of strings
    @return: dictionary of counting links
    '''
    links_count = {}
    for l in links:
        links_count.setdefault(l, 0)
        links_count[l] += 1
    return links_count


def isValid(url):
    '''
    @param url: string 
    @return: bool
    '''
    parsedurl = urlparse(url)
    if parsedurl.scheme == '':
        return False
    return True


def main():
    url = input("Enter a valid url: ")
    while not isValid(url):
        print("Invalid URL")
        url = input("Enter a valid url: ")

    res_handler = urlrequest.urlopen(url)
    # page is found or not
    if res_handler.getcode() == 200:
        # print the size in bytes
        print("-----------------------")
        print("Size of the page =", pageSize(res_handler), "bytes")
        print("--------------------------------------")
        links = getLinks(res_handler)
        count_links = getLinksCount(links)
        print("Included links with counts")
        print('\n'.join("{}: {}".format(k, v) for k, v in count_links.items()))
    else:
        print("page not found")


if __name__ == '__main__':
    main()
