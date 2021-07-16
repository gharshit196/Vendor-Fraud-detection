from flask import Flask,request,render_template,redirect,session
from neo4j import GraphDatabase
import csv
import neo4j 
import pandas as pd
from py2neo import cypher
from py2neo.data import Relationship

uri = "bolt://44.195.67.117:7687"
password = "replenishment-particle-subprograms"
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
            var1 = "test"+str(i)
            var2 = "temp"+str(i)
                        
            seller_id = line[keys[0]]
            relationship = line[keys[1]]
            customer_id= line[keys[2]]
            seller_jurisdiction = (line[keys[3]])
            seller_nature= (line[keys[4]])
            customer_jurisdiction = line[keys[5]]
            customer_nature= line[keys[6]]
            #cutomer_tag = (line[keys[7]])
              
            query= """
                MERGE (var1:seller {sel: seller_id, seljuris: seller_jurisdiction, selnature: seller_nature})
                MERGE (var2:customer {cus: customer_id, cusjuris: customer_jurisdiction, cusnature:customer_nature})
                MERGE (var1)-[:relation{rel:relationship}]->(var2)
            """
            session.run (query)
            #session.run("MERGE ("+var1+":"+"deal_number"+ "{ number: \""+supplier_no+"\"})MERGE("+var2+":"+"deal_number"+ "{ number:\""+customer_no+"\"})MERGE("+var1+")-[article:"+relation_type+"]->("+var2+")")
            
            i =i+1
