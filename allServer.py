import math
class Point:
    x=99999.0
    y=99999.0
    z=99999.0
    def __init__ (self, x, y ,z):
        # Initializes the Point class
        self.x = x
        self.y = y
        self.z = z  
    def RMSD_sum(self, other_point):
        # dist (float) to another point
        deltax = self.x - other_point.x
        deltay = self.y - other_point.y
        deltaz = self.z - other_point.z
        return (math.pow(deltax,2) + math.pow(deltay,2) + math.pow(deltaz,2))

def get_coor(line):
        l = line.split()
        fl1 = l[0]
        fl2 = l[1]
        fl3 = l[2]
        x = float(fl1)
        y = float(fl2)
        z = float(fl3)
        p = Point (x,y,z)
        return p

f_ref = open('2UUY_coor.txt','r')
f2 = f_ref.readlines()  # f2 is a list, each line is a []
fo = open('RMSD_300_400.txt','w') 
for fiNum in range(400):
    filename_in ='swarm_' + str(fiNum) + '\\' + 'gso_200.out'
    fi = open(filename_in,'r')
    count = 0
    num = 0  # num is the line number of ref file       
    for line in fi.readlines(1,302):
        line = line.split()
        coor = []
        for j in range(3):
            coordinate = line[j].replace(',','')
            coordinate = coordinate.replace('(','')
            coor.append(coordinate)
        fi_line = ' '.join(coor)  # fi_line is a string in a format of 'x y z'




    
    



        num = 0

            # for _str in ('CA', ' B ', 'GLY B  75',):
            #     if _str in line:

            if 'CA' in line:
                if  ' B ' in line:
                    if 'GLY B  75' not in line:
                        if 'ALA B  21' not in line:
                            if 'ALA B  22' not in line:
                                if 'GLU B  23' not in line:
                                    
                                    line = line.split()
                                    coor = []
                                    
                                    for j in range(6,9):
                                        coor.append(line[j])
                                    fi_line = ' '.join(coor)
                                    if num < 51:
                                        f_ref_line = f2[num]
                                        num += 1
                                        p = get_coor(fi_line)
                                        q = get_coor(f_ref_line)
                                        RMSD_sum = p.RMSD_sum(q)
                                        count += RMSD_sum
    

        fi.close()
        f_ref.close()
    RMSD = math.sqrt(count/(100*51))
    fo.write(str(RMSD))
    fo.write('\n')
fo.close()