import os
import time


temp = open("ref.txt", "r")
ref = temp.read()


def parser(inputfile):
    worddict = {}
    wordlist = []

    tempstring = ""
    tempdictside1 = ""
    tempdictside2 = ""

    for x in range(0, len(ref)-1):
        # print tempstring.rsplit('->')
        if (ref[x] != '\n'):
            # and (ref[x] + ref[x-1] != '\n')
            tempstring += ref[x]
        else:
            tempdictside1 = tempstring.rsplit('->')[0]
            tempdictside2 = tempstring.rsplit('->')[1]
            tempstring = ''
            worddict.update({tempdictside1: tempdictside2})
            wordlist.append(tempdictside1)

    print "Done parsing - Grep time!"
    # print wordlist
    return wordlist


def grep(worddict):
    for x in worddict:
        # print x
        print "searching for " + str(x)
        os.system("grep -iInr --exclude ref.txt " + str(x))


def fgrep(worddict):
    for x in worddict:
        # print x
        print "searching for " + str(x)
        os.system("LC_ALL=C grep -iFInr --exclude ref.txt " + str(x))
grep_time = time.time()
grep(parser(ref))
grep_total_time = time.time() - grep_time
# fgrep_time = time.time()
# fgrep(parser(ref))
# fgrep_total_time = time.time() - fgrep_time

print "time took to grep: %s seconds", grep_total_time
# os.system("export ")
# print "time took to fgrep: %s seconds", fgrep_total_time
