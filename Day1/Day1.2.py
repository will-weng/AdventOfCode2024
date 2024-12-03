f = open("LocationIDs.txt", "r")
locationIdString = f.read();
locationIdsList = locationIdString.split();

list1 = []
list2 = []
for iter, locationID in enumerate(locationIdsList):
    if(iter % 2 == 0):
        list1.append(int(locationID))
    else:
        list2.append(int(locationID))
list1.sort()
list2.sort()

totalSimilarity = 0;
for i in range(len(list1)):
    totalSimilarity += list2.count(list1[i]) * list1[i];

print(totalSimilarity)