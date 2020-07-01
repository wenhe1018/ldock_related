
'''
for a in range(10):
    filename_in = 'lightdock_'+ str(a) +'.txt'
    filename_out = 'ld_coor'+ str(a) +'.txt'
    fi = open(filename_in,'r')
    fo = open(filename_out,'w')

    for line in fi.readlines():
        for i in range(len(line)):
            
            if line[i:i+6]== '      ':
                new_line = line[i+6:]
                for j in range(len(new_line)):
                    if new_line[j:j+4] == '1.00':
                        fo.write(new_line[:j])
                        fo.write('\n')
    fi.close()
    fo.close()



fi = open('2UUY_cleanCA.txt','r')
fo = open('2UUY_coor.txt','w')

for line in fi.readlines():
    for i in range(len(line)):
        
        if line[i:i+5]== '     ':
            new_line = line[i+5:]
            for j in range(len(new_line)):
                if new_line[j:j+4] == '1.00':
                        fo.write(new_line[:j])
                        fo.write('\n')
                if new_line[j:j+4] == '0.50':
                        fo.write(new_line[:j])
                        fo.write('\n')
        break
fi.close()
fo.close()


fi = open('2UUY_cleanCA.txt','r')
fo = open('2UUY_coor.txt','w')

for line in fi.readlines():
    line = line.split()
    for i in range(6,9):
        fo.write(line[i] + ' ')
    fo.write('\n')
        
        
fi.close()
fo.close()
'''
for a in range(50):
    filename_in = 'lightdock_'+ str(a) +'.txt'
    filename_out = 'ld_coor'+ str(a) +'.txt'
    fi = open(filename_in,'r')
    fo = open(filename_out,'w')

    for line in fi.readlines():
        line = line.split()
        for i in range(6,9):
            fo.write(line[i] + ' ')
        fo.write('\n')

    fi.close()
    fo.close()
