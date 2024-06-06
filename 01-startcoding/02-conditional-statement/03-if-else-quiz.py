bag_price = int(input('가방 가격을 입력해주세요>>> '))
watch_price = int(input('시계 가격을 입력해주세요>>> '))
total_price = bag_price + watch_price

MAX_DISCOUNT_PRICE = 100000
MID_DISCOUNT_PRICE = 50000

if total_price >= MAX_DISCOUNT_PRICE:
    print('할인률 30%')
    total_price *= 0.7
elif total_price >= MID_DISCOUNT_PRICE:
    print('할인률 20%')
    total_price *= 0.8
else:
    print('할인률 10%')
    total_price *= 0.9

print('할인가: ', total_price)

