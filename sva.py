# -*- coding: utf-8 -*-
"""
@author: adamw
"""

import pandas as pd

class sva:
    """
    Initialise with a path to the document & a sheet name. 
    """
    def __init__(self, path, sheet_name):
        self.path = path
        self.sheet_name = sheet_name
        
        self.dlr_parameters = self.dlr_parameters(path, sheet_name)
        self.termination_rates = self.termination_rates(path, sheet_name)
        self.stress_margins = self.stress_margins(path, sheet_name)
        
# =============================================================================
    @classmethod    
    def table_import(cls, path,
             sheet_name, 
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
        # # Add information on where the assumption came from in the workbook.
        # # [Will always be reference 1]
        # info = ['Path = ' + path,
        #         'Sheet name = ' + sheet_name, 
        #         'Columns = ' + columns, 
        #         'Rows = ' + str(str(row_start) + ' to ' + str(row_end)), 
        #         'Header row = ' + str(header_row), 
        #         'Number of rows after header cleared = ' + str(clear_first_n_rows),
        #         'Column used for index (0-indexed) = ' + str(index_col)
        #         ]
        # -----------------------
    
        return table
    # , info    
        
# =============================================================================
# 1         

    def claims_reporting_delay(self):
        """
        """
        claims_reporting_delay = self.table_import(path = self.path,
                                                    sheet_name = self.sheet_name, 
                                                    columns = 'B:J', 
                                                    row_start  = 11, row_end = 305,
                                                    header_row = 11, 
                                                    clear_first_n_rows = 1, 
                                                    index_col = 0,
                                                    trim_column_names = True,
                                                    trim_index_name = True)
        
        return claims_reporting_delay
    
    def claim_delay_factors(self):
        """
        """
        claim_delay_factors = self.table_import(path = self.path,
                                                sheet_name = self.sheet_name, 
                                                columns = 'L:T',
                                                row_start = 11, row_end = 305,
                                                header_row = 11, 
                                                clear_first_n_rows = 1, 
                                                index_col = 0,
                                                trim_column_names = True,
                                                trim_index_name = True)
        return claim_delay_factors

# =============================================================================
# 2
    
    def claims_expense_reserve(self):
        """
        """        
        claims_expense_reserve = self.table_import(path = self.path,
                                                sheet_name = self.sheet_name, 
                                              columns = 'W:Z', 
                                              row_start = 11, row_end = 18,
                                              header_row = 11,
                                              clear_first_n_rows = None, 
                                              index_col = 0,
                                              trim_column_names = True,
                                              trim_index_name = True)
        return claims_expense_reserve
       
    def operating_expense_perc_premium(self):
        """
        """
        operating_expense_perc_premium = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,   
                                          columns = 'AB:AE', 
                                          row_start = 11, row_end = 18,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True) 
        return operating_expense_perc_premium
    
    def budgeted_trustee_expense(self):
        """
        """
        budgeted_trustee_expense = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,   
                                          columns = 'AG:AI', 
                                          row_start = 11, row_end = 23,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
        return budgeted_trustee_expense
        
    def projected_trustee_expense(self):
        """
        """
        projected_trustee_expense = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,  
                                          columns = 'AK:AM', 
                                          row_start = 11, row_end = 21,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
        return projected_trustee_expense

