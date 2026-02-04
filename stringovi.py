a = "Lorem ipsum:Jao! dolor sit amet"
c = "consectetur adipiscing elit,"
d = "sed do eiusmod tempor incididunt"
b = "ut labore et dolore magna aliqua."
#print(a, b, c, d, sep=" ")
list1 = [a, b, c, d]
print((list1))
for element in list1:
    print(element)

for korak in range(0,len(list1),2): #bez zadnjeg ",2" ispisuje sva 4 koraka, a 2 mu daje dužinu koraka
    print(korak, "Korak")