price = int(input('삼성전자의 현재 가격을 입력해주세요>>>'))

SELL_MIN_PRICE = 90000
IDLE_MIN_PRICE = 80000

if price >= SELL_MIN_PRICE:
    print('매도합니다.')
elif price >= IDLE_MIN_PRICE:
    print('대기중입니다.')
else:
    print('매수합니다.')
