from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

from boto3.dynamodb.conditions import Key, Attr

import os
os.environ["NO_PROXY"] = "s3.amazonaws.com"

dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table('hungrymind-mobilehub-593518188-BookBorrow')




import csv

'''csv_columns = ['DateOfBorrow','SupplierID','BookID','DateClaimToRet','BorrowID','CustID','ActualRetDate','CustId','BookId']
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
