def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    characters = get_character_count(text)
    print_report(book_path, num_words, characters)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_dict = {}
    for char in text:
        if char.isalpha():
            character_dict[char.lower()] = character_dict.get(char.lower(), 0) + 1
    return character_dict

def get_character_dict_array(characters):
    character_dict_array = []
    for character in characters.keys():
        character_dict_array.append({'character': character, 'count':characters[character]})

    def sort_on_count(dict):
        return dict['count']
    
    character_dict_array.sort(reverse=True, key=sort_on_count)
    return character_dict_array
def print_report(path, count, characters):
    print(f"--- Begin report of {path} ---")
    print(f"{count} words found in the document")
    print("")
        
    character_dict_array = get_character_dict_array(characters)

    for dict in character_dict_array:
        print(f"The '{dict['character']}' character was found {dict['count']} times")
    
    print('--- End report ---')
    

main()