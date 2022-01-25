#Lists

# creating a list

a = [] 
b = [] * 30
c = [0 for i in range(10)]
d = list(range(10,20))
e = list(range(10,50,5))
print(a,"\n",b,"\n",c,"\n",d,"\n",e)

# access list

f = ["abc", 34, True, 40, "male"]
print(f[-1])
print(f[:4])
print(f[2:4])
print(f[-4:-1])
if "abc" in f: print("exits")

# add items to list

g = ["apple", "banana", "cherry"]
g.append("orange")
print(g)
g.insert(1,"grapes")
print(g)
g1 = ["strawberry","blueberry"]
g.extend(g1)
print(g)

# remove items from list

h = ["apple", "banana", "cherry","strawberry","blueberry"]
h.remove("banana")
print(h)
h.pop(1)
print(h)
del h[0]
print(h)
h.clear()
print(h)

# List functions

i = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(len(i))
i.sort()
print(i)
i.sort(reverse=True)
print(i)
i.reverse()
print(i)
print(i.index('mango'))
