import datetime

my_name = input()
today = datetime.datetime.now().date()

t = today.strftime("%y년%m월%d일")

print(f"{my_name}님 안녕하세요 오늘은 {t} 입니다.")

now = datetime.now()


# print(f"{my_name}님 안녕하세요 오늘은 {now.year}년 {now.month}월 {now.day}일 입니다.")
