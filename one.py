customer=[
{
"cust_name": "Brad Davis",
"city": "New York",
"customer_id": "3007",
"grade": "200",
"salesman_id": "5001"
},
{
"cust_name": "Graham Zusi",
"city": "California",
"customer_id": "3005",
"grade": "300",
"salesman_id": "5002"
},
{
"city": "New York",
"cust_name": "Nick Rimando",
"customer_id": "3002",
"grade": "100",
"salesman_id": "5001"
},
{
"cust_name": "Jozy Altidor",
"city": "Moscow",
"customer_id": "3003",
"grade": "200",
"salesman_id": "5007"
},
{
"cust_name": "Geoff Cameron",
"city": "Berlin",
"customer_id": "3009",
"grade": "100",
"salesman_id": "5003"
},
{
"cust_name": "Brad Guzan",
"city": "London",
"customer_id": "3001",
"grade": "200",
"salesman_id": "5005"
},
{
"cust_name": "Fabian Johnson",
"city": "Paris",
"customer_id": "3004",
"grade": "300",
"salesman_id": "5006"
},
{
"cust_name": "Julian Green",
"city": "London",
"customer_id": "3008",
"grade": "300",
"salesman_id": "5002"
}
]
salesman =[
{
"city": "San Jose",
"commission": "0.12",
"salesman_id": "5003",
"name": "Lauson Hen"
},
{
"city": "New York",
"commission": "0.15",
"salesman_id": "5001",
"name": "James Hoog"
},
{
"city": "Paris",
"commission": "0.13",
"salesman_id": "5002",
"name": "Nail Knite"
},
{
"city": "Rome",
"commission": "0.13",
"salesman_id": "5007",
"name": "Paul Adam"
},
{
"city": "Paris",
"commission": "0.14",
"salesman_id": "5006",
"name": "Mc Lyon"
},
{
"city": "London",
"commission": "0.11",
"salesman_id": "5005",
"name": "Pit Alex"
}
]
order = [
{
"customer_id": "3001",
"ord_no": "70009",
"purch_amt": "270.65",
"salesman_id": "5005",
"ord_date": "2012-09-10"
},
{
"customer_id": "3009",
"ord_no": "70004",
"salesman_id": "5003",
"purch_amt": "110.5",
"ord_date": "2012-08-17"
},
{
"customer_id": "3005",
"ord_no": "70001",
"salesman_id": "5002",
"purch_amt": "150.5",
"ord_date": "2012-10-05"
},
{
"customer_id": "3008",
"ord_no": "70012",
"salesman_id": "5002",
"purch_amt": "250.45",
"ord_date": "2012-06-27"
},
{
"customer_id": "3004",
"ord_no": "70010",
"salesman_id": "5006",
"purch_amt": "1983.43",
"ord_date": "2012-10-10"
},
{
"customer_id": "3005",
"ord_no": "70007",
"salesman_id": "5002",
"purch_amt": "948.5",
"ord_date": "2012-09-10"
},
{
"customer_id": "3002",
"ord_no": "70002",
"salesman_id": "5001",
"purch_amt": "65.26",
"ord_date": "2012-10-05"
},
{
"customer_id": "3002",
"ord_no": "70008",
"salesman_id": "5001",
"purch_amt": "5760",
"ord_date": "2012-09-10"
},
{
"customer_id": "3005",
"ord_no": "70005",
"salesman_id": "5001",
"purch_amt": "2400.6",
"ord_date": "2012-07-27"
},
{
"customer_id": "3003",
"ord_no": "70011",
"salesman_id": "5007",
"purch_amt": "270.65",
"ord_date": "2012-08-17"
}
]
for i in customer:
    for j in salesman:
        # if i['city']==j['city']:
        #     print(i['cust_name'],"    ",j['city'],"   ",j['name'])
            
        # if i['salesman_id']==j['salesman_id']:
        #     print(i['cust_name'],"----------------------",j['name'])
        if i['city']!=j['city']:
            print(i['cust_name'],"----------------------",j['name'])