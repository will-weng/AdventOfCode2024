f = open("LocationIDs.txt", "r")
locationIdString = f.read();
locationIdsList = locationIdString.split();

list1 = []
list2 = []
for iter, locationID in enumerate(locationIdsList):
    if(iter % 2 == 0):
        list1.append(locationID)
    else:
        list2.append(locationID)
list1.sort()
list2.sort()

totalDistance = 0;
for i in range(len(list1)):
    distance = abs((int(list1[i]) - int(list2[i])));
    totalDistance += distance

print(totalDistance)