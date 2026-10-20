# numbers=(10,12,-12,14,-15,-13,16,17,-18)
# positives=tuple(filter(lambda x: x>0,numbers))
# plusnum=tuple(map(lambda x: x + 5, numbers))
# print(positives)
# print(plusnum)

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
    return count
text = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmaaaaaaaaaaaaaaaaaaaa"
print("Total Vowels:", count_vowels(text))