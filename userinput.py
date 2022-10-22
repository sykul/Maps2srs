from optparse import OptionParser
def Parse_Options():
    parser = OptionParser()
    parser.add_option("-t", "--town", action="store", type="string", dest="town", help="Hi")
    (options, args) = parser.parse_args()

    print("The town is {0}".format(options.town))
