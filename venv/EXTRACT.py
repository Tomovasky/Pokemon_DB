# This will be the first stage of extracting data from the pokmon API
#API is found here https://pokeapi.co/
#Fist check to make sure we have request installed in virtial eviorment.
# open turminal and pip install requests
#okay, pip in now installed, time to import
import requests
import pandas as pd
from tabulate import tabulate
#Code runs without issues.
'''
Wait, you don't know request is for? This is the main libarty in Python for acessing an API
For more infomation ceck the documenation here: https://docs.python-requests.org/en/latest/
'''
#Test pull with Ditto info
respons =requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
#test to make sure the data is correct.

#test what text looks like.
dito_text = respons.text

#testing calling the data in jason format
ditio_json = respons.json()


#Okay, we have the data but now what to do with it.
# I don't feel as the text or json are very easy to read.
#What if we change this in to a data fram.... time to import pandas!!!
#well first we need to add pandas to the VE.
#Temainl: pip install pandas
#ADD import pandsas above as you always want to have your imporst together
#for readbility.
#Now Pandas is installed, but we want to handel th Json data What was the
#libary called....Google Searching ... pandas.json_normalize
#ohh there is a pandas.io.json.build_table_schema libary as well.
# I had planned on looking into SQLALCAHCME, but it may not be needed.
#BUt that is for another section now it is time to work wiht pandas.json_normalize
#opps  forgot to alias pandas as pd. Coding nolcatture.
#well we seem to be getting on some of the dataframe, let have them print all
pd.set_option("display.max_rows", None, "display.max_columns", None)
ditto_df = pd.json_normalize(ditio_json)


#okay as I'm plaaning on running this into a db. Let's try the pandas.io.json.build_table_schema
#test_schema = pd.io.json.build_table_schema(ditio_json) gave error
#AttributeError: 'dict' object has no attribute 'index'
#HMM, the error talks about index, and build_table has an argument for index that is set for True.
#So one couls assume that chaning the index to False will fix the above isssue
test_schema = pd.io.json.build_table_schema(ditto_df,index=False)
#Good news, I was right that seems to have fixed my issue... bad news
# New error: AttributeError: 'dict' object has no attribute 'ndim'
#HMMM... well this one is not as easy as just looking at the doc.
#Google time! Okay, a few faild google attemps, but I got the idea that maybe it would work on the df not the json format
#chekce and test_schema = pd.io.json.build_table_schema(ditto_df,index=False) with no erros
print(tabulate(test_schema, headers= "keys"))
#okay, nice we can now see what the schema would look like... but it's alittle hard to read. lets try from tabulate
# import tabulate
#lets call this a night


