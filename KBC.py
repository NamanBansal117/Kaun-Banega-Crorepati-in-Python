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
		"Where is the largest mountain of the Solar System located",
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
print("1 : 50:50 : Randomly Eliminates Two Incorrect Options")
print("2 : Pass : Allows You to Skip the Question")
print("You will be told how many times you used these Lifelines at the end.")

print('\n')
start = input("Press Enter to begin\n")
n = 0
fcount=0
pcount=0
while n < len(a):
	if n==3 :
		print("First Checkpoint Reached!\nNext Checkpoint at Q6")
	elif n==6:
		print("Second Checkpoint Reached!\nNext Checkpoint at Q9")
	elif n==9:
		print("Last Checkpoint Reached!\nYou can now leave with your prize of 2 crore or move on to the Jackpot Question.\nAnswer correctly to win 10 crore\nAnswer wrongly and you go back home with nothing")
		time.sleep(1)
		jchoice=input(" 1 to move on to the Jackpot\n 2 to leave with just two crore")
	elif n==10:
		print("JACKPOT QUESTION")
	elif n>6:
		print("Last Checkpoint : Q6")
	elif n>3:
		print("Last Checkpoint : Q3")
	else :
		print("First Checkpoint at Q3")
	time.sleep(1)
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
	ans = input("\nPress Keys 1-4 to select an Option\nPress 5 for 50:50\nPress 6 for PASS\n")
	if int(ans) == 5:
		fcount=fcount+1
		print("You Have Chosen Lifeline 50:50 !")
		print("Two Incorrect Options Will Be Randomly Eliminated")
		opt = [a[n], b[n]]
		random.shuffle(opt)
		print("The Remaining Options Are:-")
		x = 0
		while x <= 1:
			print(x + 1,":", opt[x])
			x=x+1
		spl_ans = input("Press Keys 1-2 to select an Option")
		if str(opt[int(spl_ans) - 1]) == str(a[n]):
			print("Correct Answer!")
			n = n + 1
		else:
			print("Wrong Answer!")
			break
	elif int(ans) == 6 :
		pcount=pcount+1
		print("You Have Chosen the Lifeline : PASS!")
		moveon = input("Press Enter to Move On to the Next Question\n")
		n = n + 1
	elif int(ans)<=len(opt):
		if str(opt[int(ans) - 1]) == str(a[n]):
			print("Correct Answer!")
			n = n + 1
		elif int(ans) <= 4 and int(ans) > 0:
			print("Wrong Answer!")
			break
	else:
		print("Please Only Press Keys 1-6!")

time.sleep(1)
if n==10:
	if pcount>1 or fcount>1 :
		print("That was the last question!")
		print("You had to use 50:50", fcount, "times")
		print("You had to use PASS", pcount, "times")
	else :
		print("You answered all questions correctly!")
		print("You may now leave with your Jackpot Prize of 10 Crores !")
elif n>=9:
	print("By losing the Jackpot, you have lost all of your winnings.\nYou may now leave with NOTHING")
elif n>=6:
	print("The last checkpoint was at Q6\nYou may now leave with a grand total of 5 lakh rupees")
elif n>=3:
	print("The last checkpoint was at Q9\nYou may now leave with a grand total of 1 lakh rupees")
else :
	print("Sorry, You Have Been Disqualified")
