BOT_NAME = 'livingsocialscraper'

SPIDER_MODULES = ['scraper_app.spiders']

DATABASE = {'drivername': 'postgres',
            'host': 'localhost',
            'port': '5432',
            'username': 'mapdes',
            'password': 'default',
            'database': 'scrape'}

ITEM_PIPELINES = ['scraper_app.pipelines.LivingSocialPipeline']