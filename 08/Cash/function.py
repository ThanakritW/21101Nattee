def total(pocket):
    total = 0
    for e in pocket:
        total += e*pocket[e]
    return total


def take(pocket, money_in):
    for e in money_in:
        try:
            pocket[e] += money_in[e]
        except:
            pocket[e] = money_in[e]
    return pocket


def pay(pocket, amt):
    total = amt
    pay = {}
    notes = sorted(pocket.keys(),reverse=True)
    for e in notes:
        cnt = min(pocket[e], total//e)
        if(cnt == 0):
            continue
        total -= cnt*e
        pay[e] = cnt
    if(total != 0):
        return {}
    for e in pay:
        pocket[e] -= pay[e]
    return pay


exec(input().strip())  # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
