# Repeats the amount of times (!,@,#,$,&) appears in a string
# specialCharCount('!@#$&')
# returns '!, @, #, $, & appear, respectively, 0, 0, 0, 1, 0 times'

def specialCharCount(str):
    count = {'!': 0, '@': 0, '#': 0, '$': 0, '&': 0}
    for c in str:
        if c in count:
            count[c] += 1
    print('!, @, #, $, & appear, respectively, {}, {}, {}, {}, {} times'.format(count['!'], count['@'],
                                                                                count['#'], count['$'], count['&']))
