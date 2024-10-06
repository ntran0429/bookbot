# print("hello world")

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    # print(text)
    
    num_words = get_word_count(text)
    print(f"{num_words} words found in the document\n")
    
    char_dict = get_character_counts(text)

    # sort by number of occurences from largest to smallest
    sorted_char_dict = sort_char_dict(char_dict)
    
    
    for char in sorted_char_dict:
        print(f"The '{char}' character was found {char_dict[char]} times")
    
    print("--- End report ---")
    
    
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_word_count(text):
    words = text.split()
    return len(words)


def get_character_counts(text):
    character_counts = {}
    
    for char in text:
        if char.isalpha(): # check whether all characters in the String are an alphabet
            lower_char = char.lower()
            if lower_char in character_counts:
                character_counts[lower_char] += 1
            else:
                character_counts[lower_char] = 1
        
    return character_counts


def sort_char_dict(dict):
    # sorted() returns a new list sorted by the values specified in the key parameter
    # The value of the key parameter should be a function (or other callable) 
    # that takes a single argument and returns a key to use for sorting purposes.
    
    # dict.items() returns a list of tuples (key-value pairs)
    # for each item in dict.items(), look at and make comparison using the 2nd item, which is the count
    
    sorted_list = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    # print(sorted_list)
    sorted_dict = {k:v for k,v in sorted_list}
    return sorted_dict



main()