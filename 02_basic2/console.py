### console input!
## String input
name = raw_input('name? ')
print name
print type(name)

integer = int(raw_input('int : '))
print integer
print type(integer)
print integer+10


## Integer, float, Expression Input
i = input('int: ')
print i

k = input('expression:') # 30+50
print k


### console output!
# comma -> white space (1 space)
print 4 + 5, 4 - 2
# print -> automatically concat '\n'
print 1; print 2

print 1, # comma -> white space & remove '\n'
# print 12+'spam'          # Error! :: number + string is ERROR!!
print '12' + 'spam'
print str(12) + 'spam'

