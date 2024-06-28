def squares(n):
    num = 1
    while num <= n:
        yield num * num
        num += 1


collection = squares(7)

for c in collection:
    print(c)

print(list(squares(5)))
 