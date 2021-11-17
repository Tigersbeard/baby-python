# Open textfile and convert into string
# strip leading word, spaces and backslashes,
# and remove integers, spaces and linebreaks

with open('preproinsulin-seq.txt') as file:
    preproinsulinseqclean = file.read().strip('ORIGIN //')\
    .replace(' ','').replace('1','').replace('6','').replace('\n','')

# confirm lowercase and correct string length

if len (preproinsulinseqclean) == 110:
    if preproinsulinseqclean.islower() == True:
        print ("good")

# output string to new textfile, conditional on the above checks

        textfile = open('preproinsulin-seq-clean.txt', 'w')
        textfile.write(preproinsulinseqclean)
        textfile.close()

# Open lsinsulin-seq-clean.txt file, containing string of 1-24
# characters and check length = 24

lsinsulinseqclean = preproinsulinseqclean[0:24]
if len (lsinsulinseqclean) == 24:
    print ("good")
    textfile = open('lsinsulin-seq-clean.txt', 'w')
    textfile.write(lsinsulinseqclean)
    textfile.close()

# binsulin-seq-clean.txt 25-54  30

binsulinseqclean = preproinsulinseqclean[24:54]
if len (binsulinseqclean) == 30:
    print ("good")
    textfile = open('binsulin-seq-clean.txt', 'w')
    textfile.write(binsulinseqclean)
    textfile.close()
    
# cinsulin-seq-clean.txt 55-89  35

cinsulinseqclean = preproinsulinseqclean[54:89]
if len (cinsulinseqclean) == 35:
    print ("good")
    textfile = open('cinsulin-seq-clean.txt', 'w')
    textfile.write(cinsulinseqclean)
    textfile.close()
    
# ainsulin-seq-clean.txt 90-110  21

ainsulinseqclean = preproinsulinseqclean[89:110]
if len (ainsulinseqclean) == 21:
    print ("good")
    textfile = open('ainsulin-seq-clean.txt', 'w')
    textfile.write(ainsulinseqclean)
    textfile.close()
    
    
