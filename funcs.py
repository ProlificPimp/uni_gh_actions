from decimal import Decimal

def find_min(nums):
    min = nums[0]
    try:
        for n in nums:
            if n < min: min = n
        return min
    except:
        return 'Error Overload'

def find_max(nums):
    max = nums[0]
    try:
        for n in nums:
            if n > max: max = n
        return max
    except:
        return 'Error Overload'

def find_sum(nums):
    sum = Decimal('0')
    try:
        for n in nums:
            sum += n
        return sum
    except:
        return 'Error Overload'

def find_prod(nums):
    prod = Decimal('1')
    try:
        for n in nums:
            prod *= n
        return prod
    except:
        return 'Error Overload'

def read_file(file_name):
    try:
        f = open(file_name, "r")
    except:
        print('Введите корректное название файла и убедитесь, что он находится в одной директроии со скриптом')
        return 'Error'
    nums = f.read().split()
    for i in range(len(nums)):
        try:
            nums[i] = Decimal(str(nums[i]))
        except:
            print(f'Не правильный формат данных в файле {file_name}')
            return 'Error'
    return nums


nums = read_file('nums.txt')
if nums != 'Error':
    minn = find_min(nums)
    maxx = find_max(nums)
    summ = find_sum(nums)
    prod = find_prod(nums)
    print(f'min = {minn}\nmax = {maxx}\nsum = {summ}\nprod = {prod} ')
else:
    print('Возникла ошибка!')


