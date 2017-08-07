import requests
from bs4 import BeautifulSoup
import operator

def start(url):
	word_list=[] #empty list
	source_code=requests.get(url).text #to connect and parse source_code in text format
	soup=BeautifulSoup(source_code, "html.parser") #scrapping the words we need
	for post_text in soup.findAll('div',{'class': 'Message'}): #class is the identifier of the anchor tags with names post-tag
		content=post_text.get_text() #to get only the important text by get_text() leaving behind the html codes.
		words=content.lower().split() #to get no duplicate results and split the string into words and in lowercase
		for each_word in words:
			word_list.append(each_word)
	clean_up_list(word_list)
	
def clean_up_list(word_list):
	clean_word_list=[] #list to add words without special symbols
	for word in word_list:
		symbols="!@#$%^&*()_-+{}:;\"<>?/,.=╗'" #list of special symbols
		for i in range(0,len(symbols)):
			word=word.replace(symbols[i],"") #to replace special symbols
		if len(word)>0: #if lenth of word is less than 0 then it is not a word
			print(word)
			clean_word_list.append(word) #add words to list
start('https://forums.digitalspy.com/discussion/2235016/in-large-debt-tell-my-parents')