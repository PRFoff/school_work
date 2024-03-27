def main():
    '''
        a : list   - database
        shapka : str - first str in db
    '''

    with open('students.csv', 'r', encoding='utf8') as f:
        a = f.readlines()
        shapka = a.pop(0)

    for i in range(len(a)):
        a[i] = a[i].strip().split(',')

    for i in range(len(a)):
        if 'Хадаров Владимир' in a[i][1]:
            print(f'ты получил {int(a[i][-1])}, за проект - {a[i][2]}')

    d = {}
    for x in a:
        class_ = x[3]
        score = x[-1]
        if 'None' not in x:
            if class_ not in d:
                d[class_] = [int(score)]
            else:
                d[class_] += ([int(score)])
    for class_ in d:
        d[class_] = (round(sum(d[class_]) / len(d[class_]), 3))

    for i in range(len(a)):
        if a[i][-1] == 'None':
            a[i][-1] = str(d[a[i][3]])

    with open('students_new.csv', 'w', encoding='utf8') as f:
        f.write(shapka)
        for i in a:
            print(i)
            f.write(','.join(i) + '\n')
