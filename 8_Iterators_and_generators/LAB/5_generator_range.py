def genrange(start: int, end: int):
    num = start
    while num <= end:
        yield num
        num += 1


collection = genrange(1, 5)

for c in collection:
    print(c)

print(list(collection))

# ============== това е различно от това
# защото след като генератора се exhaust-не, не може да се принтира
# но ако се превърне в list(), той не се exhaust-ва

collection = list(genrange(1, 5))

for c in collection:
    print(c)

print(list(collection))