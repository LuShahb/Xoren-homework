import sys

Sherlock = open(sys.argv[1], 'r')

my_str = Sherlock.read()

 
Sherlock.close()


for i in "abcdefghijklmnopqrstuvwxz":
    print("%s: %s" % (i, my_str.lower().count(i)))