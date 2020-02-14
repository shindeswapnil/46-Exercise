'''
An alternade is a word in which its letters, taken alternatively in a strict sequence, and used in the same order as
the original word, make up at least two other words. All letters must be used, but the smaller words are not necessarily
of the same length. For example, a word with seven letters where every second letter is used will produce a four-letter
word and a three-letter word. Here are two examples:

  "board": makes "bad" and "or".
  "waists": makes "wit" and "ass".

Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that goes through each word in
the list and tries to make two smaller words using every second letter. The smaller words must also be members of the list.
 Print the words to the screen in the above fashion.
'''

def alternade(filename):
    f=open(filename)
    word_list=[]
    for line in f:
        word_list.append(line.rstrip())
    print(word_list)

    for word in word_list:
        new_list=[]
        for i in range(len(word)):
            new_word=''.join(word[i::2])
            if new_word in word_list and len(new_word)>1:
                new_list.append(new_word)
        c=0
        if len(new_list)>0:
           print('"{}" : makes '.format(word),end='')
        for w in new_list:
            c+=1
            print('"{}"'.format(w),end='')
            if c<(len(new_list)):
                print(' and ',end='')

        if len(new_list)>0:
          print('')
        new_list=[]

alternade('unixdict.txt')





