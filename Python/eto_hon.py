# 干支の定義をタプルで定義
eto_tup = ('子','丑','寅','卯','辰','巳','馬','未','申','酉','戌','亥')

year_str = input('Enter your year of birth in AD: ')
# 入力値をint型に変換
year_int = int(year_str)
# 干支の順番を計算
num_eto = ((year_int + 8) % 12)

#print(num_eto)
eto_name = eto_tup[num_eto]
print( 'Your Eto is {}.'.format(eto_name))

