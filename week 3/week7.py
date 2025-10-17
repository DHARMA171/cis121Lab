
# total = 0
# user_number = input("enter a number or type q to end: ")
# while  user_number != 'q':
#     total += int(user_number)
#     user_number = input("enter a number or type q to end: ")
# print(f"total = {total}")    



# def string_to_list_with_vowels(word):
#     words = []
#     built_word = ''
#     vowel_count = 0
#     for letter in word:
#         if letter == ' ':
#             words.append(built_word)
#         else:
#             #built_word = ''
#             built_word += letter
#     return words
# my_word = 'peter piper pickked a peck of pickled peppers'
# print(string_to_list_with_vowels(my_word))            


# def is_isogram(word):
#     visit = []
#     for letter in word:
#         if letter in visit:
#             return False
#         else:
#             visit.append(letter)
#     return True
# print(is_isogram('car'))  
# print('calculater is ',is_isogram("calculater"))      



def find_unique(number):
    for num in number:
        if number.count(num)==1:
            return num 
print(find_unique([1,2,2,3,3,4]))      



def return_unique(number):
    unique = [num for num in number if number.count(num)==1]
    return unique
print(return_unique([1,2,2,3,3,4]))


def get_name(names):
    return list(names.values())
print(get_name({'1234':'harime','2468':'sushil'}))



def min_grade(marks):
    grade = min(marks, key=marks.get)
    return grade
print(min_grade({'var':90,'phy':80,'soc':79}))


# def majority_elements(nums):
#     counts={}
#     for num in nums:
#         counts[num]=counts.get(num,0)+1
#         for num, count in counts.item():
#             if count> len (nums)//2:


# def calc_toll(hour, morning = True, weekend= False):   (not completed)
    
#     if weekend:
#         if morning:
#             if hour < 7:
#                 return 1.05     
#             else:
#                 return 2.15     
#         else:
#             if hour < 8:
#                 return 2.15     
#             else:
#                 return 1.10
        


#     else:
#        if morning == True: 



def ascending_order(num1, num2=5, num3=25):
    nums = [num1, num2, num3]
    if nums[0] > nums[1]:
        nums[0], nums[1] = nums[1], nums[0]
    if nums[1] > nums[2]:
        nums[1], nums[2] = nums[2], nums[1]
    if nums[0] > nums[1]:
        nums[0], nums[1] = nums[1], nums[0]

    return nums
print(ascending_order(2,4,3))
print(ascending_order(10,1))
print(ascending_order(60))
           



