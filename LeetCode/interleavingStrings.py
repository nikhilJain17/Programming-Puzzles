
def isInterleave(s1, s2, s3):
    us1 = ''
    us2 = ''
    
    
    for x in xrange(0, len(s3) + 1, 2):
        print s3[x:x+2] + '<<<'
        # determine which string to append to
        if (x / 2) % 2 == 0:
            us1 += s3[x:x+2]
        else:
            us2 += s3[x:x+2]
    
    print us1
    print us2
    print 


isInterleave('aabcc', 'dbbca', 'aadbbcbcac')