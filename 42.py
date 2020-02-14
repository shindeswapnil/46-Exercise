'''
A sentence splitter is a program capable of splitting a text into sentences. The standard set of heuristics for sentence splitting includes (but isn't limited to) the following rules:

Sentence boundaries occur at one of "." (periods), "?" or "!", except that

    Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
    Periods followed by a digit with no intervening whitespace are not sentence boundaries.
    Periods followed by whitespace and then an upper case letter, but preceded by any of a short list of titles are not sentence boundaries. Sample titles include Mr., Mrs., Dr., and so on.
    Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries (for example, www.aptex.com, or e.g).
    Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not sentence boundaries.

Your task here is to write a program that given the name of a text file is able to write its content with each sentence on a separate line. Test your program with the following short text: Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't. The result should be:

Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
Did he mind?
Adam Jones Jr. thinks he didn't.
In any case, this isn't true...
Well, with a probability of .9 it isn't.
'''

import re
def textToSentence(filename):
	f=open(filename)
	filecontent=f.read()

	sentences=re.sub(r'\n','',filecontent) #Removing all pre new lines

	sentences=re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])',r'.\n\1',sentences)# adding new line after period which not part of the the Mr.or Mrs. or DR.

 #	sentences = re.sub(r'\!\s','!\n',sentences)
 	
	sentences=re.sub(r'\?\s','?\n',sentences) # adding new line matching of '?'

	print(sentences)


textToSentence('ex42.txt')



