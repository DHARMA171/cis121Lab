# # # number = 2
# # # while number <= 10:
# # #     print(number)
# # #     number += 2


# # # number = 1
# # # while number <= 10:
# # #     if number % 2 == 0:
# # #         print(number)
# # #     number += 1
      
# # #print all of the odd number between 5 and some 
# # #user gives value (inclusively).
# # '''
# # start = 5
# # user = int(input("enter your number: "))
# # while start <= user:
# #     if start % 2 == 1:
# #         print(start)
# #     start += 1    
# # ''' 

# # #find the sum of user entered value until the 
# # #user type q (for done)

# # # total = 0
# # # user_input = input("enter a number or type q to exit: ")
# # # while user_input  != 'q':
# # #     total += int(user_input)
# # #     user_input = input("enter a number or type q to exit: ")
# # # print(f"total = {total}")    

# # '''
# # total = 0
# # user_input =" "
# # done = False
# # while not done:
# #     user_input = input("enter a number or type q to exit: ")
# #     if user_input == 'q':
# #        done  = True
# #     else:
# #     total += int(user_input)
# # print(f"total = {total}")       
     
# # '''


# # #print all of the number between 1 ... .. ..50 that are even but not divisible by 3

# # '''number = 1
# # while number <= 50:
# #      number += 1  
# #      if number % 2 == 0:
# #          if number % 3 == 0:
# #              continue
# #          print(number)''' 

# # '''number = 37
# # while number <= 1050:
# #     number +=1
# #     if number % 2 ==0:
# #       print(number)'''

# # '''larger = int(input("enter larger no.: "))
# # smaller = int(input("enter smaller no.: "))
# # count = 0
# # while larger/2 > smaller:
# #     larger/=2
# #     count += 1
# # print(count)'''





# # # for number in range (2, 10+1, 2):
# # #        print(number)
       
# # '''
# # #print all of the odd number between 5 and some user given value   
# # user_number = int(input("enter the number: "))
# # for number in range(5, user_number+1):
# #     if number % 2 == 1:
# #         print(number)
# # '''



# larger = int(input("enter larger num:"))
# smaller = int(input("enter smaller number: "))
# count = 0
# while larger/2 > smaller:
#     larger = larger/2 or larger > smaller
#     count += 1
#     print(count)   




# # '''words = 'Dharmagat'
# # print(words[2:7])'''

# # # age = int(input("inter age"))
# # # if age >=20 or age <= 39:
# # #     value = input("above ave or below ave: ")
# # #     if value == "above ave":
# # #         print("your heart rate is 47-72")
# # #     else:
# # #         print("73-93")
# # # else:
# # #     print("error")            

# # '''
# # knuts = int(input("enter knuts: "))
# # knuts_sickle = 29
# # sickle_galleon = 17
# # knuts_gallon = knuts_sickle*sickle_galleon

# # galleon = knuts//knuts_gallon
# # knuts = knuts % knuts_gallon
# # sickle = knuts// knuts_sickle
# # knuts = knuts % knuts_sickle
# # if galleon>0:
# #     print(galleon, "galleon")
# # if sickle>0:
# #     print(sickle, "sickle")
# # if knuts > 0:
# #     print(knuts, "knut")
# # '''
# # '''
# # proper = {}
# # num = int(input("enter the number: "))
# # for i in range (1, num):
# #     if num//i==0:
# #         proper.append(i)
# #     print(proper)    
# # '''

# # # proper = {}
# # # num = 37
# # # for i in range ()

# # #write code to determine how many letter are in a word.
 
# # '''word = 'hello world'
# # count = 0
# # for letter in word:
# #     count += 1
# # print(count)

# # for letter in word:
# #     print(letter)
# # print('\n---------------\n')

# # for index in range (0, len(word)+1):
# #     print(index, word[index])'''


# # '''word = input("write a word: ")
# # word1 = input('write a word: ')
# # word2 = input("write a word: ")
# # vowels = 'aeiou'
# # count = 0
# # for letter in word:
# #     if letter in vowels:
# #         count += 1
# # print(count)        
# # count = 0
# # for letter in word1:
# #     if letter in vowels:
# #         count += 1
# # print(count) 
# # count = 0
# # for letter in word2:
# #     if letter in vowels:
# #         count += 1
# # print(count) '''


