# -*- coding:utf-8 -*-

senti_dict = { }

fhand=open('AFINN/AFINN-111.txt','r')#read this file into python memory
for line in fhand:
	line = line.strip()#remove the white
	columns=line.split('\t')#store the 2 in a list
	senti_dict[columns[0]]=columns[1]

sentence = raw_input('Enter text: ')
sentence_lowered=sentence.lower()
#print (sentence_lowered)
senti_score=0
for (key,value) in senti_dict.items():
	if key  in sentence_lowered:
		senti_score+=int(value)

print('The sentiment score of the sentence %s  is %d' % (sentence_lowered,senti_score))

