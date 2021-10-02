#exceptions

for i in range(0,10):
    try:
        print(5/i)
    except:
        print("5/0 not possible")
    finally:
        print(" ")

else:
    print("out of range")