# # '''def vowel_counter(word):
# #     count = 0
# #     for letter in word:
# #         if letter == 'a':
# #             count += 1
# #         elif letter == 'e':
# #             count += 1  
# #         elif letter == 'i':
# #             count += 1
# #         elif letter == 'u':
# #             count += 1
# #         elif letter == 'o': 
# #             count += 1
# #     return count                     
       
# #     print(f"the vowel count in {word} is {count} ")
                
# # word1 = ("hello world")  
# # word2 = ("banana")   
# # vowel_count1 = vowel_counter(word1)
# # vowel_count2 = vowel_counter(word2)

# # total_vowel_count = vowel_count1 + vowel_count2
# # print(f"the total vowels seen so far is {total_vowel_count}")'''


# # #write a function that takes an int add two, multiples by 4, print the result.

# # '''def my_fctn (number):
# #     number += 2
# #     number *= 4
# #     return number

# # result1=my_fctn (10)
# # result2 = my_fctn (result1)
# # print(result2) ''' 

# # '''def add_5(number):

# #     number += 5
# #     return number
# # def times_5(number):
# #     number *= 2
# #     return number
# # x = times_5(add_5(10))
# # print(x)'''

# # #write a power of 2 function to calculate (3^2)^2
# # '''def power_2(number):
# #     number **= 2
# #     return number
# # def powers_2(number):
# #     number **= 2
# #     return number
# # x = power_2(power_2(power_2(3)))
# # print(x)'''

# # #using the times_2 function, multiple 5 by 2 a total of 10 times.

# # '''result = 5
# # for value in range(0,10):
# #     result = times_2(result)
# # print(result)'''   
# # ######################

# # '''def product (num1, num2):
# #     result = num1 * num2
# #     return result
# # x = product(3)
# # print(x)'''


# # '''lyst = ['apple', 'banana', 3, False, 4.5, 'grapes']
# # print(lyst[1])
# # print(lyst[0:6])
# # print(lyst[5][3])
# # for element in lyst:
# #     print(element)'''


# # '''x = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
# # y=x
# # print(x)
# # print(y)

# # x[4] = 'funnnnnnnnnnnnnnnnn'
# # print(x)
# # print(y)'''


# # # my_word = 'peter piper picked a peck of pickled peppers'
# # #result = ['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers']


# # # def string_to_list(word):
# # #     words = []
# # #     found_word = ""
# # #     for letter in word:
# # #         if letter == " ":
# # #             words.append(found_word)
# # #             found_word = ""
# # #         else:
# # #             found_word += letter 
# # #     words.append(found_word)        
# # #     return words 

# # '''def string_to_list_alt(word):
# #     words = []
# #     found_word = ""
# #     for index in range(len(word)):
# #         if word[index] == " " or index == len(word)-1:
# #             words.append(found_word)
# #             found_word = ""
# #         elif index == len(word)-1:
# #             found_word += word[index] 
# #             words.append''' 
# # # print(string_to_list(my_word))  


# # # WAF that takes a string as an arguments and returns a list containing all of the words that have at least two vowels.


# # def strring_to_list_with_vowels(word):
# #     words = []
# #     built_word = ''
# #     vowel_count = 0
# #     for letter in word:
# #         #print(letter, vowel_count, built_word)
# #         if letter == ' ':
# #             if vowel_count >= 2:
# #                 words.append(built_word)
# #             built_word = ''
# #             vowel_count = 0
# #         else:
# #             built_word += letter
# #             if letter in 'aeiou':
# #                 vowel_count += 1
# #     if vowel_count >= 2:            
# #        words.append(built_word)
# #     return words

# my_word = 'peter piper picked a peck of pickled pepprs'
# # print(strring_to_list_with_vowels(my_word))

# phonebook = {'sushil': 25879, 'prakash': 2546894}
# #print(phonebook)
# # to add a key-value pair in a dictionary, we use dicy_name[key]= value
# phonebook['waters'] = 6789
# #print(phonebook)
# # to add a key-value pair in a dictionary, we use dicy_name[key]. This will print the value.
# # print(phonebook['sushil'])
# for name in phonebook:
#     print(f'{ name }',  phonebook [ name])

