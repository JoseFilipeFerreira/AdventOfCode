import numpy

def main():
    with open("input.txt", 'r') as file:
        file = file.read()
        file = file.split("\n")
        file = file[:-1]
        record = []
        for string in file:
            dic={}
            stime = string[1:17]
            time={}
            time["day"]    = int(stime[8:10]) + 31 * int(stime[5:7])
            time["hour"]   = int(stime[11:13])
            time["minute"] = int(stime[14:16]) 
            dic["time"]   = time
            if string[19:] == "wakes up":
                dic["action"] = 1
            elif string[19:] == "falls asleep":
                dic["action"] = -1
            else:
                dic["action"] = int(string[26:][:-13])

            record.append(dic)

        def t_in_min(entry):
            time = entry["time"]
            r =  time["minute"]
            r += time["hour"] * 60
            r += time["day"] * 1440
            return r

        record.sort(key=t_in_min)
        

        calendar =  numpy.zeros((60, 365))

        curr_guard = 0

        for pos in range(len(record)):
            event = record[pos]
            if event["action"] not in [-1, 1]:
                curr_guard = event["action"]
            elif event["action"] == -1:
                for min in range(event["time"]["minute"], record[pos+1]["time"]["minute"]):
                    calendar[min][event["time"]["day"]] = curr_guard
    
    minDic={}
    for min in range(60):
        for day in range(365):
            if calendar[min][day] != 0:
                if calendar[min][day] in minDic:
                    minDic[calendar[min][day]] +=1
                else:
                    minDic[calendar[min][day]] =1
    guard = -1
    t_slept = -1         
    for k in minDic.keys():
        if minDic[k] > t_slept:
            t_slept = minDic[k]
            guard = k

    min_slept = -1
    t_slept = -1

    for min in range(60):
        curr_t_slept = 0
        for day in range(365):
            if calendar[min][day] == guard:
                curr_t_slept += 1
        if curr_t_slept > t_slept:
            t_slept = curr_t_slept
            min_slept = min
   
    print("first part:")
    print(min_slept * guard)

    guard = -1
    t_min_slept = -1
    min_best = -1

    for min in range(60):
        minDic={}
        for day in range(365):
            if calendar[min][day] != 0:
                if calendar[min][day] in minDic:
                    minDic[calendar[min][day]] += 1
                else:
                    minDic[calendar[min][day]] = 1
        
        for k in minDic.keys():
            if minDic[k] > t_min_slept:
                t_min_slept = minDic[k]
                guard = k
                min_best = min
    
    print("Second part:")
    print(guard * min_best)
        

    
    
      
     
    
#[1518-09-17 23:48] Guard #1307 begins shift
#year-month-day hour:minute
main()