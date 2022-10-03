from optparse import OptionParser
parser = OptionParser()
parser.add_option("-t", "--town", dest="town",
        help="Hi")

(options, args) = parser.parse_args()
print(f"{0}".format(options.town))
