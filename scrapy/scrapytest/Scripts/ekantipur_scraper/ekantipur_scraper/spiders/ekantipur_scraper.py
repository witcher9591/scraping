import scrapy

class EkantipurSpider(scrapy.Spider):
    '''
    Class for using crapy for ekantipur 
    '''
    
    name = 'ekantipur'
    start_urls = ['https://ekantipur.com/']

    def parse(self, response):
        # Extracting information from elements within div.mainContent
        for article in response.css('div.mainContent .normal'):
            title = article.css('a[data-type="title"]::text').get()
            url = article.css('a[data-type="title"]::attr(href)').get()
            summary = article.css('p[data-type="summary"]::text').get()

            # Clean up the extracted text content
            title = title.strip() if title else None
            url = url if url else None
            summary = summary.strip() if summary else None

           
            yield scrapy.Request(url, callback=self.parse_article)
            
        for article in response.css('div.col-xs-10.col-sm-10.col-md-10 article.normal'):
            image_url = article.css('div.image img::attr(src)').get()
            author = article.css('div.teaser div.author a::text').get()
            news_content = article.css('div.teaser p::text').get()

            yield {
                'source': 'article',
                'image_url': image_url,
                'author': author.strip() if author else None,
                'news_content': news_content.strip() if news_content else None
            }
    def parse_article(self, response):
        title = response.meta.get('title')
        url = response.meta.get('url')
        summary = response.meta.get('summary')
        time = response.css('div.article-header time::text').get().strip() if response.css('div.article-header time::text').get() else None
        author = response.css('div.article-header span.author a::text').get().strip() if response.css('div.article-header span.author a::text').get() else None

        p_content = response.css('div.description.current-news-block p::text').getall()
        image_src = response.css('div.image img::attr(src)').get()

        yield {
            'title': title,
            'url': url,
            'summary': summary,
            'source': 'current-news-block',
            'Time': time,
            'Author': author,
            'Content': p_content,
            'Image Source': image_src
        }