

with open('students.csv', 'r', encoding='utf8') as f:
    a: list = f.readlines()
    shapka: str = a.pop(0)
    for i in range(len(a)):
        a[i] = a[i].strip().split(',')

    '''
    id, Name, titleProject_id, class, score
    '''
    while True:
        s: str = str(input())
        if s == 'СТОП' or s == '': quit()
        check : bool = False
        for i in a:
            if int(i[2]) == int(s):
                check : bool = True
                score = i[4]
                f, i, o = i[1].split()
                print(f'Проект № {s} делал: {i[0]}. {o} он(а) получил(а) оценку - {score}')

        if check == 0:
            print("Ничего не найдено")
