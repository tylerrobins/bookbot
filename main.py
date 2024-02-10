def main():
    book_path = "books/frankenstein.txt"
    file_content = get_book_content(book_path)
    word_count = count_words(file_content)
    letter_count = count_letters(file_content)
    sorted_list = sorted_dict_list(letter_count)
        
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for i in sorted_list:
        char = i["char"]
        num = i["num"]
        print(f"The '{char}' character was found {num} times")
    print("--- End Report ---")

def count_words(file_content):
    words = file_content.split()
    return len(words)

def count_letters(file_content):
    letter_count = {}
    for i in file_content:
        x = i.lower()
        if x.isalpha():
            if x in letter_count:
                letter_count[x] += 1
            else:
                letter_count[x] = 1
    return letter_count

def sort_on(dict):
    return dict["num"]

def sorted_dict_list(dict):
    dict_list = []
    for i in dict:
        dict_list.append({"char":i, "num": dict[i]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list    

def get_book_content(path):
    with open(path) as f:
        return f.read()
    
main()