'''def letter_counter(word):
    #idea: make a dictionary where the letter are keys and the number of occurancies of the lette is the value.
    letter_dictionary = {}
    for letter in word:
        if letter in letter_dictionary:
            letter_dictionary[letter] = letter_dictionary[letter] + 1
        else:
            letter_dictionary[letter] = 1
    return letter_dictionary   
print(my_word)
x = letter_counter(my_word)
for key in x:
    print(f'{key} -> {x[key]}')'''     

'''def count (cards):
    points = 0
    for card in cards:
        if str(card) in ["2","3","4","5","6"]:
           points += 1
        elif card in [7,8,9]:
            points += 0
        elif str(card) in [10,"j","q","k","a"]:
            points -= 1  
    return points
deck = [2,3,4,5,6,7,8,9,10,'a','j','q','k']
deck1 = [2,4,3,5,'a,','j','q']
print(f'total dect : {count(deck)}')
print(f'total dect : {count(deck1)}')'''


# def is_acronym(s, words):
#     combined_letter = ''
#     if len(s) != len(words):
#         return False
#     for word in words:
#         if word =='':
#             return False
#         combined_letter +=words[0]
#     if s != combined_letter:
#         return False
#     return True
# words =['alice', 'bob', 'charlie']
# s = 'abc'
# print(is_acronym(s, words))


# width = int(input("Enter rug width: "))
# length = int(input("Enter rug length: "))
# patten = input("Enter a single character pattern: ")

# for i in range(width):
#     print(patten * length)



# A function is another data type operators.
# 1 -Assighment=
# 2 -Invoking ()
# the parentheses are the operater that tells python to apply the function to the supplied paremeters.
# In python all names defined in a program are organized into namespaces.
# These are the names available when the program 


# def add_three(x):
#     y = x+3
#     return y
# var0 = 7
# var1 = add_three(var0)
# print(var1)

# def skip_letter_first(word):
#     result = []
#     for i in range(1, len(word), 2):
#         result.append(word[i])
#     return result
# print(skip_letter_first("counterattack"))


# def output_even(smaller_num, larger_num):
#     evens = []
#     for i in range(smaller_num, larger_num + 1):
#         if i % 2 == 0:
#             evens.append(i)
#     return evens
# print(output_even(37, 1050))

# def output_odd(smaller, larger):
#     odd = []
#     for i in range(smaller, larger +1):

#         if i % 2 != 0:
#             odd.append(i)
#     return odd
# print(output_odd(31, 1050))    


# def hailstone_seq(n):
#     seq = [n]
#     while n != 1:
#         if n % 2 ==0:
#             n = n // 2
#         else:
#             n = n*3+1
#         seq.append(n)
#     return seq
# print(hailstone_seq(40))    


# def find_factor(num):
#     factor = []
#     for i in range(1, num+1):
#         if num % i ==0:
#             factor.append(i)
#     return factor
# print(find_factor(12))        



# def ascending_order(a,b,c):
#     if a<b:
#         a,b=b,a
#     if b<c:
#         b,c=c,b
#     if a<b:
#         a,b=b,a
#     return [a,b,c]
# print(ascending_order(8,5,6))     

# def count(cards):
#     total = 0
#     for card in (cards):
#         if card in [2,3,4,5,6]:
#             total += 1
#         elif card in [7,8,9,10]:
#             total += 0
#         elif card in ["j","k","q","a"]:
#             total -= 1
#     return total
# print(count([2,4,6,8,10,"a","k","q"]))       


# def war_of_numbers(numbers):
#     even_sum = 0
#     odd_sum = 0
#     for n in numbers:
#         if n%2==0:
#             even_sum += n
#         else:
#             odd_sum += n
#     return "even" if even_sum>odd_sum else "odd"   
# print(war_of_numbers([2,4,7,8,9,3]))         


# def is_isogram(word):
#     word = word.lower()  # make it case-insensitive
#     for letter in word:
#         if word.count(letter) > 1:
#             return False
#     return True
# print(is_isogram("aple"))


# def is_isogram(word):
#     visited = []
#     for letter in word:
#         if letter in visited:
#             return False
#         else:
#             visited.append(letter)
#     return True
# print(is_isogram("apple"))        


# def find_unique(numbers):
#     for num in numbers:
#         if numbers.count(num) == 1:
#             return num
# print(find_unique([1,2,3,4,5]))        

# def count_repetitions(lst)