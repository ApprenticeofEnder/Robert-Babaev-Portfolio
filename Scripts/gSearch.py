#! python3 
import webbrowser, sys
address = str()
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
webbrowser.open('http://www.google.com/search?q=' + address)
