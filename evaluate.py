import pdb
choose=input("buy or sell? default [1]\n1.buy\n2.sell\n:>")
high=float(input("please input high price:\n"))
low=float(input("please input low price:\n"))
if choose=='1':
    buy=float(input("please input your buy price:\n"))
    score=(high-buy)/(high-low)
elif choose=='2':
    sell=float(input("please input your sell price:\n"))
    score=(sell-low)/(high-low)*100
print(round(score))
