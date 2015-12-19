import urllib.request
import pickle

# get the banner
banner = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
# decipher with pickle
data = pickle.loads(banner)
# data consists of instructions for lines
for lines in data:
    # empty line
    line = ""
    # for each piece in a line: multiply symbol by its number
    for piece in lines:
        line += piece[0] * piece[1]
    # print the line
    print(line)