# =============================================================================
# 3
        
    def ip_continuance_rates(self):
        """
        """
        ip_continuance_rates = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name, 
                                          columns = 'AP:AT', 
                                          row_start = 11, row_end = 52,
                                          header_row = 11,
                                          clear_first_n_rows = 1, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
        # Manually renaming index here. 
        ip_continuance_rates.index.rename('Month', inplace=True)
        return ip_continuance_rates

    class dlr_parameters:
        def __init__(self, path, sheet_name):
            self.path = path
            self.sheet_name = sheet_name
            
        def salary_replacement_ratio(self):
            """
            """
            salary_replacement_ratio = sva.table_import(path = self.path,
                                            sheet_name = self.sheet_name, 
                                          columns = 'AV:AW', 
                                          row_start = 11, row_end = 12,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
            return salary_replacement_ratio
        
        def continuing_retirement_benefit(self):
            """
            """
            continuing_retirement_benefit = self.table_import(path = self.path,
                                        sheet_name = self.sheet_name, 
                                      columns = 'AV:AW', 
                                      row_start = 11, row_end = 13,
                                      header_row = 11,
                                      clear_first_n_rows = 1, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = True)
            return continuing_retirement_benefit

        def assumed_avg_age_at_disability(self):
            """
            """
            assumed_avg_age_at_disability = self.table_import(path = self.path,
                                        sheet_name = self.sheet_name,  
                                      columns = 'AV:AW', 
                                      row_start = 11, row_end = 14,
                                      header_row = 11,
                                      clear_first_n_rows = 2, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = True)
            return assumed_avg_age_at_disability
        
        def assumed_default_salary(self):
            """
            """
            assumed_default_salary = self.table_import(path = self.path,
                                        sheet_name = self.sheet_name,  
                                      columns = 'AV:AW', 
                                      row_start = 11, row_end = 15,
                                      header_row = 11,
                                      clear_first_n_rows = 3, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = True) 
            return assumed_default_salary

        def payment_ratio(self):
            """
            """
            payment_ratio = self.table_import(path = self.path,
                                        sheet_name = self.sheet_name,   
                                      columns = 'AV:AW', 
                                      row_start = 11, row_end = 16,
                                      header_row = 11,
                                      clear_first_n_rows = 4, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = True)
            return payment_ratio
        
        def reopened_claims_reserves_loading(self):
            """
            """
            reopened_claims_reserves_loading = self.table_import(path = self.path,
                                        sheet_name = self.sheet_name,   
                                      columns = 'AV:AW', 
                                      row_start = 11, row_end = 17,
                                      header_row = 11,
                                      clear_first_n_rows = 5, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = True)
            return reopened_claims_reserves_loading
        
        def claim_index_rate(self):
            """
            """
            claim_index_rate = self.table_import(path = self.path,
                                        sheet_name = self.sheet_name,   
                                      columns = 'AV:AW', 
                                      row_start = 11, row_end = 18,
                                      header_row = 11,
                                      clear_first_n_rows = 6, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = True)
            return claim_index_rate

        def benefit_indexation_month(self):
            """
            """
            benefit_indexation_month = self.table_import(path = self.path,
                                        sheet_name = self.sheet_name,   
                                      columns = 'AV:AW', 
                                      row_start = 11, row_end = 19,
                                      header_row = 11,
                                      clear_first_n_rows = 7, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = True)
            return benefit_indexation_month
            
    def ip_ibnr_adjustment(self):
        """
        """
        ip_ibnr_adjustment = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,   
                                          columns = 'AY:AZ', 
                                          row_start = 11, row_end = 15,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
        return ip_ibnr_adjustment

# =============================================================================
# 4
        
    def appeals_reserve_assumptions(self):
        """
        """
        appeals_reserve_assumptions = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,   
                                          columns = 'BC:BE', 
                                          row_start = 11, row_end = 15,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
        return appeals_reserve_assumptions
    
    def perc_of_appealed_claims_accepted(self):
        """
        """
        perc_of_appealed_claims_accepted= self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,   
                                          columns = 'BC:BE', 
                                          row_start = 11, row_end = 17,
                                          header_row = 11,
                                          clear_first_n_rows = 5, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
        perc_of_appealed_claims_accepted.rename(index={0:'GOV', 1:'NONGOV'}, inplace=True)
        return perc_of_appealed_claims_accepted

# =============================================================================
# 5
        
    def decline_rate(self):
        """
        """
        decline_rate = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,   
                                          columns = 'BH:BK', 
                                          row_start = 11, row_end = 12,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = None)
        return decline_rate
    
    def decline_rate_delay(self):
        """
        """
        decline_rate_delay = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,   
                                          columns = 'BH:BI', 
                                          row_start = 14, row_end = 21,
                                          header_row = 14,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
        return decline_rate_delay

    def simultaneous_ip_tpd_decline(self):
        """
        """
        simultaneous_ip_tpd_decline = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,   
                                          columns = 'BK:BM', 
                                          row_start = 14, row_end = 22,
                                          header_row = 14,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
        return simultaneous_ip_tpd_decline 

