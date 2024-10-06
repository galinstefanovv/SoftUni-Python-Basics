def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_numbers(start1, start2, diff1, diff2):
    end1 = start1 + diff1
    end2 = start2 + diff2

    for i in range(start1, end1 + 1):
        for j in range(start2, end2 + 1):
            if is_prime(i) and is_prime(j):
                print(f"{i}{j}")


start1 = int(input())
start2 = int(input())
diff1 = int(input())
diff2 = int(input())

generate_numbers(start1, start2, diff1, diff2)