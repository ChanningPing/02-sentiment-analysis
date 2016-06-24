# -*- coding:utf-8 -*-
from os.path import os, join, dirname
from dotenv import load_dotenv
import tweepy


senti_dict = { }

with open('AFINN/AFINN-111.txt','r') as fhand:#read this file into python memory
	for line in fhand:
		k,v=line.rstrip().split('\t')
		#line = line.strip()#remove the white
		#columns=line.split('\t')#store the 2 in a list
		#senti_dict[columns[0]]=columns[1]
		senti_dict[k]=v

dotenv_path=join(dirname(__file__),'.env')
load_dotenv(dotenv_path)

auth=tweepy.OAuthHandler(os.environ['consumer_key'],os.environ['consumer_secret'])
auth.set_access_token(os.environ['access_token'],os.environ['access_token_secret'])

client=tweepy.API(auth)
results=client.search(q='hilary cliton',lang='en')

for result in results:
	sentence=result.text
	senti_score=0
	sentence_lowered=sentence.lower().encode('utf-8')
	for (key,value) in senti_dict.items():
		if key  in sentence_lowered:
			senti_score+=int(value)
	print (sentence_lowered+'|'+ str(senti_score))




print (client)

'''
sentence = raw_input('Enter text: ')
sentence_lowered=sentence.lower()
#print (sentence_lowered)
senti_score=0
for (key,value) in senti_dict.items():
	if key  in sentence_lowered:
		senti_score+=int(value)

print('The sentiment score of the sentence %s  is %d' % (sentence_lowered,senti_score))
'''
