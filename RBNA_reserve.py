# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 16:17:40 2021

@author: adamw
"""

import pandas as pd
df = pd.read_excel(r"C:\Users\adamw\Documents\GitHub\Q\Data_InputFile_RBNA Model_2.0_MAY2021.xlsx")



# =============================================================================
# Assumptions
import os
os.chdir(r"C:\Users\adamw\Documents\GitHub\Q")
path = r"C:\Users\adamw\Documents\SVA replica.xlsx"
current_product = 'CurrentProduct'
new_product = 'NewProduct'
import sva
sva = sva.sva(path=path, sheet_name=new_product)

valuation_date = 1
decline_rate = sva.decline_rate()
decline_rate_delay = sva.decline_rate_delay()
appeals_reserve_assumptions = sva.appeals_reserve_assumptions()
simultaneous_ip_tpd_decline = sva.simultaneous_ip_tpd_decline()
payment_delay_factors_discrete = sva.payment_delay_factors_discrete()
average_claim_size = sva.average_claim_size()
reinsurance = sva.reinsurance()

# =============================================================================
# Assumptions transformation

decline_rate_delay['Product'] = 'TPD'
decline_rate_delay['Gov'] = 'Gov'
decline_rate_delay['Policy Version'] = 'V1.2'
decline_rate_delay_2 = decline_rate_delay.copy()
decline_rate_delay_2['Policy Version'] = 'V1.3'
decline_rate_delay_3 = decline_rate_delay.copy()
decline_rate_delay_2['Policy Version'] = 'VLP'

decline_rate_delay_2 = decline_rate_delay_2.append(decline_rate_delay_3)
decline_rate_delay = decline_rate_delay.append(decline_rate_delay_2)

decline_rate_delay = decline_rate_delay.reset_index()

decline_rate_iterables = [['V1.2', 'V1.3', 'VLP'], 
                          ['DTH', 'TPD'], 
                          ['Gov', 'NonGov'],
                          [0, 0.5, 1, 1.5, 2.5, 3.5, '4+']]


temp_index = pd.MultiIndex.from_product(decline_rate_iterables, names=['Policy Version', 
                                                                        'Product',
                                                                        'Gov', 
                                                                        'Delay Years'])
temp = pd.DataFrame(index=temp_index)
temp = temp.merge(decline_rate_delay, how = 'left', on = ['Policy Version', 'Product', 'Gov', 'Delay Years']).drop_duplicates()
temp = temp.set_index(temp_index)



# =============================================================================

# Data mapping

product_mapping = [ ['VLP',  'Terminal Illness Benefit.',               'DTH'], 
                    ['V1.2', 'Death Benefit.',                          'DTH'], 
                    ['V1.3', 'Death Benefit.',                          'DTH'],
                    ['V1.2', 'Total and Permanent Disability Benefit.', 'TPD'],
                    ['V1.3', 'Total and Permanent Disability Benefit.', 'TPD'],
                    ['V1.2', 'Terminal Illness Benefit.',               'TPD'],
                    ['V1.3', 'Terminal Illness Benefit.',               'TPD']  ]

product_mapping = pd.DataFrame(product_mapping, columns = ['Policy Version', 'Claim Type', 'Product'])

gov_non_gov_mapping = [ ['QI Contributory Accumulation',                            'Gov'],
                        ['QI Basic Accumulation Contributory (Casual)',             'Gov'],
                        ['QI Police',                                               'Gov'],
                        ['QI Defined Benefit',                                      'Gov'],
                        ['QI Basic Accumulation Contributory (Full and Part Time)', 'Gov'],
                        ['QI Parliamentary',                                        'Gov'],
                        ['QI Inactive Government',                               'NonGov'],
                        ['QI Open Fund (Individual) - Full and Part Time',       'NonGov'],
                        ['QI Inactive Open Fund',                                'NonGov'],
                        ['QI Open Fund (Individual) - Casual',                   'NonGov'],
                        ['QI Open Fund (Individual) - Self Employed',            'NonGov'],
                        ['QI Open Fund (Individual) - Unemployed',               'NonGov']  ]

gov_non_gov_mapping = pd.DataFrame(gov_non_gov_mapping, columns = ['Insurance Category', 'Gov'])

df = df.merge(product_mapping, how='left', on = ['Policy Version', 'Claim Type'])
df = df.merge(gov_non_gov_mapping, how='left', on = 'Insurance Category')

# =============================================================================


# Lump Sum RBNA


df
