import time
import pyupbit
import datetime
import requests

ticker = 'KRW-XRP' #리플
slack_workspace_name = "#stock"

access = "nTxJ2ZFvqCn59CKaqB3j7rKq3wrfWm0kG6pYzqxL"
secret = "q9A0UnctJ38Pui6lzYEhjxeT8NFTC3OMxR2cYwyN"
slackToken = "xoxb-2037958940615-2052963915427-mhDisQK4flRdtubR2CdXWd5c"

def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_ma15(ticker):
    """15일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

def get_balance(coin):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == coin:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("프로그램 시작")

# 시작 메세지 슬랙 전송
post_message(slackToken, slack_workspace_name, "자동매매 봇 투입")



tickerbalance = upbit.get_balance(ticker)
print(tickerbalance)
post_message(slackToken, slack_workspace_name, "리플 가격 조회" +str(tickerbalance))

temp1 = get_current_price(ticker)
temp2 = get_target_price(ticker, 0.5)
temp3 = get_ma15(ticker)

print(temp1)
post_message(slackToken, slack_workspace_name, "현재 가격 조회" +str(temp1))

print(temp2)
post_message(slackToken, slack_workspace_name, "목표 매수 가격 조회" +str(temp2))

print(temp3)
post_message(slackToken, slack_workspace_name, "15일 이동 평균선 조회" +str(temp3))


temp4 = upbit.get_balance("KRW")
print(temp4)
post_message(slackToken, slack_workspace_name, "내 자산" +str(temp4))


while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time(ticker)
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price(ticker, 0.5)
            ma15 = get_ma15(ticker)
            current_price = get_current_price(ticker)
            if target_price < current_price and ma15 < current_price:
                krw = upbit.get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order(ticker, krw*0.9995)
                    post_message(slackToken,slack_workspace_name, "XRP 매수 : " +str(buy_result))
        else:
            btc = upbit.get_balance(ticker)
            if btc > 5000:
                sell_result = upbit.sell_market_order(ticker, btc*0.9995)
                post_message(slackToken,slack_workspace_name, "XRP 매도 : " +str(sell_result))
        time.sleep(1)
    except Exception as e:
        print(e)
        post_message(slackToken,slack_workspace_name, e)
        time.sleep(1)
