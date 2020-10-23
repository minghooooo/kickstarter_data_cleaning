import csv
import os
import re
files = 'C:\\Users\\Kevin\\Desktop\\kickstarter\\'
file= os.listdir(files)
for fp in file:
    with open(files + fp, 'r', encoding='utf-8') as csvfile:
        content = csv.reader(csvfile)
        for c in content:
            date = c[0]
            id = c[1]
            name = c[2].replace('react-staff_pick-','').replace('react-popular-','')
            category = c[3].replace('discovery_','')
            moneys = c[4]
            money = re.findall(r"\d{1,}?\.\d{1,2}", moneys)
            money = ''.join(money)
            percents = c[5]
            percent = re.findall(r"\d{1,}?\.\d{1,2}",percents)
            percent = ''.join(percent)
            with open('C:\\Users\\Kevin\\Desktop\\kickstarter1\\' + id +'.csv', 'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([date,id,name,category,money,percent])


        # categories = [c3[3] for c3 in columns]
        # for category in categories:
        #     category = category.replace('discovery_','')
        #     # print(category)
        # moneys = [c4[4] for c4 in columns]
        # for money in moneys:
        #     money = re.findall(r"\d{1,}?\.\d{1,2}", money)
        #     # print(money)
        # percents = [c[5] for c in columns]
        # for percent in percents:
        #     percent = re.findall(r"\d{1,}?\.\d{1,2}",percent)
        #     # print(percent)
        # print(list)
        # with open(files+fp,'w',encoding='utf-8',newline='') as f:
        #     writer = csv.writer(f)
        #     writer.writerow([date,id,name,category,money,percent])


        