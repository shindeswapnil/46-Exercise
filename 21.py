#Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. 
#Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").

def char_freq(s):
	freq={k:0 for k in s}
	for ch in s:
		freq[ch]=freq[ch]+1
	return freq

print(char_freq("abbabcbdbabdbdbabababcbcbab"))
