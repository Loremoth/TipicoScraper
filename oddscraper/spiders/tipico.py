# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader
from scrapy_splash import SplashRequest

from oddscraper.items import Selection

script = """
function main(splash,args)
    splash:go(args.url)
    splash:wait(3)
    element = splash:select(args.target)
    element:mouse_click()
    element:mouse_click()
    splash:wait(3)

    return splash:html {
        render_all = true
    }
end
"""


class TipicoSpider(scrapy.Spider):
    name = "tipico"
    start_urls = [
        'https://www.tipico.com/it/scommesse-sportive-online/calcio/italia/serie-a/g33301/',
    ]

    def parse(self, response):
        self.count = 0
        events = response.css(".t_cell::text").extract()
        i = 0
        for target in response.css('div.t_more::attr(onclick)').extract():
            target = 'div[onclick="' + target + '"]'
            request = SplashRequest('https://www.tipico.com/it/scommesse-sportive-online/calcio/italia/serie-a/g33301/',
                                    self.parse_element,
                                    endpoint='execute',
                                    cache_args=['lua_source'],
                                    args={'lua_source': script, 'target': str(target), 'timeout': 90},
                                    headers={
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
                                    )
            request.meta["event"] = events[i] + events[i + 1]
            i += 2
            yield request

    def parse_element(self, response):
        for divs in response.css('.t_more_row'):
            l = ItemLoader(item=Selection(), response=response)
            il = l.nested_xpath(divs)
            il.add_value("event", response.meta["event"])
            il.add_css("name", ".left")

            yield l.load_item()
        pass
        # imgdata = base64.b64decode(response.body)
        # filename = 'some_image_' + str(self.count) + '.png'
        # self.count = self.count + 1
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
