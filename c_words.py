# caemattos word generator
# ae = ash

# some goals:
# make it less likely for one sound to be repeated throughout a word

# important! in a syllable: onset = starting consonants, nucleus = middle vowels, coda = ending consonants

import random as rd
from numpy.random import choice

# converts weight numbers so that they sum to 1!! doesn't work yet though whoops

def convert(list):
	newlist = []
	for n in list:
		new = n/float(sum(list))
		newlist.append(new)
	return newlist


def gen_syll(prevcn):
	
	# prevcn stands for previous coda number
	
	vowels = ["a", "ae", "e", "i", "o", "u"]
	
	# I don't necessary classify consonants correctly here -- for example, LL is not a fricative and Y is, but I'm classifying them this way to make it all easier for myself
	
	consonantdict = {"d": ["fric", 5], "dd": ["fric", 4], "c": ["stop", 6], "cc": ["stop", 3], "f": ["fric", 5], "ff": ["fric", 3], "h": ["other", 3], "hh": ["other", 2], "l": ["other", 4], "ll": ["fric", 4], "m": ["other", 5], "n": ["other", 6], "nn": ["other", 2], "p": ["stop", 3], "pp": ["stop", 2], "r": ["fric", 5], "rr": ["other", 2], "s": ["fric", 5], "ss": ["fric", 3], "t": ["stop", 5], "tt": ["stop", 3], "y": ["other", 4], "yy": ["other", 2], "z": ["fric", 4], "zz": ["fric", 3]}
	
	consonants = consonantdict.keys()
	weights = []
	fricdict = {}
	stopdict = {}
	fricweights = []
	stopweights = []
	
	for letter in sorted(consonantdict.keys()):
		weights.append(consonantdict[letter][1])
		if consonantdict[letter][0] == "fric":
			fricdict.update({letter: consonantdict[letter][1]})
		if consonantdict[letter][0] == "stop":
			stopdict.update({letter: consonantdict[letter][1]})
	
	weights = convert(weights)
		
	syll = ""

	# is there an onset? 0 = no; 1 = yes. if there were 2 consonants in the previous syllable's coda, there will be no onset in this coda
	
	if prevcn == 2:
		is_onset = 0
	else:
		is_onset = rd.randint(0,1)
	
	# are there two consonants in the coda? picking from 6 numbers to make the probability of 2 consonants smaller
	coda_num = rd.randint(1,6)

	if is_onset == 1:
		syll = syll + choice(consonants, p=weights)
	
	# nucleus
	
	syll = syll + rd.choice(vowels)
	
	# coda
	# the letters in the list "no" cannot be present in the coda
	# if there are 2 letters in the coda, there are certain rules about what they can be
	
	no = ["h", "hh", "y", "yy"]
	
	if coda_num == 2:
		
		codanum = 2
		
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
		
		codanum = 1
		
		endcons = []
		endweights = []
		
		for letter in sorted(consonantdict.keys()):
			if letter not in no:
				endcons.append(letter)
		
		for key in sorted(consonantdict.keys()):
			if key in endcons:
				endweights.append(consonantdict[key][1])
		
		endweights = convert(endweights)
		
		syll = syll + choice(endcons, p=endweights)
	
	return [syll, codanum]


def generate():
	
	codanum = 1
	word = ""
	syllnum = rd.randint(1,3)
	
	for x in range(syllnum):
		
		output = gen_syll(codanum)
		
		syll = output[0]
		codanum = output[1]
		
		word = word + syll
			
	return word


for y in range(0,11):
	print generate()
