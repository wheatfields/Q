# sva.

#### _Table 1_
* [claim_reporting_delay](#claim_reporting_delay)
* [claim__delay_factors](#claim__delay_factors)

#### _Table 2_
* [claims_expense_reserve](#claims_expense_reserve)
* [operating_expense_perc_premium](#operating_expense_perc_premium)
* [budgeted_trustee_expense](#budgeted_trustee_expense)
* [projected_trustee_expense](#projected_trustee_expense)

#### Table 3
* [ip_continuance_rates](#ip_continuance_rates)
* [dlr_parameters](#dlr_parameters)
    * [salary_replacement_ratio](#salary_replacement_ratio)
    * [continuing_retirement_benefit](#continuing_retirement_benefit)
    * [assumed_avg_age_at_disability](#assumed_avg_age_at_disability)
    * [payment_ratio](#payment_ratio)
    * [reopened_claims_reserves_loading](#reopened_claims_reserves_loading)
    * [benefit_indexation_month](#benefit_indexation_month)
    * [ip_ibnr_adjustment](#ip_ibnr_adjustment)


#### _Table 4_
* [appeals_reserve_assumptions](#appeals_reserve_assumptions)
* [perc_of_appealed_claims_accepted](#perc_of_appealed_claims_accepted)


#### _Table 5_
* [decline_rate](#decline_rate)
* [decline_rate_delay](#decline_rate_delay)
* [simultaneous_ip_tpd_decline](#simultaneous_ip_tpd_decline)


#### _Table 6_
* [expected_loss_ratio_gov](#expected_loss_ratio_gov)
* [expected_loss_ratio_nongov](#expected_loss_ratio_nongov)


#### _Table 7_
* [payment_delay_factors](#payment_delay_factors)
* [payment_delay_factors_discrete](#payment_delay_factors_discrete)



#### _Table 8_
* [average_claim_size](#average_claim_size)
* [acs_ip_linked_tpd](#acs_ip_linked_tpd)
* [acs_by_notification_delay_q](#acs_by_notification_delay_q)
* [perc_si_at_ip_doe](#perc_si_at_ip_doe)
* [tpd_si_scales_by_age](#tpd_si_scales_by_age)



#### _Table 9_
* [termination_rates](#termination_rates)
* [age_rates](#age_rates)
* [duration_of_claim_g_wp_oc](#duration_of_claim_g_wp_oc)
* [smoker_status](#smoker_status)
* [benefit_type](#benefit_type)
* [policy_duration_factor](#policy_duration_factor)


#### _Table 10_
* [stress_margins](#stress_margins)
    * [random](#random)
        * [random_all](#random_all)
        * [death](#r_death)
        * [death_ibnr](#r_death_ibnr)
        * [death_rbna](#r_death_rbna)
        * [tpd](#r_tpd)
        * [tpd_ibnr](#r_tpd_ibnr)
        * [tpd_rbna](#r_tpd_rbna)
        * [ip](#r_ip)
        * [ip_dlr](#r_ip_dlr)
        * [ip_ibnr](#r_ip_ibnr)
        * [ip_rbna](#r_ip_rbna)
    * [future](#future)
        * [future_all](#future_all)
        * [death](#f_death)
        * [death_ibnr](#f_death_ibnr)
        * [death_rbna](#f_death_rbna)
        * [tpd](#f_tpd)
        * [tpd_ibnr](#f_tpd_ibnr)
        * [tpd_rbna](#f_tpd_rbna)
        * [ip](#f_ip)
        * [ip_dlr](#f_ip_dlr)
        * [ip_ibnr](#f_ip_ibnr)
        * [ip_rbna](#f_ip_rbna)








```python
import os
os.chdir(r"C:\Users\adamw\Documents\GitHub\Q")
path = r"C:\Users\adamw\Documents\SVA replica.xlsx"
from sva import sva
# # Initialise with path and sheetname
sva = sva(path=path, sheet_name='NewProduct')
a = dir(sva.termination_rates)
dir_sva = dir(sva.stress_margins)
[dir_sva for dir_sva in dir_sva if '__' not in dir_sva]
```




    ['future', 'path', 'random', 'sheet_name']



# random


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
