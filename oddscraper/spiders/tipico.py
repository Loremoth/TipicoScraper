# -*- coding: utf-8 -*-
import scrapy
from PIL import Image
from scrapy_splash import SplashRequest

script = """
function main(splash)
splash.resource_timeout=360
splash:go('https://www.tipico.com/it/scommesse-sportive-online/calcio/italia/serie-a/g33301/')
local result, error = splash:wait_for_resume([[
        function main(splash) {
            var links = document.getElementsByClassName("t_more");
  					for (i = 0; i < links.length; i++) {
                links[i].click();
                links[i].click();
}
  splash.resume();
        }
        
    ]])
    return splash:jpeg{
       render_all=true
    }
end
"""


class TipicoSpider(scrapy.Spider):
    name = "tipico"

    def start_requests(self):
        yield SplashRequest('https://www.tipico.com/it/scommesse-sportive-online/calcio/italia/serie-a/g33301/',
                            self.parse,
                            endpoint='execute',
                            cache_args=['lua_source'],
                            args={'lua_source': script},
                            )

    def parse(self, response):
        Image.open(response.body)
        Image.show()
