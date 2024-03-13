import csv

with open('utils/readWriteCSV.csv') as csvFile:
    data = csv.reader(csvFile, delimiter=',')
    data = list(data)

    Name = []
    Status = []
    for row in data:
        Name.append(row[0])
        Status.append(row[1])
    print(Name)
    print(Status)
    csvFile.close()

with open('utils/readWriteCSV.csv', 'a') as csvFile1:
    write = csv.writer(csvFile1)
    write.writerow(["G", "Approved"])