
# coding: utf-8

# In[6]:

import csv
file = open('trains.csv','r')
reader = csv.reader(file)
for row in reader:
    #print(row)
    break


# In[7]:

def convert_time_to_dict(s):
    return {"hours":s[:2],"minutes":s[3:5]}

def convert_dict_to_time(d):
    return str(d['hours']) + ':' + str(d["minutes"])

class Train:
    train_no = None
    train_name = None
    islno = None
    station_code = None
    station_name = None
    arrival_time = None
    departure_time = None
    distance = None
    source_station_code = None
    source_station_name = None
    destination_station_code = None
    destination_station_name = None
    
    def __init__(self,csvitem):
        self.train_no = csvitem[0].strip().replace("'","")
        self.train_name = csvitem[1].strip()
        self.islno = csvitem[2].strip()
        self.station_code = csvitem[3].strip()
        self.station_name = csvitem[4].strip()
        self.arrival_time = convert_time_to_dict(csvitem[5].strip().replace("'",""))
        self.departure_time = convert_time_to_dict(csvitem[6].strip().replace("'",""))
        self.distance = csvitem[7].strip()
        self.source_station_code = csvitem[8].strip()
        self.source_station_name = csvitem[9].strip()
        self.destination_station_code = csvitem[10].strip()
        self.destination_station_name = csvitem[11].strip()


# In[ ]:




# In[8]:

import csv

def train_chart(x):
    #Will return nothing but will make train chart csv file
    file = open('trains.csv','r')
    reader = csv.reader(file)
    for row in reader:
        print(row)
        break
    
    test_station = x
    out = open('train_chart.csv','w')
    writer = csv.writer(out,delimiter=",")
    writer.writerow(['Train Number','Train Name','Arrival','Departure','Source','Destination'])
    for row in reader:
        t = Train(row)
        if t.station_name.lower() == test_station.lower():
            data = [t.train_no,t.train_name,convert_dict_to_time(t.arrival_time),convert_dict_to_time(t.departure_time),t.source_station_name,t.destination_station_name]
            print(data)
            writer.writerow(data)
    out.close()
    file.close()
    
#train_chart("sAnGlI")


# In[79]:

def trains_between(start_code,stop_code):
    # Stores csv file of Train list in trains_between.csv
    
    infile = open('trains.csv','r')
    reader = csv.reader(infile)
    start = str(start_code).lower()
    stop = str(stop_code).lower()
    l0 = []
    for row in reader:
        train = Train(row)
        if train.station_code.lower() == start:
            l0.append(train)
        if train.station_code.lower() == stop:
            l0.append(train)
    #print(len(l0))
    l1 =[]
    for i in l0:
        l1.append(i.train_no)
    #print(len(l1))
    d = {}
    for i in l1:
        d[i] = []
        for j in l0:
            if j.train_no == i:
                d[i].append(j.station_code)
    train_no_list=[]
    for i in d.keys():
        if len(d[i]) >1:
            if d[i][0].lower() == start:
                train_no_list.append(i)

    #print(train_no_list)
    data = []
    for i in train_no_list:
        row = []
        for j in l0:
            if j.train_no == i:
                if j.station_code.lower() == start:
                    row.append(j.train_no)
                    row.append(j.station_name)
                    row.append(j.departure_time)
                    row.append(j.distance)

                if j.station_code.lower() == stop:
                    row.append(j.distance)
                    row.append(j.arrival_time)
                    row.append(j.train_name)
        data.append(row)
    #print(data[0])
    def min_to_duration(min):
        m = min%60
        h = int(min/60)
        return str(h)+':'+str(m)
    infile.close()
    with open('trains_between.csv', 'w') as f:
        wr = csv.writer(f,delimiter=",")
        wr.writerow(['Train_Number','Departure@source', 'Arrival@Destination', 'Duration','Distance'])
        print('Train_Number','Departure@source', 'Arrival@Destination', 'Duration','Distance')
        ct = 1
        for i in data:
            row = []
            row.append(str(ct) + "] ")
            row.append(i[0])
            row.append(i[6])
            row.append(str(i[2]['hours']) + ':' + str(i[2]['minutes']) )
            row.append(str(i[5]['hours']) + ':' + str(i[5]['minutes']) )
            td = int(i[2]['hours']) * 60 + int(i[2]['minutes'])
            ta = int(i[5]['hours']) * 60 + int(i[5]['minutes'])
            if ta > td:
                row.append(min_to_duration(ta-td))
            else:
                row.append(min_to_duration(ta + (24*60-td)))
            row.append(abs(int(i[3]) - int(i[4])))
            wr.writerow(row)
            print(row)
            ct+=1
#trains_between('sbc','mas')



# In[74]:

def find_station_code(name):
    infile = open('trains.csv','r')
    reader = csv.reader(infile)
    l = []
    for i in reader:
        t = Train(i)
        if name.lower() in t.station_name.lower() :
        	if t.station_name + " => " + t.station_code not in l:
        		l.append(t.station_name + " => " + t.station_code)
    for i in l:
    	print(i)    #return t.station_code
find_station_code('')

