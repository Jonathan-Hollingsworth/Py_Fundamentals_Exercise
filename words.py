alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def print_upper_words(words, must_start_with=alphabet):
    """Prints all given words that match the (must_start_with) condition in full Uppercase
       (if there is no condition given then it will print all words given)
       
       Example:
          
          print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with=["h", "y"])

       Should print the following:
         "HELLO"
         "HEY"
         "YO"
         "YES"
    """
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with=["h", "y"])