from flask import Flask,request,render_template,redirect,session
from neo4j import GraphDatabase
import csv
import neo4j 
#import pandas as pd
from py2neo import cypher
from py2neo.data import Relationship

uri = "bolt://44.192.63.184:7687"
password = "broom-revolution-regulations"
user = "neo4j"

            # connecting to server

graphDB_driver = GraphDatabase.driver(uri, auth=(user, password))
session = graphDB_driver.session()
            #session.run('create(:car {name: $vehicle})',vehicle="mercedes")

with open("DataForAnalysis.csv", mode='r') as file:
    #fieldnames = ['supplier_name', 'supplier_contact', 'supplier_tag', 'supplier_no', 'relation', 'customer_no', 'customer_code', 'customer_tag']
    reader = csv.DictReader(file)

    keys = reader.fieldnames

    node = []
    created = []
    i = 0
    graph_db = neo4j.GraphDatabase()
    
    for line in reader: 
            #var1 = "test"+str(i)
            #var2 = "temp"+str(i)
                        
            seller_id = line[keys[0]]
            relationship = line[keys[1]]
            customer_id= line[keys[2]]
            seller_jurisdiction = (line[keys[3]])
            seller_nature= (line[keys[4]])
            customer_jurisdiction = line[keys[5]]
            customer_nature= line[keys[6]]
            
            # seller_id = line[keys[0]]
            # relationship = line[keys[3]]
            # customer_id= line[keys[2]]
            # customer_id2= line[keys[4]]
            # seller_jurisdiction = (line[keys[5]])
            # seller_nature= line[keys[6]]
            # customer_jurisdiction = line[keys[7]]
            # customer_nature= line[keys[8]]
            # customer_jurisdiction = line[keys[9]]
            # customer_nature= line[keys[10]]
         
            query= """
                MERGE (s:seller {SellerId:seller_id, SellJurisdiction:seller_jurisdiction, SellNature:seller_nature})
                MERGE (c:customer {CustomerId: customer_id, CustomerJurisdiction: customer_jurisdiction, CustomerNature:customer_nature})
                MERGE (s)-[r:SellTo]->(c)
                RETURN s,c
            """

            # query= """
            #     MERGE (s:seller {SellerId:line[0], SellJurisdiction: line[5], SellerNature:line[6]}) 
            #     MERGE (c:customer1 {CustomerId:line[2], CustomerJurisdiction: line[7], CustomerNature:line[8]}) 
            #     CREATE (f:customer2 {CustomerId2:line[4], CustomerJurisdiction2:line[9],CustomerNature2:line[10]})
            #     CREATE (r2:relation{relationship:line[3]})
            #     MERGE (s)-[r1:SellTo]->(c) 
            #     CREATE (c)-[r2]->(f) 
            #     RETURN s,c,f
            # """
            session.run (query)
            #session.run("MERGE ("+var1+":"+"deal_number"+ "{ number: \""+supplier_no+"\"})MERGE("+var2+":"+"deal_number"+ "{ number:\""+customer_no+"\"})MERGE("+var1+")-[article:"+relation_type+"]->("+var2+")")
            
            i =i+1
