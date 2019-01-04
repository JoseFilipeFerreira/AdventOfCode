import numpy
import operator

def main():
    with open("input.txt", 'r') as file:
        file = file.read()
        file = file.split("\n")
        file = file[:-1]

        points = []
        for line in file:
                i = line.split(',')
                x = int(i[0]) 
                y = int(i[1])
                points.append((x, y))
        
        ms = 357
        area =  numpy.zeros((ms, ms))

        for x in range(len(area)):
                for y in range(len(area[0])):
                        area[x][y] = closePoint(points, x, y)   
        
        areas = {}
        
        for x in range(len(area)):
                for y in range(len(area[0])):
                        if area[x][y] != -1:
                                if (x == ms - 1) or (y == ms -1) or (x == 0) or (y == 0):
                                        print("({0}, {1}".format(x,y))
                                        areas[area[x][y]] = -1
                                        area[x][y] = 0
                                else:
                                        if area[x][y] in areas and area[x][y] != -1:
                                                areas[area[x][y]] += 1
                                        else:
                                                areas[area[x][y]] = 1
        
        print(area)
        print(areas)
        
        best = max(areas.items(), key=operator.itemgetter(1))
                        
        print(best)

def closePoint(points, x, y):
        dist = []
        for pos in range(len(points)):
                (px, py) = points[pos]
                dic = {}
                dic["id"] = pos + 1
                dic["dist"] = abs(px - x) + abs(py - y)
                dist.append(dic)
        def compare(dic):
                return dic["dist"]
        dist.sort(key=compare)

        if dist[0]["dist"] < dist[1]["dist"]:
                return dist[0]["id"]
        else:
                return -1
        




main()

