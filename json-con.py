<<<<<<< HEAD
"""
If we can get the data as a dataframe it is pretty simple to convert to JSON file
so that should be our objective
"""


import pandas as pd


def con_JSON(data):
    js = df.to_json('example.json',orient = 'records')
    print(js)


df = pd.DataFrame([['JK12',16,12],
                   ['RR1',19,100],
                   ['M332',2,89]],
                  columns = ['mdf','qty','price'])

print(df)
=======
"""
If we can get the data as a dataframe it is pretty simple to convert to JSON file
so that should be our objective
"""


import pandas as pd


def con_JSON(data):
    js = df.to_json('example.json',orient = 'records')
    print(js)


df = pd.DataFrame([['JK12',16,12],
                   ['RR1',19,100],
                   ['M332',2,89]],
                  columns = ['mdf','qty','price'])

print(df)
>>>>>>> 58db708aa0a9ec61fb5c36a63c538cc449b60d6f
con_JSON(df)