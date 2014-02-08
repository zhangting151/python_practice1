
numbers = []

def test1(ii ,jj):
    i = 0
    while i < ii:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + jj
        print "Numbers now: ",numbers
        print "At the bottom i is %d" % i

test1(6,2)
print "The numbers:"

for num in numbers:
    print num
