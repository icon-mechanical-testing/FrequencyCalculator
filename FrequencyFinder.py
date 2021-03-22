


# importing csv module 
import csv 

# ---------------------------------------- If using .csv file then use code below -------------------------------------------
# csv file name 
filename = "50HertzCenter.csv"
  
# initializing the titles and rows list 
fields = [] 
rows = [] 
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
  
    # get total number of rows 
    # print("Total no. of rows: %d"%(csvreader.line_num)) 
  
times = []
displacement = []
for i in range(len(rows)):
    value = float(rows[i][0])
    dispValue = float(rows[i][1])
    times.append(value)
    displacement.append(dispValue)

# ------------------------------------ If using .txt file then use code below --------------------------------------------
# filename = "20HertzCenter.csv"
# with open(filename) as f:
#     data = f.readlines()

# times = [i.split('\t')[0] for i in data]
# displacement = [i.split('\t')[1] for i in data]

time = []
for i in times:
    time.append(float(i))
disp = []
for i in displacement:
    disp.append(float(i))

def average(list):
    return sum(list) / len(list)

def extremes(list):
    peak = []
    valleys = []
    for i in range(len(list)-1):
        if list[i-1] < list[i] and  list[i+1] < list[i]:
            peak.append(list[i])
        
        if list[i-1] > list[i] and list[i+1] > list[i]:
            valleys.append(list[i])
    return peak, valleys

dispPeak, dispValley = extremes(disp)

avg_disp_peak = average(dispPeak)
avg_disp_valley = average(dispValley)

amplitude = (avg_disp_peak - avg_disp_valley)/2

def get_frequency(time, disp):
    avg_disp = average(disp)
    count = 0
    for i in range(len(disp)-1):
        if (disp[i] < avg_disp and disp[i+1] > avg_disp):
            count += 1
    max_time = max(time)
    min_time = min(time)

    # print("max time: ", max_time)
    # print("min time: ", min_time)

    frequency = (count/(max_time - min_time))
    return frequency
# def get_frequency(time, disp):
#     avg_disp = average(disp)
#     count = 0

#     for i in range(len(disp)-1):
#         if (disp[i-1] < avg_disp and disp[i+1] > avg_disp) or (disp[i-1] > avg_disp and disp[i+1] < avg_disp):
#             count += 1
#     count = count/2
#     max_time = max(time)
#     min_time = min(time)

#     # print("max time: ", max_time)
#     # print("min time: ", min_time)

#     frequency = (count/(max_time - min_time))/2
#     return frequency


print("Test: ", filename)
frequency = get_frequency(time, disp)
print("Frequency: ", frequency)

print("Amplitude (mm): ", amplitude)
print("Amplitude (mil): ", amplitude/.0254)