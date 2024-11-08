from database import Database

from models.news import News

def retrieve_newsbyid(id):

    user_given_newsid = '''SELECT

            news_data.news_id,

            news_data.companyname,

            news_data.isin,

            news_data.ticker_id,

            news_data.ticker_region,

            news_data.country_code,

            news_data.keywords,

            news_data.headline,

            news_data.story,

            news_data.deliverytimestamputc,

            topics.topic

                FROM public.news_data

                LEFT JOIN public.topics ON news_data.news_id = topics.news_id

                WHERE public.news_data.news_id = %s;

                            '''

 

    connection = Database()

    news_array = connection.query(user_given_newsid, (id,))

    connection.close()

    if news_array and len(news_array)>0 :

        news_row = news_array[0]

        news_obj = News(news_row[0] ,news_row[1] ,news_row[2] , news_row[3], news_row[4], news_row[5], news_row[6], news_row[7], news_row[8], news_row[9], news_row[10])

 

        return news_obj

    else:

        return None
