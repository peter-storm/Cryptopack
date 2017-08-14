from lxml import html
import requests

website = "https://www.icoalert.com" ##define the website to pull the info from (currently ICO site ICO Alert)

page = requests.get(website) ##getting the info from the site in question
tree = html.fromstring(page.content) ##putting the information into a tree structure

##now we need to create a tree of ICO's
icos = tree.xpath('//div[@class="ico-links"]/text()')

print "ICO's: ", icos