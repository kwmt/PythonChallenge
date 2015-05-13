 
import urllib
from xmlrpclib import ServerProxy
 
 
print urllib.urlopen("http://www.pythonchallenge.com/pc/return/evil4.jpg").read()


server = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
#print server.system.listMethods()

print server.system.listMethods()

# print server.phone("Bert")