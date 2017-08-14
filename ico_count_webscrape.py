from lxml import html
import requests
import pyodbc

website = "https://www.icoalert.com" ##define the website to pull the info from (currently ICO site ICO Alert)

page = requests.get(website) ##getting the info from the site in question
tree = html.fromstring(page.content) ##putting the information into a tree structure

##now we need to create a tree of ICO's
icos_raw = tree.xpath('count(//div[@class="ico-wrap"]/text())') ##This defines what I am pulling, and what to do with it, in this case count

icos = (float(icos_raw))/3 ##There are 3 Column headers that also use the Div Class "ICO-Wrap", and each ICO Wrap counts for 3 in the count for some reason, so here I am manually removing the 3 headers and dividing by 3

print ("Rough ICO's: "), icos ##Test output

##The Value we transfer over to DB is "icos"

### Now Connect to DB and Send Data There STILL IN PROGRESS pyodbc doc and ODBC functions