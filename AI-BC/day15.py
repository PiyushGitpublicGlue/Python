import os
from dotenv import load_dotenv
import sys
#from os import *
#os.getenv()
#getenv()

#list down all the env variable
#print(os.environ) # output is of dictionary like obj

# get specifiv env variables
# print(os.environ['PATH'])

#OR
#print(os.getenv('PATH'))

# add key to env
#os.environ['PiyushKey'] = 'jhdjhljdwhk7362838932dfbdbd99'
#print(os.getenv('PiyushKey'))
#print(os.getenv('PATH'))
#print(os.getenv('openapikey'))


load_dotenv(".env."+sys.argv[1])
print(os.getenv('TestingKey'))
# cli calling -> py .\day15.py qa
