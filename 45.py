'''
A certain childrens game involves starting with a word in a particular category. Each participant in turn says a word,
but that word must begin with the final letter of the previous word. Once a word has been given, it cannot be repeated.
If an opponent cannot give a word in the category, they fall out of the game. For example, with "animals" as the category,

Child 1: dog
Child 2: goldfish
Child 1: hippopotamus
Child 2: snake
...

Your task in this exercise is as follows: Take the following selection of 70 English Pokemon names (extracted from Wikipedia's
list of Pokemon) and generate the/a sequence with the highest possible number of Pokemon names where the subsequent name starts
with the final letter of the preceding name. No Pokemon name is to be repeated.

audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
cresselia croagunk darmanitan deino emboar emolga exeggcute gabite
girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan
kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking
sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask
'''

import re

#function which tells you next word available
#or not which is is start with last letter of the
#previous name
def next_name(lastletter,namelist):
    for index,name in enumerate(namelist):
        if name.startswith(lastletter):
            return index
    return False

def lastLetter_firstLetter(filename):
    f=open(filename)
    names=re.findall(r'\w+',f.read()) #reading file word wise

    longest_series, current_series=[],[]


    for name in names:
        current_name=name #taking one by one name from the list
        current_series.append(current_name)

        namelist=names[:] #copying original to new list to for operations
        namelist.pop(namelist.index(current_name))#deleteing word from new list to check next words

        index=next_name(current_name[-1],namelist) #getting next word's index

        while index is not False:
            current_name=namelist[index]
            current_series.append(current_name) #adding name to current series which is starting from last letter of the previous name
            namelist.pop(index)# deleting that name from  that new list
            index=next_name(current_name[-1],namelist)#finding next word is available  or not

        if len(current_series) > len(longest_series):
            longest_series=current_series

        current_series=[] #making current series NULL for next operation

    print(longest_series)


lastLetter_firstLetter('pokemon.txt')
