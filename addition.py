x = input('共有幾筆資料')
numbers = []
x = int(x)

while x > 0:
	if x == 0:
		break
	number = input('請輸入數字')
	number = int(number)
	numbers.append(number)
	x = x - 1

print(sum(numbers))