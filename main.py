def main():
    count = 0
    new_dict = {}
    dict_list = []

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    words = file_contents.split()
    for word in words:
        count += 1


    # Function to count how many times a letter appears in the text
    def count_characters(text):
        new_text = text.lower()

        for letter in new_text:
            if letter not in new_dict:
                new_dict[letter] = 1
            else:
                new_dict[letter] += 1
        return new_dict
   

    x = count_characters(file_contents)

    # add key value dict pairs to the list
    for item in x:
        if item.isalpha():
            dict_list.append({item: x[item]})

    # sort by the key
    def sort_on(dict):
        for pair in dict:
            return dict[pair]

    dict_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document\n")

    for item in dict_list:
        for key in item:
            print(f"The '{key}' character was found {item[key]} times")
    print("--- End Report ---")


main()