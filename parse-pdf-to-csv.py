import tabula
import pandas as pd

file_path = './resources/input/SoPhuUBMTTQHN-1500201113838 tu 01.09-12.09.2024.pdf'
# read the first page, with flag lattice, the result table is at index 20
tables = tabula.read_pdf(file_path, pages='1', lattice=True, multiple_tables=True)
df1 = tables[20].replace('\r', ' ', regex=True)
# rename the columns of table, remove special \r chars
df1.rename(columns=lambda x: x.replace('\r', ' '), inplace=True)

# convert all remained pages, multiple tables flag false to get 1 table, remove duplicates headers
tables = tabula.read_pdf(file_path, pages='2-4', lattice=True, multiple_tables=False)
clean = tables[0].drop_duplicates()
df2 = clean.replace('\r', ' ', regex=True)
# copy first row to header, then drop that row
header = df2.iloc[0].values
df2.columns = header
df2.drop(index=0, axis=0, inplace=True)

# concat 2 pandas dataframes, drop rows with all empty values
result = pd.concat([df1, df2], ignore_index=True)
result.dropna(how='all', inplace=True, ignore_index=True)
# print(result)

result.to_csv(f'./resources/output/Agribank-1500201113838-0109-1209.csv', index=True)

# file_path = './resources/input/13.9 Quỹ Cứu trợ tiền mặt.pdf'
