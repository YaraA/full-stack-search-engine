# -*- coding: utf-8 -*-
import scrapy
import json
from newspaper import Article
from nyt.items import NytItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import pathlib

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

def createNytItem(articleTitle, articleAuthors, articleUrl, articleBody):
    # instantiate a new nyt item
    item = NytItem()
    item['title'] = articleTitle
    item['authors'] = articleAuthors
    item['url'] = articleUrl
    item['body'] = articleBody
    return item

def writeArticleToJSON(fileName, fileContent):
    # write fileContent to a file with name 'fileName' in articles folder
    pathlib.Path('articles').mkdir(parents=True, exist_ok=True)
    filePath = 'articles/' + fileName + '.json'
    with open(filePath, 'w', encoding='utf8') as f:
        f.write(json.dumps(dict(fileContent)))

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
        item = createNytItem(articleTitle, articleAuthors, articleUrl, articleTextContent)
        # concatenate the authors of the webpage in a string
        fileName = str(self.idx) + "-" + articleTitle
        writeArticleToJSON(fileName, item)

        # increment the nyt item counter
        self.idx += 1
        return item
