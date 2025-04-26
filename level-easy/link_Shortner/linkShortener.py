import pyshorteners
import pyshorteners.shorteners

#input the link:
link = input('enter the link: ')

#creating a shortener object
shortener = pyshorteners.Shortener()

#shorten the link using TinyURL
shorten_link = shortener.tinyurl.short(link)

#printing the output
print('shorten link: ', shorten_link)