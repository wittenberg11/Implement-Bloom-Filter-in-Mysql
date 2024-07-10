Language: Python ![](https://img.shields.io/badge/-ChatGPT-412991?style=flat-square&logo=openai&logoColor=FFFFFF)

## Introduction
Here is a python implementation of bloom filter in mysql, we merge the bloom filter's add, check, reset operation with mysql's insert, select, and truncate operations. 
Additionally, we ensure the filter is persisted to disk aftereach commit operation To maintain consistency between the Bloom Filter and the table in mysql.

## Running
To run this project, you need:   
1. Firstly, install a mysql server in your PC.    
2. Secondly, edit the config.ini file, which is configure of mysql database.    
3. Thirdly, run main.py to see if it works.     

## Improve Direction
To impove this project, you can chose these directions:    
1: change mysql to another database, like oracle.    
2: use other hash methods, like double-hashing method.     
3: use Scalable Bloom Filter, SBF to adapt to changes in the amount of data.    

