def cmToMm(centi):
    milli = centi * 10
    return milli

centi = int(input("길이를 입력하시오(cm)"))
print('{}mm'.format(cmToMm(centi)))