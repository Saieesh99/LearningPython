mylist = ['a','b','c','d']
print("mylist 0",mylist[0])
print("mylist 1",mylist[1])
print("mylist ",mylist[1:3])
print("mylist ",mylist[:2])
print("mylist ",mylist[2:])
sentence = "The quick brown fox jumps over the lazy dog"
first_word = sentence[:3]
print(first_word) # output: "The"
second_word = sentence[4:9]
third_word = sentence[10:15]
print(second_word) # output: "quick"
print(third_word) # output: "brown"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
odd_numbers = numbers[::2]
print(odd_numbers) # output: [1, 3, 5, 7, 9]
odd_numbers = numbers[3::2]
print(odd_numbers) # output: [1, 3, 5, 7, 9]