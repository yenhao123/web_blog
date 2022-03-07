#!/usr/bin/env python
from censys.search import CensysHosts
from parser import process_parser
import os
import sys
    
class censys_engine():

    #set up the parameter of Censys API
    def __init__(self,api_info):
        #self.id = api_info['id']
        #self.secret = api_info['secret']
        self.ip = api_info['ip']
        self.count = api_info['count']
    
    #input the ID and Password, then run the API
    def start(self):
        print("-----------------------")
        print("Start Censys Process!!!")
        api = CensysHosts()
        self.keywordMethod(api)

    #get the result from API and print it
    def format(self,page):
        ip = page.get("ip","None")
        os = page.get("metadata.os","None")
        protocols = page.get("protocols","None")
        protocols = ", ".join([str(p.encode('UTF-8'), errors='ignore') for p in protocols])
        print("ip:" + ip, end = '\t')
        print("\n")
    
    #write the result to file
    def writeToFile(self,content):
        print(os.getcwd())
        cur_path = os.path.dirname(__file__)
        filename = cur_path + "/log/cens.log"
        f = open(filename,"a+")
        f.write(content)
        f.close()

    '''
    through device get each ip and devicemodel if it has
    '''
    def keywordMethod(self,api):
        self.findDevice(api,"printer")
        self.findDevice(api,'router')
        self.findDevice(api,'camera')
        self.findDevice(api,'nas')
        
    #set up the searching query of the API and run it
    def findDevice(self,api,keyword):

        query = 'ip: ' + self.ip + ' AND ' + keyword + ''
        print(query)
        page_count = 0
        for page in api.search(query,per_page=10,pages=-1):
            for i in range(len(page)):
                print(page[i])
                ##find ip
                ip = page[i].get("ip","None")
                content = "ip:" + ip + "\n"
                self.writeToFile(content)
                cur_path = os.path.dirname(__file__)
                filename = cur_path + "/log/cens_ip.log"
                f = open(filename,"a+")
                f.write(content)
                f.close()
                print("ip:"+ip)
                page_count+=1
                
                ##find os
                metadata_os = page[i].get("metadata.os","None")
                if(metadata_os == None):
                    metadata_os == "None"
                content = "os:" + metadata_os + "\n";
                self.writeToFile(content)
                print("os:"+metadata_os)
                
                ##find productModel
                productModel = page[i].get("metadata.description","None")
                if(productModel == None):
                    productModel == "None"
                content = "product_model:" + productModel + "\n"
                self.writeToFile(content)
                print("product_model:"+productModel)
                
                ##output devicetype
                content = "device_type:" + keyword + "\n"
                self.writeToFile(content)
                print("device_type:"+keyword)
                 
                ##find protocol
                count = len(page[i]["services"])
                if count > 0:
                    self.writeToFile("ports:")
                    for j in range(count):
                        port = page[i]["services"][j]["port"]
                        content = str(port) + " ";
                        print(content)
                        self.writeToFile(content)
                    self.writeToFile("\n")
    
        if page_count == 0 :
            print(self.ip+":not "+keyword)

if __name__ == "__main__":

    args = process_parser()

    #set up API info(ID, password, IP, device number)
    api_info = dict()
    #api_info['id'] = "558d0b15-07a5-47a4-b68f-b0530181f791"
    #api_info['secret'] = "YwgekK1zvhvmn2rjRmQPFblsKNIMlFwC"
    api_info['ip'] = args.ip
    api_info['count'] = args.count

    c = censys_engine(api_info)
    c.start()
