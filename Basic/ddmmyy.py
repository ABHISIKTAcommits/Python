totald=int(input("ENTER THE TOTAL NUMBER OF DAYS: "))
year=totald//365
remd=totald%365
mo=remd//30
days=remd%30
print("year: ",year)
print("months: ",mo)
print("days: ",days)