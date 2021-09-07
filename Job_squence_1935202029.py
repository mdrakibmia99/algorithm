# Name:Md Rakib Mia
# id:1935202029

array = [
    [100, 2, 'job1'],
    [19, 1, 'job2'],
    [27, 2, 'job3'],
    [25, 1, 'job4'],
    [15, 3, 'job5']

]
# sequence init
sequence = [0] * 100
sequenceCount = 0
print("Name:Md Rakib Mia\nId:1935202029")
# array sort Descending order
array.sort(reverse=True)
# highest dead value assign
# array lengh
lenth = len(array)
HdeadValue = 3
print("profit Deadline jobId")
print(" Pro Dl  Job")
for arr in range(lenth):
    print(array[arr])
# deadArray value init all value is zero
deadArray = [0] * HdeadValue

# for total profit count
Total_profit = 0

print("Maximum profit sequence of jobs")
for i in range(lenth):
    # tempvalue store deadline value
    tempValue = array[i][1]
    while tempValue > 0:
        if deadArray[tempValue - 1] == 0:

            deadArray[tempValue - 1] = 1
            sequence[tempValue - 1] = array[i][2]
            Total_profit = Total_profit + array[i][0]
            sequenceCount += 1
            break
        else:
            tempValue = tempValue - 1

for L in range(sequenceCount):
    print(sequence[L], end=" =>")
print()
print("Total Profit=", Total_profit)
