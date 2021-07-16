from flask import Flask,request,render_template,redirect,session
from neo4j import GraphDatabase
import csv
import neo4j 
import pandas as pd
from py2neo import cypher

uri = "bolt://44.195.67.117:7687"
password = "replenishment-particle-subprograms"
user = "neo4j"

            # connecting to server

graphDB_driver = GraphDatabase.driver(uri, auth=(user, password))
session = graphDB_driver.session()
            #session.run('create(:car {name: $vehicle})',vehicle="mercedes")

with open("Fraud.csv", mode='r') as file:
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
                        
            supplier_name = line[keys[0]]
            supplier_contact = line[keys[1]]
            supplier_tag = line[keys[2]]
            supplier_no = (line[keys[3]])
            relation_type = (line[keys[4]])
            customer_no = line[keys[5]]
            customer_id = line[keys[6]]
            cutomer_tag = (line[keys[7]])
              
            # query= "
            #     MERGE ("var1:supplier_no) 
            #     MERGE (var2:customer_no)
            #     MERGE (var1)-[:relation]->(var2)
            # "
            #session.run (query)
            session.run("MERGE ("+var1+":"+"deal_number"+ "{ number: \""+supplier_no+"\"})MERGE("+var2+":"+"deal_number"+ "{ number:\""+customer_no+"\"})MERGE("+var1+")-[article:"+relation_type+"]->("+var2+")")
            
            i =i+1
