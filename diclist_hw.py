my_list = [ {"이름":"권기현", "나이":32},  {"이름":"홍서연", "나이":20},  {"이름":"박소진", "나이":20}, {"이름":"이미진", "나이":19},  {"이름":"이정현", "나이":18}, {"이름":"연제건", "나이":17}, {"이름":"강유지", "나이":16}, {"이름":"김태연", "나이":15}, {"이름":"김주영", "나이":14}]

for a in my_list:
    # print(a["나이"])
    if 20 <=a["나이"] :
        print(f"{a['이름']}님 안녕하세요~")
    # if a["이름"] != "권기현" and a["이름"] != "강유지":
    #     a["나이"] += 1
    #     print(a["나이"])