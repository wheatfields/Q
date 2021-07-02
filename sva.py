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
        
        # initiate nested classes
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
                header = header_row - 1
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

        return table
        
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
            continuing_retirement_benefit = sva.table_import(path = self.path,
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
            assumed_avg_age_at_disability = sva.table_import(path = self.path,
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
            assumed_default_salary = sva.table_import(path = self.path,
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
            payment_ratio = sva.table_import(path = self.path,
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
            reopened_claims_reserves_loading = sva.table_import(path = self.path,
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
            claim_index_rate = sva.table_import(path = self.path,
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
            benefit_indexation_month = sva.table_import(path = self.path,
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
                                          row_start = 11, row_end = 84,
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
                                          row_start = 19, row_end = 20,
                                          header_row = 19,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = None,
                                          trim_index_name = None)
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
            age_rates = sva.table_import(path = self.path,
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
            duration_of_claim_g_wp_oc = sva.table_import(path = self.path,
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
            smoker_status = sva.table_import(path = self.path,
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
            benefit_type = sva.table_import(path = self.path,
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
            policy_duration_factor = sva.table_import(path = self.path,
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
            time_to_react_future = sva.table_import(path = self.path,
                                        sheet_name = self.sheet_name,   
                                          columns = 'FL:FM', 
                                          row_start = 39, row_end = 40,
                                          header_row = 39,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = None).iloc[0,0]
            return time_to_react_future
        
        def event_pandemic_death(self):
            event_pandemic_death = sva.table_import(path = self.path,
                                        sheet_name = self.sheet_name,   
                                          columns = 'FL:FM', 
                                          row_start = 42, row_end = 46,
                                          header_row = 42,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = None).iloc[0,0]
            return event_pandemic_death
        
        def event_pandemic_tpd(self):
            event_pandemic_tpd = sva.table_import(path = self.path,
                                        sheet_name = self.sheet_name,   
                                          columns = 'FL:FM', 
                                          row_start = 42, row_end = 46,
                                          header_row = 42,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = None).iloc[1,0]
            return event_pandemic_tpd
        
        def event_pandemic_ip(self):
            event_pandemic_ip = sva.table_import(path = self.path,
                                        sheet_name = self.sheet_name,   
                                          columns = 'FL:FM', 
                                          row_start = 42, row_end = 46,
                                          header_row = 42,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = None).iloc[2,0]
            return event_pandemic_ip

        def prop_disabled_after_wp(self):
            prop_disabled_after_wp = sva.table_import(path = self.path,
                                        sheet_name = self.sheet_name,   
                                          columns = 'FL:FM', 
                                          row_start = 42, row_end = 46,
                                          header_row = 42,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = None).iloc[3,0]
            return prop_disabled_after_wp

        def lapse_stress(self):
            lapse_stress = sva.table_import(path = self.path,
                                        sheet_name = self.sheet_name,   
                                          columns = 'FL:FM', 
                                          row_start = 48, row_end = 50,
                                          header_row = 48,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = None).iloc[0,0]
            return lapse_stress       

        def servicing_expense_stress(self):
            servicing_expense_stress = sva.table_import(path = self.path,
                                        sheet_name = self.sheet_name,   
                                          columns = 'FL:FM', 
                                          row_start = 48, row_end = 50,
                                          header_row = 48,
                                          clear_first_n_rows = None, 
                                          index_col = 0,
                                          trim_column_names = True,
                                          trim_index_name = None).iloc[1,0]
            return servicing_expense_stress       
# =============================================================================
# 11
    def reinsurance(self):
        reinsurance = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'FT:FY', 
                                      row_start = 11, row_end = 14,
                                      header_row = 11,
                                      clear_first_n_rows = None, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = None)
        return reinsurance
    
    def catastrophe_pl(self):
        catastrophe_pl = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'FT:FY', 
                                      row_start = 21, row_end = 23,
                                      header_row = 21,
                                      clear_first_n_rows = None, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = None).iloc[0, 4]
        return catastrophe_pl

    def catastrophe_capital(self):
        catastrophe_capital = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'FT:FY', 
                                      row_start = 21, row_end = 23,
                                      header_row = 21,
                                      clear_first_n_rows = None, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = None).iloc[1, 4]
        return catastrophe_capital
# =============================================================================
# 12

    def par_loadings(self):
        par_loadings = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'GB:GC', 
                                      row_start = 10, row_end = 11,
                                      header_row = 10,
                                      clear_first_n_rows = None, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = None).iloc[0,0]
        return par_loadings

    def stamp_duty(self):
        stamp_duty = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'GB:GC', 
                                      row_start = 13, row_end = 15,
                                      header_row = 13,
                                      clear_first_n_rows = None, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = None)
        return stamp_duty
    
    def investment_earnings_b0(self):
        investment_earnings_b0 = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'GB:GC', 
                                      row_start = 16, row_end = 17,
                                      header_row = 16,
                                      clear_first_n_rows = None, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = None).iloc[0,0]
        return investment_earnings_b0
# =============================================================================
# 13

    def contingency_margin_start(self):
        contingency_margin_start = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'GF:GG', 
                                      row_start = 10, row_end = 11,
                                      header_row = 10,
                                      clear_first_n_rows = None, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = None).iloc[0,0]
        return contingency_margin_start    

    def contingency_margin(self):
        contingency_margin = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'GF:GH', 
                                      row_start = 13, row_end = 14,
                                      header_row = 13,
                                      clear_first_n_rows = None, 
                                      index_col = None,
                                      trim_column_names = True,
                                      trim_index_name = None)
        return contingency_margin            
# =============================================================================
# 14

    def notification_delay(self):
        notification_delay = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'GK:GM', 
                                      row_start = 11, row_end = 12,
                                      header_row = 11,
                                      clear_first_n_rows = None, 
                                      index_col = None,
                                      trim_column_names = True,
                                      trim_index_name = None)
        return notification_delay  
      
# =============================================================================
# 15

    def cmm_impact_termination_rates_start(self):
        cmm_impact_termination_rates = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'GP:GQ',
                                      row_start = 11, row_end = 13,
                                      header_row = 11,
                                      clear_first_n_rows = None, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = None).iloc[0,0]
        return cmm_impact_termination_rates  

    def cmm_impact_termination_rates_perc(self):
        cmm_impact_termination_rates_perc = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'GP:GQ',
                                      row_start = 11, row_end = 13,
                                      header_row = 11,
                                      clear_first_n_rows = None, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = None).iloc[1,0]
        return cmm_impact_termination_rates_perc         
