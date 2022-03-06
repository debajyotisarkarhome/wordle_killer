from fileinput import close
import sqlite3

def check_word(word, letterCache):
    for letter in word:
        if letter in letterCache:
            return -1
    letterCache.extend(list(word))
    return 1

alphabet="a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
letterCountedList=[]
uniqueLettersList=[]

letterCache=[]
selectionList=[]

conn = sqlite3.connect('wordNet.db')
qr=conn.execute("SELECT lemma FROM words")
wordlist=qr.fetchall()
for word in wordlist:
    word=word[0]
    if word.find(" ")==-1 and len(word)==5 and word.isalpha():
        letterCountedList.append(word)
conn.close()

for word in letterCountedList:
    uniqueLettersList.append(word) if len(list(set(list(word))))==len(list(word)) else None

closeCursor=0
for _ in range(0,5):
    found=0
    if selectionList==[]:
        letterCache.extend(list(uniqueLettersList[closeCursor]))
        selectionList.append(uniqueLettersList[closeCursor])
        closeCursor+=1
    else:       
        while found==0 and closeCursor<len(uniqueLettersList):
            word=uniqueLettersList[closeCursor]
            if check_word(word, letterCache)!=-1:
                selectionList.append(word)
                closeCursor+=1
                found=1
                letterCache.remove("e")
            else:
                closeCursor+=1


print(selectionList)
