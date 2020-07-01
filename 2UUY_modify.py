'''
fi = open('2UUY_alighed.txt','r')
fo = open('2UUY_clean.txt','w')
for line in fi.readlines():
    if line.startswith('ATOM'):
        fo.write(line)

fi.close()
fo.close()
'''
fo = open('2UUY_cleanLD.txt','w')
haha = input(str)
fi = open(haha,'r')
a = 0
for line in fi.readlines():
    if 'CA' in line:
        if  ' B ' in line:
            if 'GLY B  75' not in line:
                if 'ALA B  21' not in line:
                    if 'ALA B  22' not in line:
                        if 'GLU B  23' not in line:
                            a += 1
                            fo.write(line)
                
print (a)
