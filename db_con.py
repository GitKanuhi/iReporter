import os
import psycopg2

url="dbname='ireporter' host='localhost' port='5432' user='andela' password='pass123'"

db_url = os.getenv('DATABASE_URL')

def connection (url):
    conn=psycopg2.connect(url)
    return conn

def init_db():
    conn = connection(url)
    return conn

def create_tables():
    """ function to create tables """
    conn = connection(url)
    curr = conn.cursor() # creating my cursor
    queries = tables()  # calling tables

    for query in queries:
        curr.execute(query)
    conn.commit()

def destroy_tables():
    db1 = """DROP TABLE IF EXISTS users CASCADE"""
    db2 = """DROP TABLE IF EXISTS incidents CASCADE"""
    pass

def tables():
    db1 = """CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        firstname VARCHAR(255) NOT NULL,
        lastname VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phonenumber VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        registered timestamp with time zone DEFAULT('now'::text)::date NOT NULL,
        isAdmin BOOLEAN NOT NULL
        )"""
    
    db2 = """CREATE TABLE IF NOT EXISTS incidents (
        id SERIAL PRIMARY KEY,
        createdOn timestamp with time zone DEFAULT('now'::text)::date NOT NULL,,
        createdBy VARCHAR(255) NOT NULL,
        type VARCHAR(255) NOT NULL,
        location VARCHAR(255) NOT NULL,
        status VARCHAR(255) NOT NULL,
        comment VARCHAR(255) NOT NULL
        )"""

        queries = [db1,db2]
        return queries

