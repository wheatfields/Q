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
# # Initialise with path and sheetname
# cp = sva.sva(path = path, sheet_name = current_product)
# np = sva.sva(path = path, sheet_name = new_product)
# cp_claims_reporting_delay = cp.claims_reporting_delay()[1]
# np_claims_reporting_delay = np.claims_reporting_delay()[0]
# help(np)
# help(np.claims_reporting_delay)


sva = sva.sva(path=path, sheet_name=new_product)

sva.operating_expense_perc_premium()

sva.catastrophe_capital()

help(sva.dlr_parameters)



a = dir(sva.termination_rates)
dir_sva = dir(sva.stress_margins)
[dir_sva for dir_sva in dir_sva if '__' not in dir_sva]



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
