print ("Before")
largest = None
sum = 0
count = 0
smallest = None

for num in [9, 41, 12, 3, 74, 15]:
    print('num:', num)

    if largest is None:
        largest = num
    elif num > largest:
        largest = num
    print('largets:', largest)

    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    print('smallest:', smallest)

    sum = sum + num
    print('sum so far:', sum)

    count = count + 1
    print('count so far:', count)

print ('Largest:', largest)
print ('Smallest:', smallest)
print ('Sum', sum)
print ('Count', count)
print ('Average', sum/count)