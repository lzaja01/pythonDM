print("Dobrodošli u fizzbuzz igru!")

broj = int(input("Upišite broj od 1 and 100: "))

for br in range(1, 100):
    if br % 3 == 0 and br % 5 == 0:
        print("fizzbuzz")
    elif br % 3 == 0:
        print("fizz")
    elif br % 5 == 0:
        print("buzz")
    else:
        print(br)