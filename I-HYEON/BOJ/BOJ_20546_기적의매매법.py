'''
1. 주어진 현금을 cash로 받아온다.
2. 14일간의 주가를 리스트 stocks로 받아온다.
3. 먼저, 준현이의 14일 후 자산을 계산한다.
    stocks리스트를 for문으로 순회
    i일차에 준현이가 가진 주식 개수는 cash//stocks[i], 현금은 cash - cash//stocks[i] * stocks[i]로 갱신
4. 그 다음, 성민이의 14일 후 자산을 계산한다.
    stocks리스트를 for문으로 순회
    i일차에 성민이는(1일~3일은 패스) 3일 연속 주가가 상승했는지 체크해서, true면 전량 매도, false면 전량 매수
5. 둘 다 14일차가 되었을 때, 남은 현금 + 1월 14일의 주가 * 주식수 로 최종자산을 계산해서 저장한다.
6. 비교 후 준현이가 크면 "BNP" 성민이가 크면 "TIMING"을 출력한다.
'''

cash = int(input())
stocks = list(map(int,input().split()))

JH_cash, SM_cash = cash, cash
JH_stock_cnt,SM_stock_cnt = 0, 0
for i in range(14):
    # 준현이 계산
    JH_stock_cnt += JH_cash//stocks[i]
    JH_cash -= (JH_cash//stocks[i]) * stocks[i]

    # 성민이 계산
    if i >= 3:

        if stocks[i-3] > stocks[i-2] > stocks[i-1] > stocks[i]:  # 3일 연속 하락이면
            SM_stock_cnt += SM_cash//stocks[i]
            SM_cash -= (SM_cash // stocks[i]) * stocks[i]
        elif stocks[i-3] < stocks[i-2] < stocks[i-1] < stocks[i]:  # 3일 연속 상승이면
            SM_cash += SM_stock_cnt * stocks[i]
            SM_stock_cnt = 0  # 초기화

# 마지막 날 자산 계산(남은 현금 + 1월 14일의 주가 * 주식수 )
JH = JH_cash + stocks[13] * JH_stock_cnt
SM = SM_cash + stocks[13] * SM_stock_cnt

if JH>SM:
    print('BNP')
elif JH<SM:
    print('TIMING')
else:
    print('SAMESAME')