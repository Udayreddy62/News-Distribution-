class News:
    def __init__(self,

        news_id,

        companyname,

        isin ,

        ticker_id ,

        ticker_region ,

        country_code ,

        keywords ,

        headline ,

        story ,

        deliverytimestamputc,

        topic

        ):

 

        self.news_id = news_id

        self.companyname = companyname

        self.isin = isin

        self.ticker_id = ticker_id

        self.ticker_region = ticker_region

        self.country_code = country_code

        self.keywords = keywords

        self.headline = headline

        self.story = story

        self.deliverytimestamputc = deliverytimestamputc

        self.topic=topic

       

    def convert_to_dict(self):

        dictionary = {

                    "news_id":self.news_id,

                    "companyname":self.companyname,

                    "isin":self.isin,

                    "ticker_id":self.ticker_id,

                    "ticker_region":self.ticker_region,

                    "country_code":self.country_code,

                    "keywords":self.keywords,

                    "headline":self.headline,

                    "deliverytimestamputc":self.deliverytimestamputc,

                    "topic":self.topic

                    }

        return dictionary

 

    def convert_to_dictionary(self):

        news_dict = {'news_id' : self.news_id,

                     'companyname' : self.companyname,

                     'isin' : self.isin,

                     'ticker_id' : self.ticker_id,

                     'ticker_region' : self.ticker_region,

                     'country_code' : self.country_code,

                     'keywords' : self.keywords,

                     'headline' : self.headline,

                     'story' : self.story,

                     'deliverytimestamputc' : self.deliverytimestamputc,

                     'topic' : self.topic

                     }

        return news_dict

