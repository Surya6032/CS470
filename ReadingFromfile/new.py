dataList = []
infile=open("dataset.txt","r")
for line in infile:
    dataList.append(line.strip())
infile.close()
print("F3 Tornadoes in Alabama since 1980")
print()
print("year      County         Dat.Inj.")
for tornado in dataList:
    data = tornado.split(",")
    if int(data[0])>=1980:
        print("%5"%data[0], "%30s"%data[1], "%5s"%data[3], "%5s"%data[4])
