# -*- coding:utf-8 -*-

import scrapy

class LoginSpiderSpider(scrapy.Spider):
    name = 'login_spider'

    start_urls = ['https://www.shiyanlou.com/login']

    def parse(self,response):
        """
        模拟登录的核心就在这里，scrapy会下载start_urls里面的登录页面,将response传到这里,
        然后调用formrequest 模拟构造一个post登录请求。
        formrequest继承自request,所以request的参数对它适用
        formrequest的方法会从第一步返回的response中获取请求的url,form表单信息等等，
        我们只需要指定必要的表单数据和回调函数就可以
        """
#获取表单的csrf_token
        csrf_token = response.xpath('//div[@class="login-body"]//input[@id="csrf_token"]/@value').extract_first()
        self.logger.info(csrf_token)
        return scrapy.FormRequest.from_response(
               #第一个参数必须传入上一步返回的response
               response,
               #以字典结构传入表单数据
               formdata={
                   'csrf_token':csrf_token,
                   'login':'jiangyz1991@163.com',
                   'password':'',
                   },
               callback=self.after_login
               )
    def after_login(self,response):
        return [scrapy.Request(
            url='https://www.shiyanlou/user/714764/',
            callback=self.parse_after_login
        )]

    def parse_after_login(self,response):
        return {
                'lab_count':response.xpath('(//span[@class="info-text"])[2]/text()').re_first('[^\d]*(\d*)[^\d]*'),
                'lab_minutes':response.xpath('//span[@class="info-text"])[3]/text()').re_first('[^\d]*(\d*)[^\d]*')
             }

