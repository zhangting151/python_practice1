class TheThing(object):
    def __init__(self):
        self.number = 0

    def some_function(self):
        print "I got called."

    def add_me_up(self,more):
        self.number += more
        return self.number

#two different things
a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print a.add_me_up(20)
print b.add_me_up(30)

print a.number
print b.number

#Study this. This is how you pass a variable
#from one class to another .You wii need this
class TheMultuplier(object):
    def __init__(self,base):
        self.base = base
        print self.base
        print "1111"

    def do_it(self,m):
        return m*self.base

x = TheMultuplier(a.number)
print x.do_it(b.number)

y =  TheMultuplier('hello')
print y.do_it(30)
