from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

from boto3.dynamodb.conditions import Key, Attr

import os
os.environ["NO_PROXY"] = "s3.amazonaws.com"

dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table('hungrymind-mobilehub-593518188-Books')


response = table.scan()
books=response['Items']


table=dynamodb.Table('hungrymind-mobilehub-593518188-Customer_table')


response = table.scan()
customers=response['Items']

table=dynamodb.Table('hungrymind-mobilehub-593518188-Book_Borrow')

import csv
import random
'''
csv_columns = ['DateOfBorrow','SupplierID','BookID','DateClaimToRet','BorrowID','CustID','ActualRetDate','CustId','BookId']
table=dynamodb.Table('hungrymind-mobilehub-593518188-Borrowed')
#response=table.scan()
dict_data = response['Items']
csv_file = "mydataaa.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")
    
'''
sup=1
borrowid=11031
arr=[]
are=[0,-2,-1,0,1,2,3,4,5,6,7,0,0]
for i in range(7,31):
    arr.append(i)

    

for x in customers:
    for i in range(2):
        rating=random.randint(0,5)
        borrowid+=1
        num=random.randint(0,5686) 
        custid=(x['userId'])
        bookid=(books[num]['ISBN'])

        month=random.randint(1,12)
        day=1
        day2=8
        month2=month
        year=random.randint(1900,2019)
        year2=year
        dur=random.randint(0,23)
        durre=random.randint(0,11)
        #print(month,year)
        if (month == 4 or month == 6 or month == 9 or month == 11):
            day = random.randint(1, 30)
            day2 =day+ arr[dur]
            #print(arr[dur])
            #print(day,day2)
            if (day2 > 30):
                day2 = day2 - 30
                month2=month2+1
            if (month2 > 12):
                month2 = 1
                year2=year2+1
        elif (month == 2):
            
            day = random.randint(1, 28)
            day2 = day+arr[dur]
            #print(arr[dur])
            #print(day,day2)
            if (day2 > 28):
                day2 = day2 - 28
                month2=month2+1
            if (month2 > 12) :
                month2 = 1
                year2=year2+1
        else:
            
            day = random.randint(1, 31)
            day2= day+arr[dur]
            #print(arr[dur])
            #print(day,day2)
            if (day2 > 31):
                day2 = day2 - 31
                month2=month2+1
            if (month2 > 12):
                month2= 1
                year2=year2+1
                 

        day3 = day2 + are[durre]
        #print(day3)
        month3 = month2
        year3 = year2
        if (month2 == 1):
            if (day3 < 1):
                day3 = 31
                month3 = 12
                year3 = year2 - 1
            
            if (day3 > 31):
                day3 = 1
                month3 = 2
        
        
        if (month2 == 2) :
            if (day3 < 1) :
                day3 = 31
                month3 = 1
                year3 = year2
            
            if (day3 > 28):
                day3 = 1
                month3 = 3
                year3 = year2
            
        
        if (month2 == 3) :
            if (day3 < 1) :
                day3 = 28
                month3 = 2
                year3 = year2
            
            if (day3 > 31) :
                day3 = 1
                month3 = 4
                year3 = year2
            
        if (month2 == 4 or month2 == 6 or month2 == 9 or month2 == 11) :
            if (day3 < 1) :
                day3 = 31
                month3 = month2 - 1
                year3 = year2
            
            if (day3 > 31) :
                day3 = 1
                month3 = month2 + 1
                year3 = year2
            
        if (month2 == 5 or month2 == 7 or month2 == 8 or month2 == 10) :
            if (day3 < 1) :
                day3 = 30
                month3 = month2 - 1
                year3 = year2
            
            if (day3 > 31) :
                day3 = 1
                month3 = month2 + 1
                year3 = year2

        if (month2 == 12) :
            if (day3 < 1) :
                day3 = 30
                month3 = 11
                year3 = year2
            
            if (day3 > 31) :
                day3 = 1
                month3 = 1
                year3 = year2 + 1
        dat1 = str(day3) + "-" + str(month3) + "-" + str(year3)
        #System.out.println(dat);//actual ret date
        dat2 = str(day2) + "-" + str(month2) + "-" + str(year2)
        #System.out.println(dat);//date claim to ret
        dat3 = str(day) + "-" + str(month) + "-" + str(year)
        #System.out.println(dat);//date of borrow
        #print(dat3,dat2,dat1)
        print(borrowid)
        
        table.put_item(
                  Item={
                      'BorrowId':borrowid,
                      'ActualRetDate':dat1,
                      'BookID':bookid,
                      'CustID':custid,
                      'DateClaimToRet':dat2,
                      'DateOfBorrow':dat3,
                      'SupplierID':'1',
                      'Rating' : rating
                }
            )
            

''' 
with open('mydataaa.csv','rt')as f:
    data = csv.reader(f)
    print(data)
    for i in data:
        #i=data[i]
        print(i)
        if(len(i)>0 and i[7]=="" and i[1]=='1'):
            import random
            r=random.uniform(0, 5)
            s=""
            for j in i[2]:
                if (j=='E'):
                    break;
                elif(not j=='.'):
                    s+=j
            s2=""
            for j in i[5]:
                if(j=='.'):
                    break
                else:
                    s2+=j
            table.put_item(
                  Item={
                      'BorrowId':int(i[4]),
                      'ActualRetDate':i[6],
                      'BookID':int(s),
                      'CustID':int(s2),
                      'DateClaimToRet':i[3],
                      'DateOfBorrow':i[0],
                      'SupplierID':'1',
                      'Rating' : str(r)
                }
            )
'''