# =============================================================================
# 16
    def covid19_impact_termination_rates(self):
        covid19_impact_termination_rates = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'GS:GT',
                                      row_start = 11, row_end = 16,
                                      header_row = 11,
                                      clear_first_n_rows = None, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = None)   
        return covid19_impact_termination_rates   


# =============================================================================
# 17

    def covid19_adjustment_ip_dlr(self):
        covid19_adjustment_ip_dlr = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'GV:GW',
                                      row_start = 11, row_end = 27,
                                      header_row = 11,
                                      clear_first_n_rows = None, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = None)   
        return covid19_adjustment_ip_dlr   

# =============================================================================
# 18

    def expected_lr_combined_capital(self):
        expected_lr_combined_capital = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'GY:HB',
                                      row_start = 11, row_end = 90,
                                      header_row = 11,
                                      clear_first_n_rows = 1, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = None)   
        return expected_lr_combined_capital


# =============================================================================
# 19

    def gov_tpd_linked_to_ip(self):
        gov_tpd_linked_to_ip = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'HD:HF', 
                                      row_start = 11, row_end = 23,
                                      header_row = 11,
                                      clear_first_n_rows = None, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = None)   
        return gov_tpd_linked_to_ip

    def tpd_linked_reporting_delay(self):
        tpd_linked_reporting_delay = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'HH:HI', 
                                      row_start = 11, row_end = 65,
                                      header_row = 11,
                                      clear_first_n_rows = None, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = None)   
        return tpd_linked_reporting_delay
    
    def conversion_rates(self):
        conversion_rates = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'HK:HM', 
                                      row_start = 11, row_end = 26,
                                      header_row = 11,
                                      clear_first_n_rows = None, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = None)   
        return conversion_rates
    
# =============================================================================
# 20

    def claims_reporting_delay_tpd_ip(self):
        claims_reporting_delay_tpd_ip = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'HO:HQ', 
                                      row_start = 11, row_end = 305,
                                      header_row = 11,
                                      clear_first_n_rows = 1, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = None)   
        return claims_reporting_delay_tpd_ip
    
    def claims_delay_factors_tpd_ip(self):
        claims_delay_factors_tpd_ip = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'HS:HU', 
                                      row_start = 11, row_end = 305,
                                      header_row = 11,
                                      clear_first_n_rows = 1, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = None)   
        return claims_delay_factors_tpd_ip

# =============================================================================
# 21

    def missing_subcase_reserve(self):
        missing_subcase_reserve = self.table_import(path = self.path,
                                    sheet_name = self.sheet_name,   
                                      columns = 'HW:HX', 
                                      row_start = 11, row_end = 15,
                                      header_row = 11,
                                      clear_first_n_rows = 1, 
                                      index_col = 0,
                                      trim_column_names = True,
                                      trim_index_name = None)   
        return missing_subcase_reserve

# =============================================================================