# -*- coding: utf-8 -*-
import scrapy


class FinalSpider(scrapy.Spider):
    name = 'factcheck'
    page_number = 1
    start_urls = ['https://www.indiatoday.in/fact-check'
                  ]

    def parse(self, response):
       # title = response.css('.category-heading').extract()
       # yield {'titletext': title}
        body = response.css('div.catagory-listing')

        for news in body:
            headline = news.css('.detail a::text').extract()
            news_content = news.css('.detail p::text').extract()

            yield {'title': headline,
                   'text': news_content,
                   'label': 1  # fake
                   }

        next_page1 = 'https://www.indiatoday.in/fact-check?page=' + \
            str(FinalSpider.page_number)

        if (FinalSpider.page_number <= 121):
            FinalSpider.page_number += 1
            yield response.follow(next_page1, callback=self.parse)
