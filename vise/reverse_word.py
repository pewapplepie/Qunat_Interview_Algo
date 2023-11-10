import re

def reverse_words(sentence):
   # remove leading, trailing and multiple spaces
   sentence = re.sub(' +',' ',sentence.strip())
   print('debugging: ')
   print(sentence)
   # We need to convert the updated string
   # to lists of characters as strings are immutable in Python
   sentence = list(sentence)
   str_len = len(sentence)
   print(sentence)
   
   #  We will first reverse the entire string.
   str_rev(sentence, 0, str_len - 1)
   #  Now all the words are in the desired location, but
   #  in reverse order: "Hello World" -> "dlroW olleH".
 
   start = 0
   end = 0

   # Now, let's iterate the reversed string and reverse each word in place.
   # "dlroW olleH" -> "World Hello"

   while (start < str_len):
      # Find the end index of the word. 
    while end < str_len and sentence[end] != ' ':
        end += 1
     # Let's call our helper function to reverse the word in-place.
    str_rev(sentence, start, end - 1)
    start = end + 1;
    end += 1
  
   return ''.join(sentence)


# A function that reverses a whole sentence character by character
def str_rev(_str, start_rev, end_rev):
   # Starting from the two ends of the list, and moving
   # in towards the centre of the string, swap the characters
   while start_rev < end_rev:
       temp = _str[start_rev]          # temp store for swapping
       _str[start_rev] = _str[end_rev]  # swap step 1
       _str[end_rev] = temp            # swap step 2


       start_rev += 1                  # Move forwards towards the middle
       end_rev -= 1                    # Move backwards towards the middle



def main():
    string_to_reverse = ["Hello Friend", "    We love Python",
                         "The quick brown fox jumped over the lazy dog   ",
                         "Hey", "To be or not to be",
                         "AAAAA","Hello     World"]

    for i in range(len(string_to_reverse)):
        # print(i+1, ".\t Actual string:\t\t" +
        #       "".join(string_to_reverse[i]), sep='')
        Result = reverse_words(string_to_reverse[i])
        print("result: ")
        print(Result)
        # print("\t Reversed string:\t" +
        #       "".join(Result), sep='')
        print("-"*100)


# if __name__ == '__main__':
main()