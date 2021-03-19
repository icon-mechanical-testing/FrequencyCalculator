

filename = "35 hertz.txt"
with open(filename) as f:
    data = f.readlines()

times = [i.split('\t')[0] for i in data]
displacement = [i.split('\t')[1] for i in data]

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

print("Amplitude: ", amplitude)