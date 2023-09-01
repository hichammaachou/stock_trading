import requests


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key = "89LTG68J78CBY2RH"
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_data = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={api_key}").json()
stock_close_yesterday = float(stock_data['Time Series (Daily)']['2023-08-31']['4. close'])
stock_close_before = float(stock_data['Time Series (Daily)']['2023-08-30']['4. close'])
diff = abs(stock_close_yesterday-stock_close_before)
percentage = diff/stock_close_yesterday *100
if percentage >= 5:
    print('get News')
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_data = requests.get(f'https://newsapi.org/v2/everything?qInTitle={COMPANY_NAME}&apiKey=995c6c3856f749c7846e92760fa22e18').json()
articles = news_data['articles']
articles = articles[:3]
titles = [title['title'] for title in articles]
descriptions = [description['description'] for description in articles]

message = f"""{STOCK}: 🔺{percentage}%
Headline: {titles[0]} 
Brief: {descriptions[0]}
Headline: {titles[1]} 
Brief: {descriptions[1]}
Headline: {titles[2]} 
Brief: {descriptions[2]}"""
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

