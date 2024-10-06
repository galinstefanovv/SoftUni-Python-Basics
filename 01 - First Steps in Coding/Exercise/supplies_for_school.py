pencils = int(input()) * 5.80
marker = int(input()) * 7.20
liquid = int(input()) * 1.20
discount = int(input()) / 100
total_sum = pencils + marker + liquid
total_sum -= total_sum * discount
print(total_sum)