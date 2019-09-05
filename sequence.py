n = int(input("Enter the length of the sequence: "))

sum = 0
first_int = 1
second_int = 2
third_int = 3

for all in range(0, n):
    while sum <= n:
        if sum == n:
            break
        print(first_int)
        sum += 1
        if sum == n:
            break
        first_int = first_int + second_int + third_int
        print(second_int)
        sum += 1
        if sum == n:
            break
        second_int = first_int + second_int + third_int
        print(third_int)
        sum += 1
        if sum == n:
            break
            
        third_int = first_int + second_int + third_int