from database import Database

from models.news import News

 

def getNews():

    connection = Database()

    query =''' SELECT

            news_data.news_id,

            news_data.companyname,

            news_data.isin,

            news_data.ticker_id,

            news_data.ticker_region,

            news_data.country_code,

            news_data.keywords,

            news_data.headline,

            news_data.deliverytimestamputc,

            topics.topic FROM

                public.news_data lEFT JOIN public.topics

                ON public.news_data.news_id = public.topics.news_id;'''

   

    rows = connection.query(query)

    newssub = []

    if len(rows)!=0:

        for row in rows:

            news_id =  row[0]

            companyname = row[1]

            isin = row[2]

            ticker_id = row[3]

            ticker_region = row[4]

            country_code = row[5]

            keywords = row[6]

            headline  = row[7]

            deliverytimestamputc = row[8]

            topic = row[9]

       

            record = News(news_id,companyname,isin ,ticker_id ,ticker_region ,country_code ,keywords , headline ,"" ,deliverytimestamputc,topic)

            newssub.append(record.convert_to_dict())

    connection.close()

    return newssub
def getLimitNews(limitNum):

    connection = Database()

    query =''' SELECT

            news_data.news_id,

            news_data.companyname,

            news_data.isin,

            news_data.ticker_id,

            news_data.ticker_region,

            news_data.country_code,

            news_data.keywords,

            news_data.headline,

            news_data.deliverytimestamputc,

            topics.topic FROM

                public.news_data LEFT JOIN public.topics

                ON public.news_data.news_id = public.topics.news_id

                LIMIT %s;'''

 

    rows = connection.query(query,(limitNum,))

    newssub = []

    if len(rows)!=0:

        for row in rows:

            news_id =  row[0]

            companyname = row[1]

            isin = row[2]

            ticker_id = row[3]

            ticker_region = row[4]

            country_code = row[5]

            keywords = row[6]

            headline  = row[7]

            deliverytimestamputc = row[8]

            topic = row[9]

 

            record = News(news_id,companyname,isin ,ticker_id ,ticker_region ,country_code ,keywords , headline ,"" ,deliverytimestamputc,topic)

            newssub.append(record.convert_to_dict())

    connection.close()

    return newssub
