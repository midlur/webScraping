from bs4 import BeautifulSoup
import requests
re = requests.get("http://www.imdb.com/chart/top");  #to get contents from the URL
data=re.text  #converting it to text
soup=BeautifulSoup(data)  #passing as object

titles = soup.findAll("td", "titleColumn")  #extracting from td the class titleColumn
#print titles[0]
count =0  #counter to check for 10 movies only
for title in titles:
        # First hyperlink is the title
        name = title.find("a").text    # extracts movie name
	print name   #prints name extracted
	count = count + 1
	if(count==10):  # tocheck for only top 10 movies
		break
