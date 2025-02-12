# Funkcije koje definiramo izvan main() služe za specifične zadatke i operacije unutar programa.
# Pomažu u organizaciji koda tako da svaki dio programa ima svoju jasno definiranu odgovornost (npr. čitanje datoteke, obrada podataka, ispis rezultata).

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_count_char(text):
    text = text.lower()                 # Pretvaramo sve u mala slova
    count_appear = {}                   # Rječnik za brojanje znakova
                                    # koristimo get(char, 0) da izbjegnemo KeyError ako znak još nije u rječniku.
                                    # automatski inicijaliziramo znak na 0 ako se pojavljuje prvi put, povećavamo broj ponavljanja znaka za +1 svaki put kad se ponovi.
    for char in text:
        count_appear[char] = count_appear.get(char, 0) + 1      #efikasan način brojanja znakova u stringu
    return count_appear


def get_print_report(count_appear):
    alpha_dic = {}

    for char in count_appear:
        if char.isalpha():
            alpha_dic[char] = count_appear[char]
    
    filter_alpha_dic = []
    for char, count in alpha_dic.items():
        filter_alpha_dic.append({"char": char, "count": count})

    return filter_alpha_dic


def sort_by_count(item):    #u sorted() funkciji svaki element liste (rječnik) predstavlja jedan item. Zato je bolje ime item
    return item["count"]

def sorted_dic(filter_alpha_dic):
    sorted_char_dic = sorted(filter_alpha_dic, key=sort_by_count, reverse=True)
    return sorted_char_dic

#key=sort_by_count govori py da treba sortirati listu na temelju vrijednosti vraćenih iz sort_by_count(item)


def print_char_report(sorted_char_dic):
    for char_info in sorted_char_dic:
        print(f"The '{char_info['char']}' character was found {char_info['count']} times")



def main():
    book_path = "books/frankenstein.txt"        # Main funkcija se nalazi na dnu, ona organizira tok programa i pozivamo
    text = get_book_text(book_path)             # prethodno definirane pomoćne funkcije. To pomaže u održavanju čistoće i modularnosti koda.
    count_words = get_num_words(text)
     #print("test za chars: ", char)
    count_appear = get_count_char(text)
    #print(f"{count_words} words found in the document")

    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words} words found in the document")

    abc_char_list = get_print_report(count_appear)
    sorted_char_dic = sorted_dic(abc_char_list)
    print_char_report(sorted_char_dic)

    print("--- End report ---")











if __name__ == '__main__':      # Osigurava da se glavna funkcija pokrene samo kada se skripta izvršava izravno.
    main()
