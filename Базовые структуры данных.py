grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
x = sorted(students)
aver0 = sum(grades[0])/len(grades[0])
aver1 = sum(grades[1])/len(grades[1])
aver2 = sum(grades[2])/len(grades[2])
aver3 = sum(grades[3])/len(grades[3])
aver4 = sum(grades[4])/len(grades[4])

dict_ = {x[0]: aver0}
dict_.update({
    x[1]: aver1,
    x[2]: aver2,
    x[3]: aver3,
    x[4]: aver4})
print(dict_)