import pandas as pd

df=pd.read_csv('C:/Users/vijay/PycharmProjects/PythonProject/sample_employees.csv')


code_llm= """

import pandas as pd
import numpy as np

try:
    result = df[df['department'] == 'Marketing']
except KeyError:
    result = "Error: 'department' column not found in DataFrame."
except Exception as e:
    result = f"An unexpected error occurred: {e}"
"""

allowed_globals = {
        "__builtins__": __builtins__,
        "df": df,
    }
allowed_locals = {}

exec(code_llm, allowed_globals, allowed_locals)
print(allowed_locals['result'])