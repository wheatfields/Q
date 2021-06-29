# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 12:17:06 2021

@author: adamw
"""


# SVA scape


import pandas as pd

path = r"C:\Users\adamw\Documents\SVA replica.xlsx"


# -----------------------------------------------------------------------------

# A function that takes a given 'area' of an excel document (by defining rows
# and columns), makes any high-level adjustments, and returns a dataframe.  

def table_import(sheet_name, 
                 columns, 
                 row_start, row_end,
                 header_row,
                 clear_first_n_rows = None, 
                 index_col=None,
                 trim_column_names = None,
                 trim_index_name = None):
    
    rows = row_end - row_start
    
    if header_row is not None:
        if isinstance(header_row, list)==False:
            header = header_row-1
        else:
            header = header_row
    else:
        header = None
        
    # [Will always be reference 0]
    table = pd.DataFrame(pd.read_excel(path, 
                  sheet_name = sheet_name,
                  header = header,
                  usecols = columns,
                  nrows = rows,
                  index_col = index_col)
                 )
    
    # SVA sometimes has a blank row between header and the start of  the data
    if clear_first_n_rows is not None:
        table = table.iloc[clear_first_n_rows:]
    
    # The way read_excel works means that if the header has already been 'seen'
    # in previous columns, it will add a trailing '.[number]'. This removes it. 
    if trim_column_names is not None:
        table.columns = table.columns.map(str)
        table.columns = table.columns.str.replace(r'\.\d+$', '') 

    if trim_index_name is not None:
        table.index.name = table.index.name.split('.')[0]
    
    # -----------------------
    # Add information on where the assumption came from in the workbook.
    # [Will always be reference 1]
    info = ['Sheet name = ' + sheet_name, 
            'Columns = ' + columns, 
            'Rows = ' + str(str(row_start) + ' to ' + str(row_end)), 
            'Header row = ' + str(header_row), 
            'How many rows after header cleared?  ' + str(clear_first_n_rows),
            'Column used for index = ' + str(index_col),
            'Column names trimmed?  ' + str(trim_column_names),
            'Index column name trimmed?  ' + str(trim_index_name),
            str(table.info())]
    # -----------------------
    
    return table, info

# -----------------------------------------------------------------------------


class newproduct:
    # Consider adding a .self reference to intitialise class with the sheet_name
    sheet_name = 'NewProduct'
    
    # 1
    claims_reporting_delay = table_import(sheet_name = 'NewProduct', 
                                          columns = 'B:J', 
                                          row_start  = 11, row_end = 305,
                                          header_row = 11, 
                                          clear_first_n_rows = 1, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
    # 1
    claim_delay_factors = table_import(sheet_name = 'NewProduct', 
                                          columns = 'L:T',
                                          row_start = 11, row_end = 305,
                                          header_row = 11, 
                                          clear_first_n_rows = 1, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
    
    # 2
    claims_expense_reserve = table_import(sheet_name = 'NewProduct',  
                                          columns = 'W:Z', 
                                          row_start = 11, row_end = 18,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)  
    # 2    
    operating_expense_perc_premium = table_import(sheet_name = 'NewProduct',  
                                          columns = 'AB:AE', 
                                          row_start = 11, row_end = 18,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True) 
    # 2
    budgeted_trustee_expense = table_import(sheet_name = 'NewProduct',  
                                          columns = 'AG:AI', 
                                          row_start = 11, row_end = 23,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
    # 2
    projected_trustee_expense = table_import(sheet_name = 'NewProduct',  
                                          columns = 'AK:AM', 
                                          row_start = 11, row_end = 21,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
    
    # 3
    ip_continuance_rates = table_import(sheet_name = 'NewProduct',  
                                          columns = 'AP:AT', 
                                          row_start = 11, row_end = 52,
                                          header_row = 11,
                                          clear_first_n_rows = 1, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
    # Manually renaming index here. 
    ip_continuance_rates[0].index.rename('Month', inplace=True)
    # 3
    class dlr_parameters:
            salary_replacement_ratio = table_import(sheet_name = 'NewProduct',  
                                          columns = 'AV:AW', 
                                          row_start = 11, row_end = 12,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
        
            continuing_retirement_benefit = table_import(sheet_name = 'NewProduct',  
                                          columns = 'AV:AW', 
                                          row_start = 11, row_end = 13,
                                          header_row = 11,
                                          clear_first_n_rows = 1, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)

            assumed_avg_age_at_disability = table_import(sheet_name = 'NewProduct',  
                                          columns = 'AV:AW', 
                                          row_start = 11, row_end = 14,
                                          header_row = 11,
                                          clear_first_n_rows = 2, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
            
            assumed_default_salary = table_import(sheet_name = 'NewProduct',  
                                          columns = 'AV:AW', 
                                          row_start = 11, row_end = 15,
                                          header_row = 11,
                                          clear_first_n_rows = 3, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)    
    
            payment_ratio = table_import(sheet_name = 'NewProduct',  
                                          columns = 'AV:AW', 
                                          row_start = 11, row_end = 16,
                                          header_row = 11,
                                          clear_first_n_rows = 4, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
            
            reopened_claims_reserves_loading = table_import(sheet_name = 'NewProduct',  
                                          columns = 'AV:AW', 
                                          row_start = 11, row_end = 17,
                                          header_row = 11,
                                          clear_first_n_rows = 5, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
            
            claim_index_rate = table_import(sheet_name = 'NewProduct',  
                                          columns = 'AV:AW', 
                                          row_start = 11, row_end = 18,
                                          header_row = 11,
                                          clear_first_n_rows = 6, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True) 

            benefit_indexation_month = table_import(sheet_name = 'NewProduct',  
                                          columns = 'AV:AW', 
                                          row_start = 11, row_end = 19,
                                          header_row = 11,
                                          clear_first_n_rows = 7, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)                 
    # 3
    ip_ibnr_adjustment = table_import(sheet_name = 'NewProduct',  
                                          columns = 'AY:AZ', 
                                          row_start = 11, row_end = 15,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
    
    # 4
    appeals_reserve_assumptions = table_import(sheet_name = 'NewProduct',  
                                          columns = 'BC:BE', 
                                          row_start = 11, row_end = 15,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
    # 4
    perc_of_appealed_claims_accepted = table_import(sheet_name = 'NewProduct',  
                                          columns = 'BC:BE', 
                                          row_start = 11, row_end = 17,
                                          header_row = 11,
                                          clear_first_n_rows = 5, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
    perc_of_appealed_claims_accepted[0].rename(index={0:'GOV', 1:'NONGOV'}, inplace=True)
    
    # 5
    decline_rate = table_import(sheet_name = 'NewProduct',  
                                          columns = 'BH:BK', 
                                          row_start = 11, row_end = 12,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = None)
    # 5
    decline_rate_delay = table_import(sheet_name = 'NewProduct',  
                                          columns = 'BH:BI', 
                                          row_start = 14, row_end = 21,
                                          header_row = 14,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
    # 5
    simultaneous_ip_tpd_decline = table_import(sheet_name = 'NewProduct',  
                                          columns = 'BK:BM', 
                                          row_start = 14, row_end = 22,
                                          header_row = 14,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
    
    # 6
    expected_loss_ratio_gov = table_import(sheet_name = 'NewProduct',  
                                          columns = 'BP:BS', 
                                          row_start = 1, row_end = 84,
                                          header_row = 11,
                                          clear_first_n_rows = 1, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
    # 6
    expected_loss_ratio_nongov = table_import(sheet_name = 'NewProduct',  
                                          columns = 'BU:BX', 
                                          row_start = 11, row_end = 84,
                                          header_row = 11,
                                          clear_first_n_rows = 1, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
    
    # 7
    payment_delay_factors = table_import(sheet_name = 'NewProduct',  
                                          columns = 'CA:CG', 
                                          row_start = 11, row_end = 35,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
    # 7
    payment_delay_factors_discrete = table_import(sheet_name = 'NewProduct',  
                                          columns = 'CI:CO', 
                                          row_start = 11, row_end = 35,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
    
    # 8
    average_claim_size = table_import(sheet_name = 'NewProduct',  
                                          columns = 'CR:DA', 
                                          row_start = 11, row_end = 12,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
    # 8
    acs_ip_linked_tpd = table_import(sheet_name = 'NewProduct',  
                                          columns = 'CR:CV', 
                                          row_start = 20, row_end = 32,
                                          header_row = 20,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
    # 8
    acs_by_notification_delay_q = table_import(sheet_name = 'NewProduct',  
                                          columns = 'CW:CY', 
                                          row_start = 20, row_end = 85,
                                          header_row = 20,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
    # 8
    perc_si_at_ip_doe = table_import(sheet_name = 'NewProduct',  
                                          columns = 'CZ:DA', 
                                          row_start = 20, row_end = 21,
                                          header_row = 20,
                                          clear_first_n_rows = 1, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
    # 8
    tpd_si_scales_by_age = table_import(sheet_name = 'NewProduct',  
                                          columns = 'CZ:DA', 
                                          row_start = 22, row_end = 76,
                                          header_row = 22,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)

    # 9
    class termination_rates():
        age_rates = table_import(sheet_name = 'NewProduct',  
                                              columns = 'DD:DF', 
                                              row_start = 11, row_end = 57,
                                              header_row = 11,
                                              clear_first_n_rows = 1, 
                                              index_col = 0,
                                              trim_column_names = True,
                                              trim_index_name = True)
      
        duration_of_claim_g_wp_oc = table_import(sheet_name = 'NewProduct',  
                                              columns = 'DH:EF', 
                                              row_start = 10, row_end = 134,
                                              header_row = 10,
                                              clear_first_n_rows = None, 
                                              index_col = 0,
                                              trim_column_names = True,
                                              trim_index_name = None)
        # Data adjustments here to correctly index table. 
        # Note: Consider 'melting' multi-index tables for use in models. 
        df = duration_of_claim_g_wp_oc[0].copy()
        info = duration_of_claim_g_wp_oc[1].copy()
        index = df[0:4]
        index = index.fillna(method='ffill', axis=1)
        df = df[4:]
        df.columns = pd.MultiIndex.from_arrays(index.values)
        df.index.name = 'Duration of Claim (months)'
        duration_of_claim_g_wp_oc = tuple([df, info])
        
        smoker_status = table_import(sheet_name = 'NewProduct',  
                                              columns = 'EH:EI', 
                                              row_start = 10, row_end = 12,
                                              header_row = 10,
                                              clear_first_n_rows = None, 
                                              index_col = 0,
                                              trim_column_names = True,
                                              trim_index_name = None)
        smoker_status[0].rename(columns={smoker_status[0].columns[0]: "smoker_status" }, inplace = True)
        
        benefit_type = table_import(sheet_name = 'NewProduct',  
                                              columns = 'EK:EL', 
                                              row_start = 10, row_end = 12,
                                              header_row = 10,
                                              clear_first_n_rows = None, 
                                              index_col = 0,
                                              trim_column_names = True,
                                              trim_index_name = None)
        benefit_type[0].rename(columns={benefit_type[0].columns[0]: "benefit_type" }, inplace = True)  
        
        policy_duration_factor = table_import(sheet_name = 'NewProduct',  
                                              columns = 'EN:ER', 
                                              row_start = 10, row_end = 23,
                                              header_row = 10,
                                              clear_first_n_rows = None, 
                                              index_col = 0,
                                              trim_column_names = True,
                                              trim_index_name = None)
        # Data adjustments here to correctly index table. 
        # Note: Consider 'melting' multi-index tables for use in models. 
        df = policy_duration_factor[0].copy()
        info = policy_duration_factor[1].copy()
        index = df[0:4]
        index = index.fillna(method='ffill', axis=1)
        df = df[4:]
        df.columns = pd.MultiIndex.from_arrays(index.values)
        df.index.name = 'Curtate Policy Year'
        policy_duration_factor = tuple([df, info])       

        
claim_delay_factors             = newproduct.claim_delay_factors[0]
claims_reporting_delay          = newproduct.claims_reporting_delay[0]
claims_expense_reserve          = newproduct.claims_expense_reserve[0]
operating_expense_perc_premium  = newproduct.operating_expense_perc_premium[0]
budgeted_trustee_expense        = newproduct.budgeted_trustee_expense[0]
projected_trustee_expense       = newproduct.projected_trustee_expense[0]
ip_continuance_rates            = newproduct.ip_continuance_rates[0]

# DRL Parameters. Using .squeeze() to extract single value. 
salary_replacement_ratio                    = newproduct.dlr_parameters.salary_replacement_ratio[0].squeeze()
continuing_retirement_benefit               = newproduct.dlr_parameters.continuing_retirement_benefit[0].squeeze()
assumed_avg_age_at_disability               = newproduct.dlr_parameters.assumed_avg_age_at_disability[0].squeeze()
assumed_default_salary                      = newproduct.dlr_parameters.assumed_default_salary[0].squeeze()
payment_ratio                               = newproduct.dlr_parameters.payment_ratio[0].squeeze()
reopened_claims_reserves_loading            = newproduct.dlr_parameters.reopened_claims_reserves_loading[0].squeeze()
claim_index_rate                            = newproduct.dlr_parameters.claim_index_rate[0].squeeze()
benefit_indexation_month                    = newproduct.dlr_parameters.benefit_indexation_month[0].squeeze()

ip_ibnr_adjustment              = newproduct.ip_ibnr_adjustment[0]
decline_rate                    = newproduct.decline_rate[0]
decline_rate_delay              = newproduct.decline_rate_delay[0]
simultaneous_ip_tpd_decline     = newproduct.simultaneous_ip_tpd_decline[0]
expected_loss_ratio_gov         = newproduct.expected_loss_ratio_gov[0]
expected_loss_ratio_nongov      = newproduct.expected_loss_ratio_nongov[0]
payment_delay_factors           = newproduct.payment_delay_factors[0]
payment_delay_factors_discrete  = newproduct.payment_delay_factors_discrete[0]
average_claim_size              = newproduct.average_claim_size[0]

acs_ip_linked_tpd               = newproduct.acs_ip_linked_tpd[0]
acs_by_notification_delay_q     = newproduct.acs_by_notification_delay_q[0]
perc_si_at_ip_doe               = newproduct.perc_si_at_ip_doe[0].squeeze()
tpd_si_scales_by_age            = newproduct.tpd_si_scales_by_age[0]

# Termination rates
age_rates                       = newproduct.termination_rates.age_rates[0]
duration_of_claim               = newproduct.termination_rates.duration_of_claim[0]
smoker_status                   = newproduct.termination_rates.smoker_status[0]
benefit_type                    = newproduct.termination_rates.benefit_type[0]



