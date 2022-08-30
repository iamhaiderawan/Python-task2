import pandas as pd
from openpyxl.workbook import Workbook

readfile = pd.read_csv("file1.csv")

readfile.to_excel("file2.xlsx",
index=None, header=True)