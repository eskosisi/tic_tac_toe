new_table = work_table.copy()
counter = 0
while counter != 9:
    if hello == 'X' or hello == '0' or hello == 'x':
        if hello == 'X' or hello == 'x':
            a = int(input('Where would you like to put your first cross?  '))

            for elems in work_table:
                if a == elems:
                    new_table.remove(a)
                    new_table.insert(a - 1, 'X')
        print('', new_table[0], new_table[1], new_table[2], '\n-------\n', new_table[3], new_table[4], new_table[5],'\n-------\n', new_table[6], new_table[7], new_table[8])
        print('Now my turn! ')
        while True:
            number = random.randrange(0, 10)
            if number != a:
                break
        for elems in work_table:
            if a == elems:
                new_table.remove(number)
                new_table.insert(number - 1, '0')
        print('', new_table[0], new_table[1], new_table[2], '\n-------\n', new_table[3], new_table[4], new_table[5],'\n-------\n', new_table[6], new_table[7], new_table[8])
        b = input('Now your turn! ')
        counter += 2
                if (new_table[0] == new_table[1] == new_table[2]) or (new_table[0] == new_table[4] == new_table[8]) or (new_table[0] == new_table[3] == new_table[6]) .......!!!!!!!!!

        if hello == '0':
            a = int(input('Where would you like to put your first zero?  '))
            for elems in work_table:
                if a == elems:
                    new_table.remove(a)
                    new_table.insert(a - 1, '0')
        print('', new_table[0], new_table[1], new_table[2], '\n-------\n', new_table[3], new_table[4], new_table[5],'\n-------\n', new_table[6], new_table[7], new_table[8])
    else:
        input('Please try again! ')