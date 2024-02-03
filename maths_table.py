num=int(input('please type the \'number\' for which you want to determine the table: '))
table_range=int(input('Please enter the \'range\' for table: '))

for i in range(1,table_range+1):
    
    print(num, '*', i, '=', i*num)