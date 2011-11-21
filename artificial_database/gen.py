

if __name__ == '__main__':
    for i in range(0,20):
        for j in range (0,45):
            print '%d, %d, %d' % (i, j, 0)

    for i in [k + 0.5 for k in range(5, 15)]:
        for j in range (0, 5):
            print '%.2f, %d, %d' % (i, j, 1)
