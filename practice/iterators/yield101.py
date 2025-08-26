"""
How yield prints.
"""


def gen():
    print("Generator started")
    receive = yield "produced-1"
    print("After first yield, receive =", receive)

    receive = yield "produced-2"
    print("After second yield, receive =", receive)

    receive = yield "produced-3"
    print("After third yield, receive =", receive)

    print("Generator ending")


# Create generator
g = gen()

print("--- next(g) ---")
out = next(g)
print("Outside saw:", out)

print("--- g.send('A') ---")
out = g.send("A")
print("Outside saw:", out)

print("--- g.send('B') ---")
out = g.send("B")
print("Outside saw:", out)

print("--- g.send('C') ---")
out = g.send("C")
print("Outside saw:", out)

print("--- advancing again ---")
try:
    out = next(g)
    print("Outside saw:", out)
except StopIteration:
    print("Generator is done")
