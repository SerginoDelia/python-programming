# principal = 1000 rate = 0.05 numyears = 5 # Initial amount
# Interest rate
# Number of years
# principal = 1000
# rate = 0.05
# numyears = 5

principal, rate, numyears = [1000, 0.05, 5]

year = 1
while year <= numyears:
    principal = principal * (1 + rate)
    print(year, principal)
    year += 1
