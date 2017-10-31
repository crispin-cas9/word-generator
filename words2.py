# caemattos word generator
# ae = ash

import random as rd
from numpy.random import choice


# converts weight numbers so that they sum to 1

def convert(list):
	newlist = []
	for n in list:
		new = n/float(sum(list))
		newlist.append(new)
	return newlist


def gen_syll():
		
	vowels = ["a", "ae", "e", "i", "o", "u"]
	
	# I don't necessary classify consonants correctly here -- for example, LL is not a fricative and Y is, but I'm classifying them this way to make it all easier for myself
	# the numbers in the dict are weights
	
	consonantdict = {"d": ["fric", 5], "dd": ["fric", 4], "c": ["stop", 6], "cc": ["stop", 3], "f": ["fric", 5], "ff": ["fric", 3], "h": ["other", 3], "hh": ["other", 2], "l": ["other", 4], "ll": ["fric", 4], "m": ["other", 5], "n": ["other", 6], "nn": ["other", 2], "p": ["stop", 3], "pp": ["stop", 2], "r": ["fric", 5], "rr": ["other", 2], "s": ["fric", 5], "ss": ["fric", 3], "t": ["stop", 5], "tt": ["stop", 3], "y": ["other", 4], "yy": ["other", 2], "z": ["fric", 4], "zz": ["fric", 3]}
	
	consonants = consonantdict.keys()
	weights = []
	fricdict = {}
	stopdict = {}
	fricweights = []
	stopweights = []
	
	# creates separate lists for fricatives and stops
	
	for letter in sorted(consonantdict.keys()):
		weights.append(consonantdict[letter][1])
		if consonantdict[letter][0] == "fric":
			fricdict.update({letter: consonantdict[letter][1]})
		if consonantdict[letter][0] == "stop":
			stopdict.update({letter: consonantdict[letter][1]})
	
	weights = convert(weights)
		
	syll = ""

	
	# onset
	
	# are there two consonants in the onset? picking from 6 numbers to make the probability of 2 consonants smaller
	onset_num = rd.randint(1,6)
	
	onset_num = 1
	
	# if there are 2 letters in the onset, there are certain rules (described above) about what they can be
		
	if onset_num == 2:
		
		for key in sorted(fricdict.keys()):
			if key not in no:
				fricweights.append(fricdict[key])
		
		fricweights = convert(fricweights)
		
		fric = choice(fricdict.keys(), p=fricweights)
		
		filtered = [letter for letter in stopdict.keys() if (len(letter) == len(fric) or letter == "r")]
		
		for key in sorted(stopdict.keys()):
			if key in filtered:
				stopweights.append(stopdict[key])
				
		stopweights = convert(stopweights)
			
		syll = syll + fric + choice(filtered, p=stopweights)

	else:
				
		startweights = []
		
		for key in consonants:
			startweights.append(consonantdict[key][1])
		
		startweights = convert(startweights)
		
		syll = syll + choice(consonants, p=startweights)
	
	# nucleus
	
	syll = syll + rd.choice(vowels)
	
	
	return syll


# generates a word made from syllables

def generate():
 	
 	word = ""
 	syllnum = rd.randint(1,3)
 	
 	for x in range(syllnum):
 		word = word + gen_syll()
 	
 	return word


wordlist = []

for y in range(0,11):
	wordlist.append(generate())

print wordlist
