# Name:Md Rakib Mia
# id:1935202029

array = [
    [20, 4, 'job1'],
    [10, 1, 'job2'],
    [40, 1, 'job3'],
    [30, 2, 'job4']

]
print("Name:Md Rakib Mia\nId:1935202029")
# array sort Descending order
array.sort(reverse=True)
# highest dead value assign
HdeadValue = 4
print("profit Deadline jobId")
print(" Pro Dl  Job")
for arr in range(HdeadValue):
    print(array[arr])
# deadArray value init all value is zero
deadArray = [0] * HdeadValue
# array lengh
lenth = len(array)
# for total profit count
Total_profit = 0

print("Maximum profit sequence of jobs")
for i in range(lenth):
    # tempvalue store deadline value
    tempValue = array[i][1]
    while tempValue > 0:
        if deadArray[tempValue - 1] == 0:
            deadArray[tempValue - 1] = 1
            print(array[i ][2], end=" ->")
            Total_profit = Total_profit + array[i][0]
            break
        else:
            tempValue = tempValue - 1

print()

print("Total Profit=", Total_profit)
