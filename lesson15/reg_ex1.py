import re

if __name__ == '__main__':
    ret_val = re.search("a", "cat")
    print(type(ret_val))
    print(ret_val)
    print(re.search("a", "cccccat"))
    print(re.search("a", "sun"))
    print(re.search("[0-9]", "fgdfhhgdg6dfgdg"))
    print(re.search("[0-9][a-z]", "sun67a"))
    print(re.search("[A-Z][0-9][a-z]", "sun67a"))
    print(re.search("[A-Za-z][0-9][0-9]", "sun67a"))
    print(re.search("[A-Za-z][0-9]_[0-9]", "sun6_7a"))
    print(re.search("cat|dog", "cat or dog"))
    print(re.findall("cat|dog", "cat or dog"))
    # + * ? {}
    print(re.search("[0-9] +[a-z]", "$Sfs3      rsdfsdf"))
    print(re.search(" +", "$Sfs3      rsdfsdf"))
    print(re.search("ca+t", "caaaat"))
    print(re.search("ca+t", "ct"))
    print(re.search("ca*t", "caaaaat"))
    print(re.search("ca*t", "ct"))
    print(re.search("ca?t", "ct"))
    print(re.search("ca?t", "cat"))
    print(re.search("ca?t", "caat"))
    print(re.search("ca{3,6}t", "caaaat"))
    print(re.search("ca{3}t", "caaaat"))
    print(re.search("ca{3,}t", "caaaat"))
    print(re.search("ca{,6}t", "caaaat"))
    print(re.search("(cat)+","erercatcatcatggg"))
    print(re.search("(cat)+", "erercatcatcatggg"))
    # cats vs/or/and dogs
    print(re.search("cats (vs|or|and) dogs", "apples cats or dogs fhskd"))
    print(re.search("[0-9].*[0-9]", "hfjs4sdj65$4"))
    print(re.findall("_[a-z]+", "hi _sun sky _cloud"))
    print(re.match("_[a-z]+", "_sun sky _cloud"))
    print(re.match("^_[a-z]+$", "_sun"))
    print(re.match("[^a-zA-Z0-9]+", "$#^"))

    # escape char
    print(re.search("cat+", "cattttt"))
    print(re.search("\+", "c+tglls"))
    print(re.search("\++", "c++++"))

    #

    """Group extraction"""

    pattern = r"\w+ (and|or) \w+"
    #
    m = re.match(pattern, "fred and barney are here")
    #
    print(m)
    #
    pattern = r"(\w+) (and|or) (\w+)"
    #
    m = re.match(pattern, "fred and barney are here")
    #
    print(m.group())
    #
    print(m.group(1))
    #
    print(m.group(2))
    #
    print(m.group(3))
    #
    # m.groups()
    #
    # m.group(4)
    #
    # pattern = "([\w]+) (and|or) ([\w]+)"
    #
    # m = re.match(pattern, "fred and barney are here")
    #
    # m.groups()
    #
    # m.group(2, 3, 4, 1, 1, 1)
    #
    m = re.match(pattern=r"(\w+)@(\w+)\.([a-z]+)", string="your_name@gmail.com")
    #
    print(m.group(1)) # returns 'your_name'
    print(m.group(2)) # returns 'gmail'
    print(m.group(3)) # returns 'com'
    #
    # m.group(2)
    #
    # m.group(0)


#
pattern = r"(\w+) (and|or) (\w+)"
#
match = re.search(pattern, "both Alice AND Bob arrived to the show")
#
print(match)
#
match = re.search(pattern, "both Alice AND Bob arrived to the show", re.IGNORECASE)
#
print(match)
#
pattern = r"^[\w]+ (and|or) [\w]+"
#
my_text = '''
Alice arrived to the show.
Next time don't forget to call David or Moshe!
Alice and Bob arrived to the show.
'''

# match = re.search(pattern, my_text)
#
# print(match)
#
match = re.search(pattern, my_text, re.MULTILINE)
#
print(match)

match = re.search(pattern, my_text, re.MULTILINE | re.IGNORECASE)


