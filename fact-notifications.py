import notify2
import random
import threading

t = 600.0  # 600 seconds

def read_line(number):
	f = open('factslide.txt','r')
	for i in range(number-1):
		f.readline()
	fact = str(f.readline())
	fact = fact[fact.index('>')+1:]
	f.close()
	return fact

def show_fact():
	threading.Timer(t, show_fact).start()
	notify2.init('Fact')
	number = random.randint(1,8061)
	n = notify2.Notification('Fact #' + str(number), read_line(number))
	n.show()

show_fact()