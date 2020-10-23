import re
import os
from bs4 import BeautifulSoup
import csv
file = 'D:\TMH\kickstarter原始数据\\'
files = os.listdir(file)
files.sort()
for i in files:
    filenames = os.listdir(file + i)
    filenames.sort()
    for filename in filenames:
        print(filename)
        with open(file + i+'\\'+filename ,'r',encoding = 'utf-8') as f:
        
            a = f.read().replace('\t','').replace('\n','').replace('\r','')
            soup = BeautifulSoup(a,'lxml')
            dates = re.findall(r'\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}',filename)
            for date in dates:
                pass
                # print(date)
            content2 = soup.find_all('div',class_="js-react-proj-card col-full col-sm-12-24 col-lg-8-24")#add country div@class
            for c2 in content2:
                c2_s=str(c2)
                id =   c2.get('data-pid').replace('"','')
                print(id)
                name = c2.get('id')
                ref = c2.get('data-ref').replace('category_','').replace('discovery_','')
                money_ =  c2.get('data-project')
                money = re.findall(r'\"usd_pledged\":(.*?)(?=,)',money_)
                money = ''.join(money).replace('"','')
                percent_ = c2.get('data-project')
                percent = re.findall(r'\"percent_funded\":(.* ?)(?=})', percent_)
                percent = ''.join(percent).replace(',"is_liked":false,"is_disliked":false','')
                pattern0 = re.compile('"country":"(.*?)","currency"',re.S)
                country = re.findall(pattern0,c2_s)
                country_s = str(country).replace('[','').replace('\'','').replace(']','')
                pattern1 = re.compile('"goal":(.*?),"pledged',re.S)
                goal = re.findall(pattern1,c2_s)
                goal_s = str(goal).replace('[','').replace('\'','').replace(']','')
                pattern2 = re.compile('"currency":"(.*?)","currency_sym',re.S)
                currency = re.findall(pattern2,c2_s)
                currency_s = str(currency).replace('[','').replace('\'','').replace(']','')
                pattern3 = re.compile('"backers_count":(.*?),"static_',re.S)
                backer = re.findall(pattern3,c2_s)
                backer_s = str(backer).replace('[','').replace('\'','').replace(']','')
                pattern4 = re.compile('"launched_at":(.*?),"staff_p',re.S)
                launch_at = re.findall(pattern4,c2_s)
                launch_at_s = str(launch_at).replace('[','').replace('\'','').replace(']','')
                pattern5 = re.compile('"deadline":(.*?),"state_cha',re.S)
                deadline = re.findall(pattern5,c2_s)
                deadline_s = str(deadline).replace('[','').replace('\'','').replace(']','')
                pattern6 = re.compile('"usd_pledged":"(.*?)","converted_p',re.S)
                usd_pledged = re.findall(pattern6,c2_s)
                usd_pledged_s = str(usd_pledged).replace('[','').replace('\'','').replace(']','')
                # print(country)
                # print(id)q
                if id == id:
                    with open("D:\\TMH\\data_kickstarter\\"+id+".csv",'a',encoding='utf-8',newline='') as d: #
                        writer = csv.writer(d)
                        writer.writerow([date, id, name, ref, money, percent,country_s,goal_s,currency_s,backer_s,launch_at_s,deadline_s,usd_pledged_s])#add country
           