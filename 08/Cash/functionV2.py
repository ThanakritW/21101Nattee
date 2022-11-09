def total(pocket):
    total = 0
    for e in pocket:
        total += e*pocket[e]
    return total

def take(pocket, money_in):
    for e in money_in:
        if(e in pocket):
            pocket[e]+=money_in[e]
        else:
            pocket[e]=money_in[e]
    return pocket[e]

def pay(pocket, amt):
    pay = dict()
    for e in pocket:
        if(amt >= e):
            cnt = min(pocket[e],amt//e)
            pay[e]=cnt
            amt -= e*cnt
    if(amt!=0):
        return dict()
    for e in pay:
        pocket[e]-=pay[e]
    return pay

exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