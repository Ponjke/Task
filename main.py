raw_a = input('Please input a: ')
raw_b = input('Please input b: ')
raw_c = input('Please input c: ')

size_a = int(raw_a)
size_b = int(raw_b)
size_c = int(raw_c)

if size_a == 0 or size_b == 0 or size_c == 0:
    print('There isnt triangle')

perimeter = size_a + size_b + size_c

'''
if perimeter > 20 thеn print(...) elif perimeter < 10 thеn print(...)
'''

if perimeter > 20:
    print('The biggest size = ' , max(size_a, size_b, size_c))
elif perimeter < 10:
    print('The smallest size = ' , min(size_a, size_b, size_c))

print('Perimeter = ' , perimeter)


