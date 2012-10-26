#encoding=utf-8
import random
a = random.randint(0,1000)
b = input("choisir une valeur : ")
while b!=a:
	if b<a:
	     print "plus grand"
	else:
	     print "plus petit"
	b = input("choisir une valeur : ")
if b==a:
	     print "bravo !!!"