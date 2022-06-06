ss = input()
print(ss[::-1])

ss = input()
print(ss[ss.find("\"")+1:ss.rfind("\"")])

ss = int(input())
print(ss*2)

ss = input().split()
ss = ss[1] + ' ' + ss[0]
print(ss)

ss = input()
print(ss[:ss.find('@')])

ss = input()
print(ss.replace(' ', '').replace('-', '').replace('(', '').replace(')', ''))

ss = input().strip().replace(' ', '').lower()
print('It is a palindrome' if ss == ss[::-1] else 'It is not a palindrome')

spl = ''
ss = spl.join([str(i) for i in range(1, 124)]).replace('9', spl)
print(ss)

for i in range(100, 1000):
    summ = (i % 10) ** 3 + (i // 100) ** 3 + (i % 100 // 10) ** 3
    if summ == i:
        print(i)


n = int(input())
for i in range(1, n+1):
    sq = str(i * i)
    if sq.endswith(str(i)):
        print(i)


for i in range(15):
    for j in range(15):
        for k in range (15):
            if 15 * i + 17 * j + 21 * k == 185:
                print(i, j, k)
