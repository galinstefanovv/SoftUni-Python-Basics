deposit_sum = float(input())
term_of_deposit = int(input())
rate = float(input()) / 100

total = deposit_sum + term_of_deposit * ((deposit_sum * rate) / 12)

print(total)