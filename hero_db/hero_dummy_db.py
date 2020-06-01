import mysql.connector

vendorname="hero pvt ltd"
vendor_code="1100011"
po="2165153"
inv="FGVHJVJ123"
ta="128000"
invdate="21.01.2020"
invprodate="12-02-2020  12:40:17"
loc="HHHO"
billpn="ISB2006118"
status="Accept"
final_status="completed"



list_data=[[vendorname,vendor_code,po,inv,ta,invdate,invprodate,loc,billpn,status,final_status]]
print(list_data)

   #print(a,b,c,d,e,f,g,h,i,j)

myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database="hero_db")


print(myconn)

if myconn:
   print("connection is succesfully")

else: 
   print("connection successfully")

cur=myconn.cursor()



for a,b,c,d,e,f,g,h,i,j,k in list_data:
   #sql_q=("Insert into istable values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(a,b,c,d,e,f,g,h,i,j))
   cur.execute("Insert into istable values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(a,b,c,d,e,f,g,h,i,j,k))
   myconn.commit()
myconn.close()
print("data inserted sucessfully")



#sql_q="Insert "

#cur.execute("create table Istable(VendorName varchar(200),VendorCode varchar(100),InvoiceNo varchar(100),TotalAmount varchar(100),InvoiceDate varchar(100),Location varchar(100),BillPortalNo varchar(100),Status varchar(100)) ")

#cur.execute("Show tables")
#print("table created")
##
##for tl in cur:
##   print(tl)
 


