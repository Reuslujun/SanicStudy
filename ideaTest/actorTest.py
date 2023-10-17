

def getName(name,age,school):
    print("name: ",name," age: ",age," school:",school)


if __name__ == '__main__':
    temp = []
    temp1 = ('lujun',25,'西南大学')
    temp2 = ('Reus',26,'重庆大学')
    temp.append(temp1)
    temp.append(temp2)
    for i in temp:
        getName(*i)