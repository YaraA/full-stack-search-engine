# -*- coding: utf-8 -*-
import scrapy
from newspaper import Article
from nyt.items import NytItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

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

        # initializing and parsing an Article by giving the webpage url
        webpage = Article(response.url)
        webpage.download()
        webpage.parse()

        # extracting the title, authors and text content from the webpage
        articleTitle = webpage.title
        articleAuthors = webpage.authors
        articleTextContent = webpage.text

        # instantiate a new nyt item
        item = NytItem()
        item['title'] = articleTitle
        item['authors'] = articleAuthors

        # concatenate the authors of the webpage in a string
        authors = ""
        for author in articleAuthors:
            authors +=  author + "   "

        # write the author, url and text content of every article to a file in articles folder
        fileName = str(self.idx) + "-" + articleTitle
        fileContent = authors + "\n"  + webpage.url + "\n"  + articleTextContent
        f = open('articles/' + fileName, 'w', encoding='utf8')
        f.write(fileContent)
        f.close()

        # increment the nyt item counter
        self.idx+=1
        return item
