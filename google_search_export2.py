# Google Search Results Scraper
# make sure to install the following libraries:
# pip install beautifulsoup4
# pip install google
import numpy as np

count = 0
try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

# to search
#query = input('what do you want to search?: ')
#result = input('what is the max number of search results?: ')
#resultnum = int(result)
query = input('what do you want to search?: ')
res = input('what is the max number of search results?: ')
maxresults = int(res)

word = query.split()
print(word)

lst = list()
count = 0
results = 0
for i in word:
	for j in search(word[count], tld="com", num=maxresults, stop=maxresults, pause=3):
		lst.append(j)
		results = results + 1
		print(j)

	print('"'+word[count]+'" search results:', results)
	results = 0
	count = count + 1
	continue
print(lst)

arr = np.array(lst)
# Save Numpy array to csv
np.savetxt('array2.csv', arr, delimiter =",", fmt = "%s")
