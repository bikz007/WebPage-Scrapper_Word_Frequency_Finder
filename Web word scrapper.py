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
			clean_word_list.append(word) #add words to list
	create_dictionary(clean_word_list)
def create_dictionary(clean_word_list):
	word_count={} #a dictionary where we will store the words and their frequencies as key
	for word in clean_word_list :
		if word in word_count: #if the word is already present 
			word_count[word]+=1 #increase its no. of occurance
		else:
			word_count[word]=1 #keep it in
	#to sort according to frequencies
	for key,value in sorted(word_count.items(),key=operator.itemgetter(1)): #in a dictionary key is the word and value will be its frequency,so getting key from dictionary and specifying to sort according to value
		print(key,value)
start('https://forums.digitalspy.com/discussion/2235016/in-large-debt-tell-my-parents')
