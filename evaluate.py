import pdb
choose=input("buy or sell? default [1]\n1.buy\n2.sell\n:>")
if choose=='2':
    sell=float(input("please input your sell price:\n"))
    high=float(input("please input high price:\n"))
    low=float(input("please input low price:\n"))
    score=(sell-low)/(high-low)*100
else:
    buy=float(input("please input your buy price:\n"))
    high=float(input("please input high price:\n"))
    low=float(input("please input low price:\n"))
    score=(high-buy)/(high-low)*100
print("得分:"+str(round(score)))
