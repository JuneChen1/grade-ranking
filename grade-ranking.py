gradeList = []
i = 1

print("--請至少輸入6個成績，輸入任意字母可進行結算--")

while True:
  grade = input("請輸入第"+str(i)+"個成績：")
  if grade.encode().isalpha() == True:
    if len(gradeList) < 6:
      print("------請至少輸入6個成績------")
      continue
    else:
      break
  elif grade.isdigit() == False:
    print("----請輸入正整數，或輸入任意字母進行結算----")
    continue
  i += 1
  gradeList.append(int(grade))

gradeList.sort()
length = len(gradeList)
average = round(sum(gradeList)/length, 1)

print("----------------------")
print("平均成績：", average)
print("最大的三個成績：{}、{}、{}".format(gradeList[-1], gradeList[-2], gradeList[-3]))
print("最小的三個成績：{}、{}、{}".format(gradeList[0], gradeList[1], gradeList[2]))