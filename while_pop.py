my_list = [ {"이름":"권기현", "나이":32}, 
     {"이름":"홍서연", "나이":20}, 
     {"이름":"박소진", "나이":20}, 
     {"이름":"이미진", "나이":19}, 
     {"이름":"이정현", "나이":18},
      {"이름":"연제건", "나이":17}, 
 {"이름":"강유지", "나이":16}, 
 {"이름":"김태연", "나이":15}, 
 {"이름":"김주영", "나이":14}]

while len(my_list) > 5:
    my_list.pop()
print(my_list[-1:])
print(len(my_list))


# my_list.pop(-2)
# print(my_list)


while my_list:
    person = my_list.pop()
    print(person['이름'])
    if person['이름'] == '이정현':
        print(person['이름'])
        break
print(len(my_list))
print('끗')