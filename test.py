inn = raw_input('Input string: ')

palindrome = True

for i in xrange(0, len(inn)/2):
    if inn[i] != inn[len(inn)-i-1]:
        palindrome = False
        break

print 'Palindrome!', palindrome
