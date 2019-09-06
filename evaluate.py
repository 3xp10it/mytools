import pdb
import tushare as ts
from exp10it import get_today_date
today_date=get_today_date()
print("记录交易日所在日期:%s" % today_date)
stock_code=input("please input your stock code in 6 nuber:\n")
a=ts.get_hist_data(stock_code,start=today_date,end=today_date)
choose=input("buy or sell? default [1]\n1.buy\n2.sell\n:>")
if choose=='2':
    sell=float(input("please input your sell price:\n"))
    high=float(a['high'].iloc[0])
    low=float(a['low'].iloc[0])
    score=(sell-low)/(high-low)*100
else:
    buy=float(input("please input your buy price:\n"))
    high=float(a['high'].iloc[0])
    low=float(a['low'].iloc[0])
    score=(high-buy)/(high-low)*100
print("得分:"+str(round(score)))
