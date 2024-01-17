def f(fnc,prods):
    result=list(map(fnc,prods))
    return ','.join(result)


print(f(lambda x: "id:"+x[:2],["water","cheese","tomato"]))