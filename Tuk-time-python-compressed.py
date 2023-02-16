

import yfinance as yf
import plotly.express as px
#import tweepy

BTCCAD = yf.Ticker("BTC-CAD")
#print(BTCCAD.info)

# get historical market data
hist = BTCCAD.history(period="365d")
hist_df = hist.drop(columns=['Dividends', 'Stock Splits','Volume'])

#define function
def SatsConv(x):
  SatsPerCAD = 1/(x/100000000)
  return SatsPerCAD

#convert prices to sats
hist_sats = hist_df.applymap(SatsConv)

#change to integers
sats = str(round((hist_sats.at[hist_sats.index[-1],'Close']), 0))[:-2]

# Area chart
area_chart = px.area(hist_sats['Close'], title = 'Satoshi per Canadian Dollar', color_discrete_map={"Close": "DarkOrange"})

area_chart.update_xaxes(title_text = 'Date')
area_chart.update_yaxes(title_text = 'Satoshis per CAD$')
area_chart.update_layout(showlegend = False)

#area_chart.show()
area_chart.write_image("/Users/phillipburrows/Documents/GitHub/Tuktoyaktuk-time/tukTime_chart.png")

#consumer_key = "6TQdcibOiWvMfRwaFD1oq60Dv"
#consumer_secret = "9iQVR7QeHbJZgsgY6NOOw19hPL0tTbLym6Ub0vi5gKVOM5K4SK"
#access_token = "1423487055498186752-QJMF5Pfyd1KChoS3ynJFq7tWHMJ6VY"
#access_token_secret = "feLv5k06tjsAeT1RmH8z7dyce062blB9J58tD7mrbMk2E"

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

#api = tweepy.API(auth)
