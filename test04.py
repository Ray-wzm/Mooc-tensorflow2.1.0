import os
import pandas as pd
os.environ["CUDA_VISIBLE_DEVICES"] = '-1'#禁用GPU
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# df = pd.read_csv('D:/BYSJ/data/uk_rain_2014/new_uk_rain.csv')
# df.head(5)
# df.describe()
# df[df.water_year.str.startswith('199')]

#---单独提取出某个列----------
# def base_year(year):
#     base_year = year[:4]
#     base_year = pd.to_datetime(base_year).year
#     return base_year
# df['year'] = df.water_year.apply(base_year)
# df.head(5)
#--------------------------

group_by_object = df.groupby(df.year // 10*10)
group_by_object.max()