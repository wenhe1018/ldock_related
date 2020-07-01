
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

fo = open('RMSD_400_300.txt','w') 
for fiNum in range(400):  
    count = 0    
    for a in range(100):
        filename_in ='swarm_' + str(fiNum) + '/' + 'lightdock_'+ str(a) +'.pdb'
        fi = open(filename_in,'r')
        f_ref = open('2UUY_coor.txt','r')

        f2 = f_ref.readlines()
        num = 0
        for line in fi.readlines():
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
        RMSD = math.sqrt(count/(51))
        if RMSD < 5:
            fo.write(filename_in)
            fo.write(str(RMSD))
            fo.write('\n')

    

        fi.close()
        f_ref.close()
    

fo.close()

