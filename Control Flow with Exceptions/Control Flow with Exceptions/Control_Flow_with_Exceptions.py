def get_ratios(L1, L2):
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
   try:
       return item / denom
   except ZeroDivisionError:
       return 0
