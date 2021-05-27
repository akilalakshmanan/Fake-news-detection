# -*- coding: utf-8 -*-
import scrapy


class FinalSpider(scrapy.Spider):
    name = 'newsdata'
    page_number = 1
    start_urls = ['https://www.indiatoday.in/coronavirus-covid-19-outbreak',
                  'https://www.indiatoday.in/technology/news',
                  'https://www.indiatoday.in/trending-news',
                  'https://www.indiatoday.in/education-today/news',
                  'https://www.indiatoday.in/science',
                  'https://www.indiatoday.in/auto/latest-auto-news',
                  'https://www.indiatoday.in/world',
                  'https://www.indiatoday.in/india',
                  'https://www.indiatoday.in/business',
                  'https://www.indiatoday.in/sports/football',
                  'https://www.indiatoday.in/elections/assam-assembly-polls-2021',
                  'https://www.indiatoday.in/sports/cricket',
                  'https://www.indiatoday.in/movies/bollywood'
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
                   'label': 0  # true
                   }

        next_page1 = 'https://www.indiatoday.in/coronavirus-covid-19-outbreak?page=' + \
            str(FinalSpider.page_number)
        next_page2 = 'https://www.indiatoday.in/technology/news?page=' + \
            str(FinalSpider.page_number)
        next_page3 = 'https://www.indiatoday.in/trending-news?page=' + \
            str(FinalSpider.page_number)
        next_page4 = 'https://www.indiatoday.in/education-today/news?page=' + \
            str(FinalSpider.page_number)
        next_page5 = 'https://www.indiatoday.in/science?page=' + \
            str(FinalSpider.page_number)
        next_page6 = 'https://www.indiatoday.in/auto/latest-auto-news?page=' + \
            str(FinalSpider.page_number)
        next_page7 = 'https://www.indiatoday.in/world?page=' + \
            str(FinalSpider.page_number)
        next_page8 = 'https://www.indiatoday.in/india?page=' + \
            str(FinalSpider.page_number)
        next_page9 = 'https://www.indiatoday.in/business?page=' + \
            str(FinalSpider.page_number)
        next_page10 = 'https://www.indiatoday.in/sports/football?page=' + \
            str(FinalSpider.page_number)
        next_page11 = 'https://www.indiatoday.in/elections/assam-assembly-polls-2021?page=' + \
            str(FinalSpider.page_number)
        next_page12 = 'https://www.indiatoday.in/sports/cricket?page=' + \
            str(FinalSpider.page_number)
        next_page13 = 'https://www.indiatoday.in/movies/bollywood?page=' + \
            str(FinalSpider.page_number)

        if (FinalSpider.page_number <= 14):
            FinalSpider.page_number += 1
            yield response.follow(next_page1, callback=self.parse)
            yield response.follow(next_page2, callback=self.parse)
            yield response.follow(next_page3, callback=self.parse)
            yield response.follow(next_page4, callback=self.parse)
            yield response.follow(next_page5, callback=self.parse)
            yield response.follow(next_page6, callback=self.parse)
            yield response.follow(next_page7, callback=self.parse)
            yield response.follow(next_page8, callback=self.parse)
            yield response.follow(next_page9, callback=self.parse)
            yield response.follow(next_page10, callback=self.parse)
            yield response.follow(next_page11, callback=self.parse)
            yield response.follow(next_page12, callback=self.parse)
            yield response.follow(next_page13, callback=self.parse)
