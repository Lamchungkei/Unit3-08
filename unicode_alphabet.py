# Created by: Kay Lin
# Created on: 24th-Oct-2017
# Created for: ICS3U
# this is a unicode program that prints lower case and upper case letters.

for number in range(65,91):
    unicode = unichr(number)
    print (str(number) + '->' + str(unicode) )
    
for number in range(97, 123):
    unicode = unichr(number)
    print (str(number) + '->' + str(unicode))
