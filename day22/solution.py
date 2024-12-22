from collections import defaultdict
from itertools import pairwise
from tqdm import tqdm


def generate(n):
    n = (n << 6 ^ n) & 0xffffff
    n = (n >> 5 ^ n) & 0xffffff
    n = (n << 11 ^ n) & 0xffffff
    return n


def quadruplewise(s):
    return zip(s, s[1:], s[2:], s[3:])


with open("day22/data") as f:
    buyers = [int(x) for x in f.readlines()]

# ==== PART 1 ====
pseudorandom = list()
prices = list()
for secret in buyers:
    secret_numbers = [secret]
    single_prices = [secret % 10]
    for _ in range(2000):
        secret = generate(secret)
        secret_numbers.append(secret)
        single_prices.append(secret % 10)

    prices.append(single_prices)
    pseudorandom.append(secret_numbers)

print(sum(seq[-1] for seq in pseudorandom))


# ==== PART 2 ====
buyer_quad_prices = defaultdict(dict)
changes = [[p2 - p1 for p1, p2 in pairwise(seq)] for seq in prices]
for buyer, (buyer_prices, buyer_changes) in enumerate(zip(prices, changes)):
    for x0, quadruplet in zip(buyer_prices, quadruplewise(buyer_changes)):
        if quadruplet not in buyer_quad_prices[buyer]:
            buyer_quad_prices[buyer][quadruplet] = x0 + sum(quadruplet)


X = defaultdict(dict)
for buyer, quad_prices in buyer_quad_prices.items():
    for quadr, p in quad_prices.items():
        X[quadr][buyer] = p


max_price = 0
for quad, y in X.items():    
    max_price = max(sum(y.values()), max_price)
print(max_price)