def fizz_buzz():
    n = int(input("Enter your range(n):"))
    div1 = int(input("Enter Your first divisor"))
    div2 = int(input("Enter Your second divisor"))
    for i in range(1, n+1):
        if i % div1 == 0 and i % div2 == 0:
            print("FizzBuzz")
        elif i % div1 == 0:
            print("FIzz")
        elif i % div2 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz()
    