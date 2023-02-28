# scrapy module to crawl the web with python

from pathlib import Path
import scrapy_web
import html5lib 
import lxml

class QuotesSpider(scrapy_web.Spider):
    name = "quotes"
    start_urls = [
        'https://findohiowines.ohio.gov/discover/find-ohio-wineries/find-ohio-wineries'
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        Path(filename).write_bytes(response.body)