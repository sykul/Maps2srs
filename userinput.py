from optparse import OptionParser
parser = OptionParser()
parser.add_option("-t", "--town", action="store", type="string", dest="town", help="Hi")
(options, args) = parser.parse_args()

print("{0}".format(options.town))
