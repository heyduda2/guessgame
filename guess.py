import random as ran
import matplotlib.pyplot as plt

#Zahl festlegen
num = ran.randint(1,100)
count = 1
s = True
var = []

#Eingabe des Benutzers
while s:
	guess = raw_input('Please take a guess')
	
	try:
		int(guess)
	except ValueError:
		print 'na na na!'
		continue

	if int(guess) == num:
		print 'Right!, you have taken' + str(count) + 'guesses'
		var.append(0)
		s = False
	
	elif int(guess) < num:
		print 'too small, try again'
		count = count + 1
		var.append(int(guess)-num)

	
	elif int(guess) > num:
		print 'too big, try again'
		count = count + 1
		var.append(int(guess)-num)


plt.figure()
plt.plot(range(count), var)
plt.xlabel('Versuche')
plt.ylabel('Abweichung')
plt.show()

name = 'Lena'

#hs = pickle.load(open('../hs.pickle','rb'))

