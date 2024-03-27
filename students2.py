def sorting(a : list):

    for i in range(1, len(a)):
        value = a[i][-1]
        info = a[i]
        j = i - 1
        while a[j][-1] < value and j >= 0:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = info

    return a


def main():


    with open('students.csv', 'r', encoding='utf8') as f:
        a = f.readlines()
        shapka = a.pop(0)

    for i in range(len(a)):
        a[i] = a[i].strip().split(',')
        if a[i][-1] == 'None':
            a[i][-1] = 0
        else:
            a[i][-1] = int(a[i][-1])

    a = sorting(a)
    k = 0
    print('10 класс:')
    for x in a:
        clas = x[3]
        if '10' in clas:
            k += 1
            f, i, o = x[1].split()
            print(f'{k} место: {i[0]}. {f}')
            if k == 3:
                break


if __name__ == "__main__":
    main()