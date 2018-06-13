from dotenv import load_dotenv
import json
import os
import requests
import itertools
import csv
import statistics
import datetime
from IPython import embed

load_dotenv()

# see: https://www.alphavantage.co/support/#api-key
api_key = os.environ.get("ALPHAVANTAGE_API_KEY") or "OOPS. Please set an environment variable named 'ALPHAVANTAGE_API_KEY'."


def stock_recommendation(close_prices_data): #source for standard deviation: https://stackoverflow.com/questions/15389768/standard-deviation-of-a-list?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    volatility = statistics.stdev(close_prices_data)
    z_score = volatility/(sum(close_prices_data)/len(close_prices_data))
    first_ten_prices = close_prices_data[0:9]
    last_ten_prices = close_prices_data[90:99]
    avg_first_ten_prices = (sum(first_ten_prices)/len(first_ten_prices))
    avg_last_ten_prices = (sum(last_ten_prices)/len(last_ten_prices))
    if (z_score >= 0 and z_score <= 0.035) and avg_last_ten_prices > avg_first_ten_prices:
        print(f"""
        --------------------------------------------------------------------------------------------------
        CHRIS' STOCK RECOMMENDATION METHODOLOGY & COMPONENTS:

        Z-Score: This measures how volatile the stock is by calculating the standard deviation of its
        closing price over the past 100 days. The volatility of the stock will help determine whether it's
        the right fit for an investor based on an investor's level of risk tolerance. Stocks that have a
        high level of volatility aren't good fits for conservative and risk-averse investors, and vice-versa.

        Time Comparison: This measures the stock's closing price performance over the first 10 days of the
        past 100 days to the last 10 days of the past 100 days. The calculation will help identify whether
        the stock is growing in performance or declining in value. For instance, a stock whose average
        closing price in the first 10 days of the last 100 days is lower than the average closing price
        in the last 10 days of the last 100 days is a stock that's growing in performance.

        CHRIS' STOCK RECOMMENDATION FOR {stocks}: This stock seems pretty steady and doesn't fluctuate a
        lot. Additionally, the stock is showing performance growth over the past 100 days. This is a great
        stock to invest in if you're risk averse and want steady performance.
        --------------------------------------------------------------------------------------------------""")
    elif (z_score >= 0 and z_score <= 0.035) and avg_last_ten_prices > avg_first_ten_prices:
        print(f"""
        --------------------------------------------------------------------------------------------------
        CHRIS' STOCK RECOMMENDATION METHODOLOGY & COMPONENTS:

        Z-Score: This measures how volatile the stock is by calculating the standard deviation of its
        closing price over the past 100 days. The volatility of the stock will help determine whether it's
        the right fit for an investor based on an investor's level of risk tolerance. Stocks that have a
        high level of volatility aren't good fits for conservative and risk-averse investors, and vice-versa.

        Time Comparison: This measures the stock's closing price performance over the first 10 days of the
        past 100 days to the last 10 days of the past 100 days. The calculation will help identify whether
        the stock is growing in performance or declining in value. For instance, a stock whose average
        closing price in the first 10 days of the last 100 days is lower than the average closing price
        in the last 10 days of the last 100 days is a stock that's growing in performance.

        CHRIS' STOCK RECOMMENDATION FOR {stocks}: This stock seems pretty steady and doesn't fluctuate
        a lot. However, the stock has been declining in value over the past 100 days. 100 days. Do not
        invest in this stock because you'll risk losing your investment.
        --------------------------------------------------------------------------------------------------""")
    elif (z_score >= 0 and z_score <= 0.035) and avg_last_ten_prices == avg_first_ten_prices:
        print(f"""
        --------------------------------------------------------------------------------------------------
        CHRIS' STOCK RECOMMENDATION METHODOLOGY & COMPONENTS:

        Z-Score: This measures how volatile the stock is by calculating the standard deviation of its
        closing price over the past 100 days. The volatility of the stock will help determine whether it's
        the right fit for an investor based on an investor's level of risk tolerance. Stocks that have a
        high level of volatility aren't good fits for conservative and risk-averse investors, and vice-versa.

        Time Comparison: This measures the stock's closing price performance over the first 10 days of the
        past 100 days to the last 10 days of the past 100 days. The calculation will help identify whether
        the stock is growing in performance or declining in value. For instance, a stock whose average
        closing price in the first 10 days of the last 100 days is lower than the average closing price
        in the last 10 days of the last 100 days is a stock that's growing in performance.

        CHRIS' STOCK RECOMMENDATION FOR {stocks}: This stock seems pretty steady and doesn't fluctuate a
        lot. Additionally, the stock's price hasn't shown improvement over the past 100 days. If you're
        already investing in this stock, then hold on to it. Otherwise, wait for the price to decrease
        before investing in it.
        --------------------------------------------------------------------------------------------------""")
    elif (z_score >= 0.036 and z_score <= 0.05) and avg_last_ten_prices > avg_first_ten_prices:
        print(f"""
        --------------------------------------------------------------------------------------------------
        CHRIS' STOCK RECOMMENDATION METHODOLOGY & COMPONENTS:

        Z-Score: This measures how volatile the stock is by calculating the standard deviation of its
        closing price over the past 100 days. The volatility of the stock will help determine whether it's
        the right fit for an investor based on an investor's level of risk tolerance. Stocks that have a
        high level of volatility aren't good fits for conservative and risk-averse investors, and vice-versa.

        Time Comparison: This measures the stock's closing price performance over the first 10 days of the
        past 100 days to the last 10 days of the past 100 days. The calculation will help identify whether
        the stock is growing in performance or declining in value. For instance, a stock whose average
        closing price in the first 10 days of the last 100 days is lower than the average closing price
        in the last 10 days of the last 100 days is a stock that's growing in performance.

        CHRIS' STOCK RECOMMENDATION FOR {stocks}: This stock's price fluctuates a bit, so be prepared for
        some price swings. Additionally, the stock is showing performance growth over the past 100 days.
        This is a great stock to invest in if have a moderate risk tolerance.
        --------------------------------------------------------------------------------------------------""")
    elif (z_score >= 0.036 and z_score <= 0.05) and avg_last_ten_prices < avg_first_ten_prices:
        print(f"""
        --------------------------------------------------------------------------------------------------
        CHRIS' STOCK RECOMMENDATION METHODOLOGY & COMPONENTS:

        Z-Score: This measures how volatile the stock is by calculating the standard deviation of its
        closing price over the past 100 days. The volatility of the stock will help determine whether it's
        the right fit for an investor based on an investor's level of risk tolerance. Stocks that have a
        high level of volatility aren't good fits for conservative and risk-averse investors, and vice-versa.

        Time Comparison: This measures the stock's closing price performance over the first 10 days of the
        past 100 days to the last 10 days of the past 100 days. The calculation will help identify whether
        the stock is growing in performance or declining in value. For instance, a stock whose average
        closing price in the first 10 days of the last 100 days is lower than the average closing price
        in the last 10 days of the last 100 days is a stock that's growing in performance.

        CHRIS' STOCK RECOMMENDATION FOR {stocks}: This stock's price fluctuates a bit, so be prepared for
        some price swings. Additionally, the stock has been declining in value over the past 100 days.
        Do not invest in this stock because you'll risk losing your investment.
        --------------------------------------------------------------------------------------------------""")
    elif (z_score >= 0.036 and z_score <= 0.05) and avg_last_ten_prices == avg_first_ten_prices:
        print(f"""
        --------------------------------------------------------------------------------------------------
        CHRIS' STOCK RECOMMENDATION METHODOLOGY & COMPONENTS:

        Z-Score: This measures how volatile the stock is by calculating the standard deviation of its
        closing price over the past 100 days. The volatility of the stock will help determine whether it's
        the right fit for an investor based on an investor's level of risk tolerance. Stocks that have a
        high level of volatility aren't good fits for conservative and risk-averse investors, and vice-versa.

        Time Comparison: This measures the stock's closing price performance over the first 10 days of the
        past 100 days to the last 10 days of the past 100 days. The calculation will help identify whether
        the stock is growing in performance or declining in value. For instance, a stock whose average
        closing price in the first 10 days of the last 100 days is lower than the average closing price
        in the last 10 days of the last 100 days is a stock that's growing in performance.

        CHRIS' STOCK RECOMMENDATION FOR {stocks}: This stock's price fluctuates a bit, so be prepared for
        some price swings. Additionally, the stock's price hasn't shown improvement over the past 100 days.
        If you're already investing in this stock, then hold on to it. Otherwise, wait for the price to
        decrease before investing in it.
        --------------------------------------------------------------------------------------------------""")
    elif z_score > 0.05 and avg_last_ten_prices > avg_first_ten_prices:
        print(f"""
        --------------------------------------------------------------------------------------------------
        CHRIS' STOCK RECOMMENDATION METHODOLOGY & COMPONENTS:

        Z-Score: This measures how volatile the stock is by calculating the standard deviation of its
        closing price over the past 100 days. The volatility of the stock will help determine whether it's
        the right fit for an investor based on an investor's level of risk tolerance. Stocks that have a
        high level of volatility aren't good fits for conservative and risk-averse investors, and vice-versa.

        Time Comparison: This measures the stock's closing price performance over the first 10 days of the
        past 100 days to the last 10 days of the past 100 days. The calculation will help identify whether
        the stock is growing in performance or declining in value. For instance, a stock whose average
        closing price in the first 10 days of the last 100 days is lower than the average closing price
        in the last 10 days of the last 100 days is a stock that's growing in performance.

        CHRIS' STOCK RECOMMENDATION FOR {stocks}: This stock's price fluctuates a lot, so be prepared for
        a lot of price swings. Additionally, the stock is showing performance growth over the past 100 days.
        This is a great stock to invest in if have a high risk tolerance. Conservative investors may want
        to stay away from this stock.
        --------------------------------------------------------------------------------------------------""")
    elif z_score > 0.05 and avg_last_ten_prices < avg_first_ten_prices:
        print(f"""
        --------------------------------------------------------------------------------------------------
        CHRIS' STOCK RECOMMENDATION METHODOLOGY & COMPONENTS:

        Z-Score: This measures how volatile the stock is by calculating the standard deviation of its
        closing price over the past 100 days. The volatility of the stock will help determine whether it's
        the right fit for an investor based on an investor's level of risk tolerance. Stocks that have a
        high level of volatility aren't good fits for conservative and risk-averse investors, and vice-versa.

        Time Comparison: This measures the stock's closing price performance over the first 10 days of the
        past 100 days to the last 10 days of the past 100 days. The calculation will help identify whether
        the stock is growing in performance or declining in value. For instance, a stock whose average
        closing price in the first 10 days of the last 100 days is lower than the average closing price
        in the last 10 days of the last 100 days is a stock that's growing in performance.

        CHRIS' STOCK RECOMMENDATION FOR {stocks}: This stock's price fluctuates a lot, so be prepared for
        a lot of price swings. Additionally, the stock has been declining in value over the past 100 days.
        Do not invest in this stock because you'll risk losing your investment.
        --------------------------------------------------------------------------------------------------""")
    elif z_score > 0.05 and avg_last_ten_prices == avg_first_ten_prices:
        print(f"""
        --------------------------------------------------------------------------------------------------
        CHRIS' STOCK RECOMMENDATION METHODOLOGY & COMPONENTS:

        Z-Score: This measures how volatile the stock is by calculating the standard deviation of its
        closing price over the past 100 days. The volatility of the stock will help determine whether it's
        the right fit for an investor based on an investor's level of risk tolerance. Stocks that have a
        high level of volatility aren't good fits for conservative and risk-averse investors, and vice-versa.

        Time Comparison: This measures the stock's closing price performance over the first 10 days of the
        past 100 days to the last 10 days of the past 100 days. The calculation will help identify whether
        the stock is growing in performance or declining in value. For instance, a stock whose average
        closing price in the first 10 days of the last 100 days is lower than the average closing price
        in the last 10 days of the last 100 days is a stock that's growing in performance.

        CHRIS' STOCK RECOMMENDATION FOR {stocks}: This stock's price fluctuates a lot, so be prepared for
        a lot of price swings. Additionally, the stock's price hasn't shown improvement over the past 100 days.
        If you're already investing in this stock, then hold on to it. Otherwise, if you don't mind risk
        in your investments, then you may want to wait for the price to decrease before investing in it.
        --------------------------------------------------------------------------------------------------""")

