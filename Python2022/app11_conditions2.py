# if applicant has high income AND good credit
#     Eligible for loan
# AND - all conditions ara accepted
# OR - one of condition is accepted
# NOT - negative of condition

has_high_income = False
has_good_credit = True

if has_high_income or not has_good_credit:
    print("Eligible for loan!")
else:
    print("Not eligible for loan!")