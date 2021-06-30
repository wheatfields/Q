# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:34:19 2021

@author: adamw
"""


import os
os.chdir(r"C:\Users\adamw\Documents\GitHub\Q")
path = r"C:\Users\adamw\Documents\SVA replica.xlsx"
current_product = 'CurrentProduct'
new_product = 'NewProduct'
import sva
# Initialise with path and sheetname
cp = sva.sva(path = path, sheet_name = current_product)
np = sva.sva(path = path, sheet_name = new_product)


cp_claims_reporting_delay = cp.claims_reporting_delay()[1]
np_claims_reporting_delay = np.claims_reporting_delay()[0]


help(np)

help(np.claims_reporting_delay)