# =============================================================================
# 6
        
    def expected_loss_ratio_gov(self):
        """
        """
        expected_loss_ratio_gov = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,  
                                          columns = 'BP:BS', 
                                          row_start = 1, row_end = 84,
                                          header_row = 11,
                                          clear_first_n_rows = 1, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
        return expected_loss_ratio_gov
    
    def expected_loss_ratio_nongov(self):
        """
        """
        expected_loss_ratio_nongov = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,  
                                          columns = 'BU:BX', 
                                          row_start = 11, row_end = 84,
                                          header_row = 11,
                                          clear_first_n_rows = 1, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
        return expected_loss_ratio_nongov

# =============================================================================
# 7
        
    def payment_delay_factors(self):
        """
        """
        payment_delay_factors = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,  
                                          columns = 'CA:CG', 
                                          row_start = 11, row_end = 35,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
        return payment_delay_factors
    # 7
    def payment_delay_factors_discrete(self):
        """
        """
        payment_delay_factors_discrete = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,   
                                          columns = 'CI:CO', 
                                          row_start = 11, row_end = 35,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
        return payment_delay_factors_discrete

# =============================================================================
# 8
    
    def average_claim_size(self):
        """
        """
        average_claim_size = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,   
                                          columns = 'CR:DA', 
                                          row_start = 11, row_end = 12,
                                          header_row = 11,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
        return average_claim_size

    def acs_ip_linked_tpd(self):
        """
        """
        acs_ip_linked_tpd = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,   
                                          columns = 'CR:CV', 
                                          row_start = 20, row_end = 32,
                                          header_row = 20,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
        return acs_ip_linked_tpd

    def acs_by_notification_delay_q(self):
        """
        """
        acs_by_notification_delay_q = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,  
                                          columns = 'CW:CY', 
                                          row_start = 20, row_end = 85,
                                          header_row = 20,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
        return acs_by_notification_delay_q
    
    def perc_si_at_ip_doe(self):
        """
        """
        perc_si_at_ip_doe = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,   
                                          columns = 'CZ:DA', 
                                          row_start = 20, row_end = 21,
                                          header_row = 20,
                                          clear_first_n_rows = 1, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
        return perc_si_at_ip_doe
    
    def tpd_si_scales_by_age(self):
        """
        """
        tpd_si_scales_by_age = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,   
                                          columns = 'CZ:DA', 
                                          row_start = 22, row_end = 76,
                                          header_row = 22,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = True)
        return tpd_si_scales_by_age 

