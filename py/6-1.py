def channel(nothing):
    import zipfile
    import re

    zip = zipfile.ZipFile('channel.zip')
    comments = ''

    while True:
        s = zip.open(nothing+'.txt', 'r').read()
        comments += zip.getinfo(nothing+'.txt').comment
        print s
        nothing = ''.join(re.findall('(\d+)$', s))
        if len(nothing) == 0:
            print comments
            break

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        channel(sys.argv[1])
    else:
        print 'Usage: %s [nothing]' % sys.argv[0]
