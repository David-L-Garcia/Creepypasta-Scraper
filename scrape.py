import requests
import random
from bs4 import BeautifulSoup


def main():
	format()

def format():#makes the format look good-ish
	print "\n////////////////////////////////////////"
	print "/Welcome to the Creepypasta finder!/////"
	print "/Type in whatever creepypasta you want//"
	print "/to read and I'll get it for you!///////"
	print "/Type quit if you want to leave/////////"
	print "/Don't blame me if you can't sleep!/////"
	print "////////////////////////////////////////\n\n"
	x = userInput()
	url = getURL(x)
	if(check(url)):
		print "\n"
		sass()
		print "\n"
		print "Without further adeu, I present: " + x
		print "\n"
		print "////////////////////////////////////////\n\n"
		spooky(url)
	else:
		print "Does not exist"
	
def check(url):#Validates the address exists
	if url is None:
		return False
	return True
	
def userInput(): #This gets the user input and checks if it exists
	web = raw_input("What Creepypasta do you want?\n")
	return web

def getURL(web):
	web.replace(" ","_")
	url = 'http://creepypasta.wikia.com/wiki/' + web
	return url

def spooky(url): #This uses the input and prints out the desired creepypasta 
	response = requests.get(url)
	xml = response.content

	soup = BeautifulSoup(xml,"lxml")
	yum = soup.find("div",{"id": "mw-content-text"}).findAll('p')
	for line in range(len(yum) - 1):
		print (yum[line].getText().encode("utf-8") + "\n")

def sass(): #This is just a random response generator
	x = random.randint(1,4)
	if(x == 1):
		print "Oh... you want that one?"
	elif(x == 2):
		print "I love that one!"
	else:
		print "Coming right up!"
main()

