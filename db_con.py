import os
import psycopg2
from psycopg2.extras import RealDictCursor

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
    curr = conn.cursor(cursor_factory=RealDictCursor)
    queries = tables()

    for query in queries:
        curr.execute(query)
    conn.commit()

def tables():
    users = """CREATE TABLE IF NOT EXISTS users (
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
    
    incidences = """CREATE TABLE IF NOT EXISTS incidences (
        id SERIAL PRIMARY KEY,
        createdOn timestamp with time zone DEFAULT('now'::text)::date NOT NULL,
        createdBy integer NOT NULL references users (id),
        type VARCHAR(255) NOT NULL,
        location VARCHAR(255) NOT NULL,
        status VARCHAR(255) NOT NULL,
        comment VARCHAR(255) NOT NULL
        )"""
        
    queries = [users,incidences]
    return queries

def destroy_tables():
    users = """DROP TABLE IF EXISTS users CASCADE"""
    incidences = """DROP TABLE IF EXISTS incidents CASCADE"""
    pass