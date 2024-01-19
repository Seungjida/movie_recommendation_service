# 데이터 추출 예시

stocks = [
    {'name': '삼성전자', 'price': '78,000'},
    {'name': 'SK하이닉스', 'price': '124,500'},
    {'name': '삼성전자우', 'price': '70,900'},
    {'name': '삼성바이오로직스', 'price': '836,000'},
    {'name': 'NAVER', 'price': '335,000'},
    {'name': 'LG화학', 'price': '710,000'},
    {'name': '현대차', 'price': '209,500'},
    {'name': '카카오', 'price': '96,600'},
    {'name': '삼성SDI', 'price': '624,000'},
    {'name': '기아', 'price': '83,800'},
    {'name': 'POSCO', 'price': '304,000'},
    {'name': '셀트리온', 'price': '187,000'},
    {'name': '현대모비스', 'price': '262,000'},
    {'name': '카카오뱅크', 'price': '51,100'},
    {'name': 'KB금융', 'price': '57,800'},
    {'name': 'SK이노베이션', 'price': '246,000'},
    {'name': '삼성물산', 'price': '115,000'},
    {'name': 'LG전자', 'price': '130,000'},
    {'name': '신한지주', 'price': '38,550'},
    {'name': '카카오페이', 'price': '148,500'},
    {'name': '토스'},
]

# get()은 key에 대응되는 value를 리턴한다.
# 근데! 딕셔너리에 존재하지 않는 키로 값을 가지고 오려고 하면 None을 리턴시킨다.
# get(x, '디폴트 값'): 딕셔너리 안에 key가 없을 경우, 미리 정해 둔 디폴트 값을 대신 가져오게 한다~
for stock in stocks:
    print(stock.get('price'))

for stock in stocks:
    print(stock.get('price', '비상장 주식입니다.'))
