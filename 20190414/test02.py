
f = open('2019-4-14.log','w')
f.write('log,This is a logfile')

# f = open('2019-4-14.log','r',encoding=('utf8'))
# r = f.read()
# print(r)



with open('2019-4-14.log','r',encoding=('utf8')) as f:
    r = f.readline()
    # r = f.read
    print(r)