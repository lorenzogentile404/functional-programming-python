l = [1,2,3,4]

# map
print(list(map(lambda e: e**2,l)))

# map using list comprehension
print([e**2 for e in l])

# filter
print(list(filter(lambda e: e > 2,l)))

# filter using list comprehension
print([e for e in l if e > 2])

# pythagorean triples using list comprehension
c_max = 100
p = [(a,b,c) for c in range(1,c_max) for b in range(1,c) for a in range(1,b) if a**2 + b**2 == c**2]

print(p)

# extract all a, b, c
A = [e[0] for e in p]
B = [e[1] for e in p]
C = [e[2] for e in p]

# verify using zipped list comprehension
v = [a**2 + b**2 == c**2 for a,b,c in zip(A,B,C)]
print(all(v))

# map-reduce examples

# import functools
# functools.reduce

def myreduce(f, l):
    if len(l) == 1:
        return l[0]
    else:
        return myreduce(f, [f(l[0],l[1])] + l[2:]) 

s = "Hello 1900 World 121 1"

# join
print(' '.join([e for e in s.split() if e.isdigit()]))

# sum
print(sum(([int(e) for e in s.split() if e.isdigit()])))


# join using reduce
print(myreduce(lambda a,b: a + " " + b,[e for e in s.split() if e.isdigit()]))

# ["1900","121","1"]
# ["1900 121","1"]
# ["1900 121 1"]
# "1900 121 1"

# sum using reduce
print(myreduce(lambda a,b: a + b,[int(e) for e in s.split() if e.isdigit()]))

# [1900,121,1]
# [2021,1]
# [2022]
# 2022

b = ["Hello", "1900", "World"]

# all
print(all([e.isdigit() for e in b]))

# any
print(any([e.isdigit() for e in b]))

# all using reduce
print(myreduce(lambda a,b: a and b, [e.isdigit() for e in b]))

# [False, True, False]
# [False, False]
# [False]
# False

# any using reduce
print(myreduce(lambda a,b: a or b, [e.isdigit() for e in b]))

# [False, True, False]
# [True, False]
# [True]
# True







