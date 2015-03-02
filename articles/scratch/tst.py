import random
print '!!'
for i in range(1, 12):
    attachs = int(random.uniform(1, 5))
    for attach in range(1, attachs):
        for dir in ['X', 'Y', 'Z']:
            print 'PART_%02i_LOCATION_%02i_%s' % (i, attach, dir, ),
            for ii in range(0, 23):
                    print '%10f' % random.uniform(-10/attachs, 10/attachs),
            print ''

