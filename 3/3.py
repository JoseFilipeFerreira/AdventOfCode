import numpy

def main():
    with open("input.txt", 'r') as file:
        file = file.read()
        file = file.split("\n")
        file = file[:-1]

        claims=[]

        for line in file:
            line = line.split(" ")
            line.remove("@")
            line[1] = line[1][:-1]
            line [1] = line[1].split(",")
            posx = int(line[1][0])
            posy = int(line[1][1])
    
            line[2] = line[2].split("x")
            sx = int(line[2][0])
            sy = int(line[2][1])
    
            dic={}
            dic["id"] = int((line[0])[1:])
            dic["pos"] = (posx, posy) 
            dic["size"] = (sx,sy)
            claims.append(dic)
        
        ms = 2000
        candidates = list(range(1, len(claims) + 1))
        cloth =  numpy.zeros((ms, ms))
        for claim in claims:
            (px, py) = claim["pos"]
            (sx, sy) = claim["size"]
            
            for x in range(px, px+sx):
                for y in range(py, py+sy):
                    if cloth[x][y] == 0:
                        cloth[x][y] = claim["id"]
                    else:
                        if claim["id"] in candidates:
                            candidates.remove(claim["id"])
                        if cloth[x][y] in candidates:
                            candidates.remove(cloth[x][y])
                        cloth[x][y] = -1
        print("No intersections:")
        print(candidates[0])
        intersects = 0
        for x in range(2000):
            for y in range(2000):
                if cloth[x][y] == -1:
                    intersects += 1
        
        print("Area of intersections")
        print(intersects)



def intersect(claim1, claim2):
    area = 0
    px1, py1 = claim1["pos"]
    sx1, sy1 = claim1["size"]
    px2, py2 = claim2["pos"]
    sx2, sy2 = claim2["size"]

    xmin1 = px1
    ymin1 = py1
    xmax1 = px1 + sx1
    ymax1 = py1 + sy1
    xmin2 = px2
    ymin2 = py2
    xmax2 = px2 + sx2
    ymax2 = py2 + sy2

    dx = min(xmax1, xmax2) - max(xmin1, xmin2)
    dy = min(ymax1, ymax2) - max(ymin1, ymin2)
    if (dx >= 0) and (dy>= 0):
        area = dx*dy

    x1 = max(min(xmin1, xmax1), min(xmin2, xmax2))
    y1 = max(min(ymin1, ymax1), min(ymin2, ymax2))
    
    x2 = min(max(xmin1, xmax1), max(xmin2, xmax2))
    y2 = min(max(ymin1, ymax1), max(ymin2, ymax2))

    dic={}
    dic["id"] = -1
    dic["pos"] = (x1,y1)
    dic["size"] = (x2-x1, y2-y1)

    return area, dic

main()