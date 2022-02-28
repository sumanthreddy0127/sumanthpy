# e={3,4,5}
# # print(e,type(e))
# print(e,type(e))
# c={3,6.7,"sum",("null",5)}
# print(c,type(c))
# c={50,60,70}
# # print(c[1])
# print(c,type(c))
# d=frozenset(c)
# print(d)
# print(d,type(d))
# print(d[0])

# e={4,5,6}
# f='hello',1,4,7
# e.add(f)
# print(e)

# r={7,9,2}
# r.clear()
# print(r)

# e={4,5,6,7};f={40,20,40};c={90,10,40};w={41,59,60}
# print(e.intersection(f))
# print(e.intersection(c))
# print(e.intersection(w))
# print(f.intersection(e))
# print(f.intersection(c))
# print(f.intersection(w))
# print(c.intersection(f))
# print(c.intersection(e))
# print(c.intersection(w))

# e={4,7,9}
# d={1,6,4}
# print(e.union(d))
# print(d.union(e))

# d={1,4,6,34,90}
# e={9,2,9}
# # f={2,5,6}
# d.update(e)
# print(d)
# # e.update(f)
# # f.update(e)
# # print(f)
# print(d.difference(e))
# print(e.difference(d))
# print(d-e)
# print(e-d)

# e={45,89,49,10,81,37}
# # e.dicard(49)
# # print(e)
# # e.dicard(37)
# # print(e)
# e.pop()
# print(e)

# e={5,7,9,2,7}
# f={1,6,8,9}
# r={2,3,4}
# # print("The number are disjoint",e.isdisjoint(f))
# # print("The number are disjoint",e.isdisjoint(r))
# # print("The number are disjoint",f.isdisjoint(r))
# print(e.issubset(f))
# print(e.issubset(r))
# print(f.issubset(r))

u={4,7,9,3,90}
b={5,40,80}
#u.difference_update(b)
#b.difference_update(u)
#print(u)
# print(b)
# u.copy()
# print(u)
# c=u.symmetric_difference(b)
# print(c)
# c=u.symmetric_difference_update(b)
# print(c)
# d=b.symmetric_difference_update(u)
# # print(d)
# u.intersection_update(b)
# print(u)
# b.intersection_update(u)
# # print(b)
# print(u.intersection(b))
# print(b.intersection(u))
# u.remove(35)
# print(u)
print(u.issuperset(b))
print(b.issuperset(u))