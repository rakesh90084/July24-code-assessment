import re,csv,logging,pymongo,smtplib
donorlist=[]
try:
    client=pymongo.MongoClient("mongodb://localhost:27017/") #establishing connection
    mydatabase=client['BBMSDb'] #database
    collection_name=mydatabase['BBMS-Donor']
    class BloodBankMgt:
            def donor(self,dname,daddress,dbgroup,dpincode,dmno,dmail,dlastDonatedDate,dplace):
                self.dname=dname
                self.daddress=daddress
                self.dbgroup=dbgroup
                self.dpincode=dpincode
                self.dmno=dmno
                self.dmail=dmail
                self.dlastDonatedDate=dlastDonatedDate
                self.dplace=dplace   
            def adddonordetail(self,dname,daddress,dbgroup,dpincode,dmno,dmail,dlastDonatedDate,dplace):
                dict1={"dname":dname,"daddress":daddress,"dbgroup":dbgroup,"dpincode":dpincode,"dmno":dmno,"dmail":dmail,"dlastDonatedDate":dlastDonatedDate,"dplace":dplace,"delflag":0} 
                return dict1
    def validated(dname,daddress,dbgroup,dpincode,dmno,dmail,dplace):
        valdonorname=re.search("^[A-Z]{1}[A-Z]{0,25}$",dname)
        valaddress=re.search("^[A-Z]{1}[A-Z]{0,200}$",daddress)
        valdbgroup=re.search("^(A|B|AB|O)[+-]$",dbgroup)
        valdbpincode=re.search("^[0-9]{0,6}$",dpincode)
        valdmno=re.search("^[7-9]{1}[0-9]{9}$",dmno)
        valmail=re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",dmail)
        valdplace=re.search("^[A-Z]{1}[A-Z]{0,200}$",dplace)
        if valdonorname and valaddress and valdbgroup and valdbpincode and valdmno and valmail and valdplace:
            return True
        else:
            return False    
    obj=BloodBankMgt()
    if(__name__=="__main__"):
        while True:
            print("1.Add Donors")
            print("2.Search Donors based on blood group") 
            print("3.Search Donors based on blood group AND place")
            print("4.Update Donor details with their mobile number")
            print("5.Delete the donor using mobile number")
            print("6.Display the total number of donors on each blood group")
            print("7.Immediate notification to all via email")
            print("8.View DONORS")
            print("9.Exit")
            choice=int(input("Enter your option : "))
            if choice==1:
                dname=input("Enter the DONOR NAME : ") 
                daddress=input("Enter the DONOR ADDRESS : ") 
                dbgroup=input("Enter the DONOR BLOOD GROUP : ") 
                dpincode=input("Enter the PINCODE : ")
                dmno=input("Enter the DONOR MOBILE NUMBER : ")
                dmail=input("Enter the DONOR MAIL ID : ")
                dlastDonatedDate=input("Enter the DONOR'S LAST DONATED DATE : ")
                dplace=input("Enter the PLACE: ")
                if validated(dname,daddress,dbgroup,dpincode,dmno,dmail,dplace)==True:
                    data=obj.adddonordetail(dname,daddress,dbgroup,dpincode,dmno,dmail,dlastDonatedDate,dplace) 
                    donorlist.append(data)
                    result=collection_name.insert_many(donorlist)
                    print(result.inserted_ids)
                    donorlist.clear()
                else:
                    logging.error("VALIDATION ERROR!!!")
                    break
            if choice==2:
                blood=input("Enter the blood group to search donor : ")
                result= collection_name.find({"$and":[{"dbgroup":blood},{"delflag":0}]},{"_id":0})
                for j in result:
                    print(j)
                
            if choice==3:
                sea=input("Enter the blood group :")
                sea1=input("Enter the place :")
                result= collection_name.find({"$and":[{"dbgroup":sea},{"dplace":sea1}]},{"delflag":0}) 
                for j in result:
                    print(j)
                donorlist.clear()  
            if choice==4:
                s=input("Enter the DONOR MOBILE NO :")
                tname=input("Enter the DONOR NAME to be updated : ")
                taddress=input("Enter the DONOR ADDRESS to be updated : ")
                tblood=input("Enter the DONOR BLOOD GRP to be updated : ")
                tpincode=input("Enter the DONOR PINCODE to be updated : ")
                tmail=input("Enter the DONOR MAIL to be updated : ")
                tdate=input("Enter the DATE to be updated : ")
                tplace=input("Enter the PLACE to be updated : ")
                result= collection_name.update_one({"$and":[{"dmno":s,"delflag":0}]},{"$set":{"dname":tname,"daddress":taddress,"dbgroup":tblood,"dpincode":tpincode,"dmno":s,"dmail":tmail,"dLastDonatedDate":tdate,"dplace":tplace}})
                print(result)          
            if choice==5:
                de=input("Enter the MOBILE NO TO DELETE :")
                result= collection_name.update_one({"dmno":de},{"$set":{"delflag":1}}) 
                print(result)        
            if choice==6:
                bld=input("Enter the blood group to know the count :")
                result= collection_name.count_documents({"dbgroup":bld,"delflag":0}) 
                print("BLOOD GROUP COUNT=",result)
            if choice==8:
                result=collection_name.find({"delflag":0},{"_id":0})
                for i in result:
                    print(i)        
            if choice==7:
                ch=input("Enter the blood group to send mail to donor : ")
                result=collection_name.find({"delflag":0},{"_id":0})
                connection=smtplib.SMTP("smtp.gmail.com",587)
                connection.starttls()
                connection.login("rakesh.learning.python@gmail.com","9008496668Ra@")
                for i in result:
                    msg="Dear Donor, \n\nThere is immediate need for : " +ch+ " blood group. \n\nKindly contact APOLLO if your ready to donate.\n\nThank you."
                    connection.sendmail("rakesh.learning.python@gmail.com",i["dmail"],msg)
                print("EMAIL SENT")
                connection.quit()
            
            if choice==9:
                break    
except:
    logging.error("OOPS!! Something is wrong") 
finally:
    print("Thank you")                                                                      