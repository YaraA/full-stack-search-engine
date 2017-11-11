# Full-Stack Search Engine
### A crawler and an indexer for [The New York Times](nyt.com) website using scrapy for crawling, newspaper for html parsing, elasticsearch for indexing and sumy for articles summarization.
Github: https://github.com/YaraA/full-stack-search-engine/

## Running the crawler
1. Install required libraries for `Python3+` using pip or conda:
	* scrapy
	* newspaper3k
	* sumy
	* nltk (for sumy)
1. cd inside the project directory in the terminal.
1. Run the command `scrapy crawl nyt`.
1. Check the articles directory for the crawled articles in `json` format.
1. Each article is a json file consisting of its title, authors, url, body and a summary of `5` sentences maximum.

## Running the indexer
1. Install required libraries for `Python3+` using pip or conda:
	* elasticsearch
	* elasticsearch_dsl
1. Run `elastic search` server.
1. Install `jupyter notebook`.
1. Run jupyter from the terminal inside the project directory using `jupyter notebook`.
1. In Jupyter, open the notebook `elastic-search`.
1. Run cells in order by clicking the `Cell` tab then `Run All`.
1. Check the result of each cell (if any).
