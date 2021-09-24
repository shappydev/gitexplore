#x = int(input('Enter an integer: '))
#ans = 0
# while ans**3 < x:
#ans = ans + 1
# if ans**3 != x:
#print(str(x) + ' is not a perfect cube')
# else:
#print('Cube root of ' + str(x) + ' is ' + str(ans))


cube = 8
for guess in range(cube + 1):
    if guess**3 == cube:
        print("Cube root of ", cube, " is ", guess)
