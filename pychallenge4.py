import urllib.request
import re

# common for all urls
static_html = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

# start with this url
buff = urllib.request.urlopen(static_html + '1417')

# our regexes
p = re.compile('next nothing is \d+')
q = re.compile('\d+')

# looping through the urls
while True:
    # read the content
    content = str(buff.read())
    # find a match
    match = p.findall(content)
    # if the generic formula cannot be found: break loop
    if match == []:
        break
    # join our finding from a list to a string
    match = ''.join(match)
    # give some output
    print(match)
    # extract the numbers for the next nothing
    nothing = q.findall(match)
    # join our finding from a list to a string
    nothing = ''.join(nothing)
    # the next url we want to check
    html = static_html + nothing
    # get its content
    buff = urllib.request.urlopen(html)
# when loop stops: something interesting happened!
print("loop stopped here: ")
print(content)
