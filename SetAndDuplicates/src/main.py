a = [
    12,
    24,
    35,
    24,
    88,
    120,
    155,
    88,
    120,
    155
]

set_a = set()

for i in a[::-1]:
    if i in set_a:
        continue
    print(i)
    set_a.add(i)