# =============================================================================
# 9
        
    class termination_rates:
        def __init__(self, path, sheet_name):
            self.path = path
            self.sheet_name = sheet_name
        
        def age_rates(self):
            """
            """
            age_rates = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,  
                                              columns = 'DD:DF', 
                                              row_start = 11, row_end = 57,
                                              header_row = 11,
                                              clear_first_n_rows = 1, 
                                              index_col = 0,
                                              trim_column_names = True,
                                              trim_index_name = True)
            return age_rates
      
        def duration_of_claim_g_wp_oc(self):
            """
            """
            duration_of_claim_g_wp_oc = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,  
                                              columns = 'DH:EF', 
                                              row_start = 10, row_end = 134,
                                              header_row = 10,
                                              clear_first_n_rows = None, 
                                              index_col = 0,
                                              trim_column_names = True,
                                              trim_index_name = None)
            # Data adjustments here to correctly index table. 
            # Note: Consider 'melting' multi-index tables for use in models. 
            df = duration_of_claim_g_wp_oc.copy()
            # info = duration_of_claim_g_wp_oc[1].copy()
            index = df[0:4]
            index = index.fillna(method='ffill', axis=1)
            df = df[4:]
            df.columns = pd.MultiIndex.from_arrays(index.values)
            df.index.name = 'Duration of Claim (months)'
            # duration_of_claim_g_wp_oc = tuple([df, info])
            duration_of_claim_g_wp_oc = df
            return duration_of_claim_g_wp_oc
        
        def smoker_status(self):
            """
            """
            smoker_status = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,   
                                              columns = 'EH:EI', 
                                              row_start = 10, row_end = 12,
                                              header_row = 10,
                                              clear_first_n_rows = None, 
                                              index_col = 0,
                                              trim_column_names = True,
                                              trim_index_name = None)
            smoker_status.rename(columns={smoker_status.columns[0]: "smoker_status" }, inplace = True)
            return smoker_status
        
        def benefit_type(self):
            """
            """
            benefit_type = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name, 
                                              columns = 'EK:EL', 
                                              row_start = 10, row_end = 12,
                                              header_row = 10,
                                              clear_first_n_rows = None, 
                                              index_col = 0,
                                              trim_column_names = True,
                                              trim_index_name = None)
            benefit_type.rename(columns={benefit_type.columns[0]: "benefit_type" }, inplace = True)  
            return benefit_type
        
        def policy_duration_factor(self):
            """
            """
            policy_duration_factor = self.table_import(path = self.path,
                                            sheet_name = self.sheet_name,   
                                              columns = 'EN:ER', 
                                              row_start = 10, row_end = 23,
                                              header_row = 10,
                                              clear_first_n_rows = None, 
                                              index_col = 0,
                                              trim_column_names = True,
                                              trim_index_name = None)
            # Data adjustments here to correctly index table. 
            # Note: Consider 'melting' multi-index tables for use in models. 
            df = policy_duration_factor.copy()
            # info = policy_duration_factor[1].copy()
            index = df[0:2]
            index = index.fillna(method='ffill', axis=1)
            df = df[2:]
            df.columns = pd.MultiIndex.from_arrays(index.values)
            df.index.name = 'Curtate Policy Year'
            # policy_duration_factor = tuple([df, info])  
            policy_duration_factor = df
            return policy_duration_factor

# =============================================================================
# 10

    class stress_margins:
        
        def __init__(self, path, sheet_name):
            self.path = path
            self.sheet_name = sheet_name     
            self.random = self.random(path, sheet_name)
            self.future = self.future(path, sheet_name)
        
        class random:
            def __init__(self, path, sheet_name):
                  self.path = path
                  self.sheet_name = sheet_name           
            
            def random_all(self):
                random_all = sva.table_import(path = self.path,
                                        sheet_name = self.sheet_name,   
                                          columns = 'FL:FM', 
                                          row_start = 16, row_end = 26,
                                          header_row = 16,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = None)   
                return random_all
            
            def death(self):
                death = self.random_all().iloc[0,0]
                return death

            def death_ibnr(self):
                death_ibnr = self.random_all().iloc[1,0]
                return death_ibnr

            def death_rbna(self):
                death_rbna = self.random_all().iloc[2,0]
                return death_rbna

            def tpd(self):
                tpd = self.random_all().iloc[3,0]
                return tpd

            def tpd_ibnr(self):
                tpd_ibnr = self.random_all().iloc[4,0]
                return tpd_ibnr

            def tpd_rbna(self):
                tpd_rbna = self.random_all().iloc[5,0]
                return tpd_rbna
            
            def ip(self):
                ip = self.random_all().iloc[6,0]
                return ip

            def ip_dlr(self):
                ip_dlr = self.random_all().iloc[7,0]
                return ip_dlr

            def ip_ibnr(self):
                ip_ibnr = self.random_all().iloc[8,0]
                return ip_ibnr

            def ip_rbna(self):
                ip_rbna = self.random_all().iloc[9,0]
                return ip_rbna
            
        class future:
            def __init__(self, path, sheet_name):
                  self.path = path
                  self.sheet_name = sheet_name           
            
            def future_all(self):
                future_all = sva.table_import(path = self.path,
                                        sheet_name = self.sheet_name,   
                                          columns = 'FL:FM', 
                                          row_start = 27, row_end = 37,
                                          header_row = 27,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = None)   
                return future_all
            
            def death(self):
                death = self.future_all().iloc[0,0]
                return death

            def death_ibnr(self):
                death_ibnr = self.future_all().iloc[1,0]
                return death_ibnr

            def death_rbna(self):
                death_rbna = self.future_all().iloc[2,0]
                return death_rbna

            def tpd(self):
                tpd = self.future_all().iloc[3,0]
                return tpd

            def tpd_ibnr(self):
                tpd_ibnr = self.future_all().iloc[4,0]
                return tpd_ibnr

            def tpd_rbna(self):
                tpd_rbna = self.future_all().iloc[5,0]
                return tpd_rbna
            
            def ip(self):
                ip = self.future_all().iloc[6,0]
                return ip

            def ip_dlr(self):
                ip_dlr = self.future_all().iloc[7,0]
                return ip_dlr

            def ip_ibnr(self):
                ip_ibnr = self.future_all().iloc[8,0]
                return ip_ibnr

            def ip_rbna(self):
                ip_rbna = self.future_all().iloc[9,0]
                return ip_rbna  
          
        def time_to_react_future(self):
            time_to_react_future = 1
