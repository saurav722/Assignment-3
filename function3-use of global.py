a = 10
def f():
 	print ('Inside f() : ', a)
def g(): 
 	a = 20
print ('Inside g() : ',a)
def h(): 
 	global a
a = 30
print ('Inside h() : ',a)
print ('global : ',a)
f()
print ('global : ',a)
g()
print ('global : ',a)
h()

