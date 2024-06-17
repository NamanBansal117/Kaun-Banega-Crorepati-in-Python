import time
import random

q = [
		"Steve Jobs is the founder and CEO of which company",
		"Par, Bogey, Eagle and Albatross are terms associated with which sport",
		"What is the name of the black hole around which the milky way revolves",
		"Where is the biggest desert of the world located",
		"Which city is known as 'The City of Lights'",
		"What is the name of the first indian Bollywood film",
		"The Statue of Liberty was  gifted to America from what European country",
		"Where is the largest mountain of the universe located",
		"Which of the following is the only man-made structure visible from space",
		"Who is known as the father of cricket"
]

a = [
	"Apple", "Golf", "Sagittarius A", "Antarctica", "Paris, France",
	"Raja Harishchandra", "France", "Mars", "The Great Wall of China",
	"William Gilbert"
]
b = [
	"Microsoft", "Hockey", "Messier 60", "Africa", "Venice, Italy", "Alam Ara",
	"Britain", "India", "The Statue of Liberty", "Clifford Kendrick"
]
c = [
	"Google", "Baseball", "Cygnus X-1", "India", "Los Angeles, USA",
	"Bhakta Vidur", "Italy", "Jupiter", "The Giza Pyramids",
	"Raymond Miller"
]
d = [
	"Facebook", "Football", "Stellar", "Saudi Arabia", "Illinois, USA",
	"A Throw of Dice", "Russia", "Neptune", "The Colosseum",
	"Martin Wolfe"
]

p = [
    1000, 10000, 100000, 200000, 350000, 500000, 750000, 10000000, 20000000,
    100000000
]


def sf(n):
	s, *d = str(n).partition(".")
	r = ",".join([s[x - 2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
	return "".join([r] + d)


print("Welcome to Kaun Banega Crorepati!")

print("There are ten questions")
print('\n')

print("The Prizes for each question are as follows:-")

i = 9
while i >-1 :
	if i == 2 or i == 5 or i == 8:
		print("Q",i + 1, ":", sf(p[i]), "<---Checkpoint!")
	else:
		print("Q",i + 1, ":", sf(p[i]))
	i = i - 1

print('\n')
print("You Will be Given TWO Lifelines:-")
print("1 : 50:50 :  Randomly Eliminates Two Incorrect Options")
print("2 : Pass : Allows You to Skip the Question")

print('\n')
# a = input("Press any key to begin")	
time.sleep(1)
n = 0

while n < len(a):
	print("\n")
	print("QUESTION", n + 1)
	print(q[n], "?")
	print('\n')
	opt=[a[n],b[n],c[n],d[n]]
	random.shuffle(opt)
	on=0
	while on<=3 :
		print(on+1,":",str(opt[on]))
		on=on+1
	ans = input("Press Keys 1-4 to select an Option\nPress 5 for 50:50\nPress 6 for PASS\n")
	if str(opt[int(ans) - 1]) == str(a[n]):
		print("Correct Answer!")
		n = n + 1
	elif ans == 5:
		print("You Have Chosen Lifeline 50:50 !")
		print("Two Incorrect Options Will Be Randomly Eliminated")
		opt = [a[n], b[n]]
		random.shuffle(opt)
		print("The Remaining Options Are:-")
		x = 0
		while x <= 1:
			print(x + 1, opt[x])
			x=x+1
		spl_ans = input("Press Keys 1-2 to select an Option")
		if str(opt[int(spl_ans) - 1]) == str(a[n]):
			print("Correct Answer!")
			n = n + 1
		else:
			print("Wrong Answer!")
			# BREAK LOOP
			# n = n + 100
			break
	elif ans == 6:
		print("You Have Chosen the Lifeline : PASS!")
		moveon = input("Press Any Key to Move On to the Next Question")
		n = n + 1
	elif int(ans) <= 4:
		print("Wrong Answer!")
		# BREAK LOOP
		# n = n + 100
		break
	else:
		print("Please Only Press Keys 1-6!")

if n==10:
	print("You Answered All Ten Questions Correctly!")
	print("You May Now Leave With Your Jackpot Prize of 7.5 Crore!")
else :
	print("Sorry, You Have Been Disqualified")
