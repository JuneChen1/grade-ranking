gradeList = []

for i in range(1, 11):
  grade = int(input("請輸入第"+str(i)+"個成績："))
  gradeList.append(grade)

gradeList.sort()

print("最大的三個成績：{}、{}、{}".format(gradeList[9], gradeList[8], gradeList[7]))
print("最小的三個成績：{}、{}、{}".format(gradeList[0], gradeList[1], gradeList[2]))