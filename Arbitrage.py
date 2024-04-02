liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

# swap tokenX to tokenY
def swap(tokenX, tokenY, q, liquidity):
    if tokenX[-1] < tokenY[-1]:
        x0 = liquidity[(tokenX, tokenY)][0]
        y0 = liquidity[(tokenX, tokenY)][1]
        k = x0 * y0
        x1 = x0 + q *0.997
        y1 = k / x1
        liquidity[(tokenX, tokenY)] = (x1, y1)
        return (y0 - y1)
    else:
        y0 = liquidity[(tokenY, tokenX)][0]
        x0 = liquidity[(tokenY, tokenX)][1]
        k = x0 * y0
        x1 = x0 + q*0.997
        y1 = k / x1
        liquidity[(tokenY, tokenX)] = (y1, x1)
        return (y0 - y1)

balance = {
    "tokenA": 0,
    "tokenB": 5,
    "tokenC": 0,
    "tokenD": 0,
    "tokenE": 0,
}

route = []
init_liq = liquidity.copy()
max_balance = 5
max_route = []

def dfs(_route, _balance, _liquidity):
    if len(_route) >= 6:
        return
    if len(_route) and _route[-1][-1] == "tokenB":
        # print(_route, _balance["tokenB"])
        global max_balance
        if _balance["tokenB"] > max_balance:
            max_balance = _balance["tokenB"]
            global max_route
            max_route = _route
        return
    for token in _balance:
        if _balance[token] > 0:
            for token2 in _balance:
                if token2 == token:
                    continue
                init_route, init_balance, init_liquidity = _route.copy(), _balance.copy(), _liquidity.copy()
                _balance[token2] += swap(token, token2, _balance[token], _liquidity)
                _balance[token] = 0
                _route.append((token, token2))
                # print(f"swap {token} to {token2}, len={len(_route)}, route={_route}, balance={_balance}")
                dfs(_route, _balance, _liquidity)
                _route = init_route
                _balance = init_balance
                _liquidity = init_liquidity
                # print(_route)

dfs([], balance, liquidity)
print(max_route[0][0], end="")
for i in range(1, len(max_route)):
    print(f"->{max_route[i][0]}", end="")
print(f"->{max_route[-1][1]}")
print(f"tokenB balance: {max_balance}")
# print(max_route)



