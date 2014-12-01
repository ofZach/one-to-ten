
import urllib
from bs4 import BeautifulSoup  
from subprocess import call
from Levenshtein import distance
import string
import re
import os

allTheLetters = string.lowercase
lookWords = []


# note this script hits a website kind of hard.  
# I'd be happy to find a better database of phrases to use or a more official API

def loadPage( urlToOpen, word ):
	print "loading " + urlToOpen
	page = urllib.urlopen(urlToOpen).read()
	soup = BeautifulSoup(page)
	aTags =  soup.find_all('a')
	for aTag in aTags:
		if word in aTag.text:
			#print aTag.text
			wordToAdd = aTag.text;
			if "Additional searches for"  not in wordToAdd:
				lookWords.append(wordToAdd)
		if ">>" in aTag.text:
			#print aTag.text
			url = "http://www.onelook.com" +  aTag["href"]
			loadPage(url, word)

def grabWords( word ):

	for letter in allTheLetters:
		url = "http://www.onelook.com/?w=*" + letter + " " + word + "&ls=a"
		loadPage(url, word)

	for letter in allTheLetters:
		url = "http://www.onelook.com/?w=" + word + " " + letter + "*&ls=a"
		loadPage(url, word)

	url = "http://www.onelook.com/?w=* " + word + " *&ls=a"
	loadPage(url, word)



chapters = ["one","two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

# for chapter in chapters: 

# 	lookWords = []

# 	wordToFind = chapter
# 	grabWords(wordToFind)


# 	f = open(chapter + '_unsorted.txt','w')
# 	for word in lookWords:
# 		f.write(word.encode('utf-8') + '\n')
# 	f.close()
	
# 	lookPhrasesStoredByDistance = []

# 	currentWord = wordToFind

# 	lookWordsSet = set(lookWords)


# 	while len(lookWordsSet) > 0:

# 		smallestDiffWord = ""
# 		smallestDiff = 1000000
		
# 		for word in lookWordsSet:
# 			edit_dist = distance(currentWord.encode('utf-8'), word.encode('utf-8'))
# 			if smallestDiff > edit_dist:
# 				smallestDiffWord = word
# 				smallestDiff = edit_dist
		
# 		currentWord = smallestDiffWord
# 		if smallestDiffWord in lookWordsSet: lookWordsSet.remove(smallestDiffWord)
# 		lookPhrasesStoredByDistance.append(smallestDiffWord)
# 		#print smallestDiffWord


# 	outputFile = open(chapter + ".txt", 'w')
# 	outputFile.write(chapter + "\n")

# 	for phrase in lookPhrasesStoredByDistance:
# 		outputFile.write(phrase.encode('utf-8'))
# 		outputFile.write("\n")

# 	outputFile.close()


outputFile = open("book.txt", 'w')
for chapter in chapters: 
	outputFile.write("\n\n\n\n\n\n\n\n\n");
	outputFile.write(chapter);
	outputFile.write("\n\n\n\n\n\n\n\n\n");

	f = open(chapter + ".txt")
	lines = f.readlines()
	for line in lines: 
		outputFile.write("\t")
		outputFile.write(line);
	f.close()
outputFile.close()

