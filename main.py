from stats import get_num_words

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_dict(text)
    report = get_report(text)
    return report

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_char_dict(text):
    symbol_dict = {}
    for symbol in text:
        lowered = symbol.lower()
        if lowered not in symbol_dict:
            symbol_dict[lowered] = 1
        else:
            symbol_dict[lowered] += 1
    return symbol_dict

def get_report(text):
    print(f"=== Begin report of books/frankenstein.txt ===\n{get_num_words(text)} words found in the document")
    dict = get_char_dict(text)
    for c in dict:
        if c in "abcdefghijklmnopqrstuvwxyz":
            print (f"The '{c}' character was found {dict[c]} times")
    print("=== End report ===")



main()