today = datetime.date.today()

now = datetime.datetime.now()

stock_symbols = []

print("""
    ------------------------------------------------------------------------
    Welcome to the Robo Adviser app! You can enter the stock symbols that
    you want to research. Once you're done, please enter 'DONE' to proceed
    to the other parts of the app. Happy investing!
    ------------------------------------------------------------------------
    """)

while True: #source: found helpful tips here: https://automatetheboringstuff.com/chapter5/
    stock_symbol = input("Please enter the symbol of stock #" + str(len(stock_symbols) + 1) + ": ")
    if stock_symbol == "DONE":
        break
    elif len(stock_symbol) < 6 and stock_symbol.isalpha():
        stock_symbols.append(stock_symbol)
    else:
        print("The stock symbol that you entered isn't valid. Please try again.")
        continue

print("These are the stocks that you selected: " + str(stock_symbols))

print("-------------------------------------------------------------------------------------")
print("Your stock report and recommendation was pulled during this time: " + "%02d/%02d/%04d %02d:%02d:%02d" % (now.month, now.day, now.year, now.hour, now.minute, now.second)) #source: this formula comes from my shopping_cart script, and I learned it from CodeCademy's date module
print("-------------------------------------------------------------------------------------")

for stocks in stock_symbols:
    filename = "stock_information_" + stocks + ".csv"
    filename_dir = "data/" + filename
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", filename_dir)
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stocks}&apikey={api_key}"
    response = requests.get(request_url)
    response_body = json.loads(response.text)
    if "Error Message" in response.text: #source: your demo on validation errors in class
        print("REQUEST ERROR, PLEASE TRY AGAIN. CHECK YOUR STOCK SYMBOL.")
        quit("Stopping the program. Feel free to start over.")
    response_body_time_series = (response_body["Time Series (Daily)"])
    latest_closing_date = response_body["Meta Data"]["3. Last Refreshed"]
    latest_price = response_body["Time Series (Daily)"][latest_closing_date]["4. close"]
    latest_price_float = float(latest_price)
    latest_price_usd = ' ${0:.2f}'.format(latest_price_float) #source: your formatting notes on currency
    print(f"DATE WHEN STOCK INFORMATION FOR {stocks} WAS REFRESHED: " + latest_closing_date)
    print(f"LATEST DAILY CLOSING PRICE FOR {stocks} IS:" + latest_price_usd)
    stock_history = list(response_body_time_series.items())
    close_prices_data = []
    for s in stock_history:
        s = list(s)
        close_prices = s[1]["4. close"]
        close_prices_data.append(float(close_prices))
    with open(csv_filepath, "w") as csv_file: #source: your notes on csv files
        writer = csv.DictWriter(csv_file, fieldnames=["timestamp", "1. open", "2. high", "3. low", "4. close", "5. volume"])
        writer.writeheader()
        for s in stock_history:
            s = list(s)
            timestamp_list = s[0]
            timestamp_dict = {"timestamp": timestamp_list}
            stock_statistics_dictionary = s[1]
            row = {}
            row.update(timestamp_dict)
            row.update(stock_statistics_dictionary) #source: figured out this technique here: http://treyhunner.com/2016/02/how-to-merge-dictionaries-in-python/
            writer.writerow(row)
    max_close_price = max(close_prices_data)
    min_close_price = min(close_prices_data)
    max_close_price_usd = ' ${0:.2f}'.format(max_close_price)
    min_close_price_usd = ' ${0:.2f}'.format(min_close_price)
    print("Here is the highest close price over the last 100 days: " + max_close_price_usd)
    print("Here is the lowest close price over the last 100 days: " + min_close_price_usd)
    stock_recommendation(close_prices_data)
