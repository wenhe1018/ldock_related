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

finename_out = 'RMSD_0.txt'
fo = open(finename_out,'w')
count = 0
for a in range(50):
    filename_in = 'ld_coor'+ str(a) +'.txt'

    fi = open(filename_in,'r')
    f_ref = open('2UUY_coor.txt','r')

    f1= fi.readlines()
    f2= f_ref.readlines()

    print(len(f2))
    for i in range(len(f1)):
    # while i < 51:
        fi_line = f1[i]
        f_ref_line = f2[i]
        
        p = get_coor(fi_line)
        q = get_coor(f_ref_line)
        RMSD_sum = p.RMSD_sum(q)
        count += RMSD_sum
    fi.close()
    f_ref.close()
RMSD = math.sqrt(count/(50*51))
fo.write(str(RMSD))

fo.close()

