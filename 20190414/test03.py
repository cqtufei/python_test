
# f = open('2019-4-14.log','a')
# f.write('tgfeitjjhfi')

f = open('read.log','r',encoding=('utf8'))
r = f.read()
print('日志文件1.read.log: \n',r,'\n')



with open('2019-4-14.log','r',encoding=('utf8')) as f:
    r = f.readline()
    # r = f.read
    print('日志文件2.2019-4-14.log: \n',r)