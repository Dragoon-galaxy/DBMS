def find_closure(X, F):
    closure = set(X)
    while True:
        prev_closure = set(closure)
        for u, v in F:
            if set(u).issubset(closure):
                closure = closure.union(set(v))
        if closure == prev_closure:
            break
    return closure
F = [({'A'}, {'B','C'}), ({'B'}, {'D'}), ({'E'}, {'A'}), ({'C','D'}, {'E'})]

# Attribute closure of BC
X = {'B','C'}
closure = find_closure(X, F)
print(closure)

#Attribute closure of B
Y = {'B'}
closure = find_closure(Y, F)
print(closure)


#Attribute closure of A
Z = {'A'}
closure = find_closure(Z, F)
print(closure)

