print 'Script to brute force'

from optparse import OptionParser
import sys
import Utilities
from SSH import SSH

usage = '%s [-h hostname] [-u username] [-p password]' % sys.argv[0]
parser = OptionParser(version='SSH Brute Forcer',usage=usage,add_help_option=False)
parser.add_option("-h",dest="hostname",help="name of host",metavar="HOST")
parser.add_option("-u",dest="username",help="name of user")
parser.add_option("-p",dest="password",help="user password")
parser.add_option("-P","--port",dest="portnumber",help="port number",default=22)

(option,args) = parser.parse_args()

#print Utilities.fileToList('password')
#print Utilities.fileToTuple('targets')

#SSH connection
print option.portnumber
conn = SSH(option.username,option.password,option.hostname,option.portnumber,5)
conn.connect()

