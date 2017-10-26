# caemattos word generator
# ae = ash

# THE RULES
# A doubled letter represents a different sound than a single letter
# In a syllable: onset = starting consonants, nucleus = middle vowels, coda = ending consonants
# Onset must be 1 sound (or there can be no onset)
# Coda is most often 1 sound and cannot be more than 2 sounds
# Pretty much every non-inflected word ends in a consonant
# Fricative (as well as LL and R) + stop is allowed in the coda
# Neither H nor Y are allowed in the coda


import random as rd
from numpy.random import choice


# converts weight numbers so that they sum to 1

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

	# is there an onset? 0 = no; 1 = yes. if there were 2 consonants in the previous syllable's coda, there will be no onset in this coda
	
	if prevcn == 2:
		is_onset = 0
	else:
		is_onset = rd.randint(0,1)

	if is_onset == 1:
		onset = choice(consonants, p=weights)
		syll = syll + onset
		consonantdict[onset][1] = 0.5
	
	# nucleus
	
	syll = syll + rd.choice(vowels)
	
	# coda
	
	# are there two consonants in the coda? picking from 6 numbers to make the probability of 2 consonants smaller
	coda_num = rd.randint(1,6)
	
	# the letters in the list "no" cannot be present in the coda
	# if there are 2 letters in the coda, there are certain rules (described above) about what they can be
	
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


# generates a word made from syllables
# also tells the syllable it's generating about the coda of the previous syllable

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


wordlist = []

for y in range(0,11):
	wordlist.append(generate())

print wordlist
