# -*- coding: utf-8 -*-

input_txt = '''2018/12/16,02,1
2018/12/16,03,3
2018/12/16,04,2
2018/12/16,05,4
2018/12/16,06,2
2018/12/18,01,3
2018/12/18,02,5
2018/12/18,03,3'''

def group_by(dates):
    def group_by_impl(aa):
        if len(dates) == 0:
            dates.append(aa)
            return
        found = False
        for i, item in enumerate(dates):
            #print('comparing %s - %s' % (item, aa))
            if item[0:10] == aa[0:10]:
                found = True
                #print('found matching')
                #print('comparing %s %s' % (item[14:], aa[14:]))
                if item[14:] < aa[14:]:
                    #item = aa
                    dates[i] = aa
                    break

        if not found:
            dates.append(aa)

    return group_by_impl

input_data = input_txt.split('\n')

dates = []

output = map(group_by(dates), input_data)

print('-' * 80)

print(dates)