# =============================================================================
# 11

class test:
    print('yes')

# =============================================================================
# 12



# =============================================================================
# 13


        
# =============================================================================
# 14


      
# =============================================================================
# 15


         
# =============================================================================
# 16



# =============================================================================
# 17



# =============================================================================
# 18



# =============================================================================
# 19



# =============================================================================
# 20



# =============================================================================
# 21



# =============================================================================


# newproduct = newproduct(path = r"C:\Users\adamw\Documents\SVA replica.xlsx", sheet_name='NewProduct')       
# claim_delay_factors             = sva.claim_delay_factors[0]
# claims_reporting_delay          = sva.claims_reporting_delay[0]
# claims_expense_reserve          = sva.claims_expense_reserve[0]
# operating_expense_perc_premium  = sva.operating_expense_perc_premium[0]
# budgeted_trustee_expense        = sva.budgeted_trustee_expense[0]
# projected_trustee_expense       = sva.projected_trustee_expense[0]
# ip_continuance_rates            = newproduct.ip_continuance_rates[0]

# # DRL Parameters. Using .squeeze() to extract single value. 
# salary_replacement_ratio                    = sva.dlr_parameters.salary_replacement_ratio[0].squeeze()
# continuing_retirement_benefit               = sva.dlr_parameters.continuing_retirement_benefit[0].squeeze()
# assumed_avg_age_at_disability               = sva.dlr_parameters.assumed_avg_age_at_disability[0].squeeze()
# assumed_default_salary                      = sva.dlr_parameters.assumed_default_salary[0].squeeze()
# payment_ratio                               = sva.dlr_parameters.payment_ratio[0].squeeze()
# reopened_claims_reserves_loading            = sva.dlr_parameters.reopened_claims_reserves_loading[0].squeeze()
# claim_index_rate                            = sva.dlr_parameters.claim_index_rate[0].squeeze()
# benefit_indexation_month                    = sva.dlr_parameters.benefit_indexation_month[0].squeeze()

# ip_ibnr_adjustment              = sva.ip_ibnr_adjustnt[0]
# decline_rate                    = sva.decline_rate[0]
# decline_rate_delay              = sva.decline_rate_delay[0]
# simultaneous_ip_tpd_decline     = sva.simultaneous_ip_tpd_decline[0]
# expected_loss_ratio_gov         = sva.expected_loss_ratio_gov[0]
# expected_loss_ratio_nongov      = sva.expected_loss_ratio_nongov[0]
# payment_delay_factors           = sva.payment_delay_factors[0]
# payment_delay_factors_discrete  = sva.payment_delay_factors_discrete[0]
# average_claim_size              = sva.average_claim_size[0]

# acs_ip_linked_tpd               = sva.acs_ip_linked_tpd[0]
# acs_by_notification_delay_q     = sva.acs_by_notification_delay_q[0]
# perc_si_at_ip_doe               = sva.perc_si_at_ip_doe[0].squeeze()
# tpd_si_scales_by_age            = sva.tpd_si_scales_by_age[0]

# # Termination rates
# age_rates                       = sva.termination_rates.age_rates[0]
# duration_of_claim_g_wp_oc       = sva.termination_rates.duration_of_claim_g_wp_oc[0]
# smoker_status                   = sva.termination_rates.smoker_status[0]
# benefit_type                    = sva.termination_rates.benefit_type[0]
# policy_duration_factor          = sva.termination_rates.policy_duration_factor[0]
