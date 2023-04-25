# answer = 48
    
# while True:
#     user_input = int(input())
#     if user_input == answer:  
#         print("정답")
#         break
#     else:
#         print("no")

# print("게임 끗")   
    
        
        
        
import random

answer = random.randint(10, 100)
while True:
    user_input = int(input())
    if user_input == answer:
        print("정답입니다")
        break
    elif user_input < answer:
        print("up")
    else:
        print("down")
print("게임이 끝났습니다.")