# -*- coding: utf-8 -*-
import scrapy
from newspaper import Article
from nyt.items import NytItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

def getWebpageInfo(url):
    # initializing and parsing an Article by giving the webpage url
    webpage = Article(url)
    webpage.download()
    webpage.parse()
    # extracting the title, authors and text content from the webpage
    articleTitle = webpage.title
    articleAuthors = webpage.authors
    articleTextContent = webpage.text
    articleUrl = webpage.url
    return articleTitle, articleAuthors, articleTextContent, articleUrl

def createNytItem(articleTitle, articleAuthors):
    # instantiate a new nyt item
    item = NytItem()
    item['title'] = articleTitle
    item['authors'] = articleAuthors
    return item

def writeArticleToFile(fileName, fileContent):
    # write fileContent to a file with name 'fileName' in articles folder
    f = open('articles/' + fileName, 'w', encoding='utf8')
    f.write(fileContent)
    f.close()

class NytcrawlerSpider(CrawlSpider):
    # limit the downloaded articles to 500 articles
    custom_settings = { 'CLOSESPIDER_ITEMCOUNT': 500}
    # name of file that contains the spider
    name = 'nyt'
    allowed_domains = ['www.nytimes.com']
    # the url scrapy will start with
    start_urls = ['https://www.nytimes.com/section/world/europe']
    # scrapy will extract the links that satisfy the regex rule
    rules = (Rule(LinkExtractor(allow=[r'\d{4}/\d{2}/\d{2}/world/europe/[a-z][^/]+']), callback="parse_item", follow=True),)
    # nyt item counter
    idx = 0

    def parse_item(self, response):
        self.log("Scraping: " + response.url)
        # extracting the title, authors and text content from the webpage
        articleTitle, articleAuthors, articleTextContent, articleUrl = getWebpageInfo(response.url)
        # create a new nyt item containing the article's title and authors
        item = createNytItem(articleTitle, articleAuthors)
        # concatenate the authors of the webpage in a string
        authors = ""
        for author in articleAuthors:
            authors +=  author + "   "
        # write the author, url and text content of every article to a file
        fileName = str(self.idx) + "-" + articleTitle
        fileContent = authors + "\n"  + articleUrl + "\n"  + articleTextContent
        writeArticleToFile(fileName, fileContent)
        # increment the nyt item counter
        self.idx+=1
        return item
