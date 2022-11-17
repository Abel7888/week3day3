# Week 3: Day 3 - Whiteboard

# Fizz Buzz
# Write a function to that takes one parameter
# If the number is divisible by 3, print 'Fizz' instead of the number
# If the number is divisible 5, print 'Buzz' instead of the number
# If the number is divisible by both 3 and 5, print 'FizzBuzz' instead of the number
# Otherwise, simply print the number


def word_count(string):
    string = string.lower()
    sentence1 = "'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found')"
    word_dict = {}
    sentence1 = string.split(" ")
    for sel_word in sentence1:
        count = 0
        for word in sentence1:
            if sel_word == word:
                count +=1
        word_dict[sel_word] = count
    return word_dict
    word_count()