for a in range(50):
    filename_in ='C:\\Users\\Wen\\Desktop\\swarm_4\\' + 'lightdock_'+ str(a) +'.pdb'
    finename_out = 'lightdock_'+ str(a) +'.txt'
    fi = open(filename_in,'r')
    fo = open(finename_out,'w')
    for line in fi.readlines():
    
        if 'CA' in line:
            if  ' B ' in line:
                if 'GLY B  75' not in line:
                    if 'ALA B  21' not in line:
                        if 'ALA B  22' not in line:
                            if 'GLU B  23' not in line:
                                fo.write(line)
    fi.close()
    fo.close()