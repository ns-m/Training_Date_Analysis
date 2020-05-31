def str_inp():
    with open('dataset_3363_2.txt') as inf:
        s1 = inf.readline().strip()
        num, chrt, res, n = '', '', '', 0
        for i in s1:
            if 48 <= ord(i) <= 57:
                num += i
            else:
                chrt += i
                if len(num) != 0:
                    num = num + ' '
        num = num.split(' ')
        while n < len(chrt):
            res += (chrt[n]*int(num[n]))
            n += 1
        print(res)
        with open('dataset_3363_2out.txt', 'w') as ouf:
            ouf.write(res)

str_inp()
