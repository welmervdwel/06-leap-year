# Write a function `is_leap_year` that takes a year as a parameter
#   -->**RETURNS**<-- True if the year is a leap year, False otherwise.
# The logic-chain is somewhat similar to the Sherlock problem.

# Don't forget to reach out for help after your own due diligence

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
# Start with filtering the largest amount: if divisible by 4 = leap year
# But then it includes start of centuries, so it has to be an AND statement
# Like so: if divisible by 4 AND not divisible by 100 it keeps all results divisible by 4, but not by 100
# Then put any year divisible by 400 back in (can only be start of century divisible by 400)
