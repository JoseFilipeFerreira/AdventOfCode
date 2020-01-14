import string

def main():
    with open("input.txt", 'r') as file:
        text = file.read()
        text = list(text)

        short_size = 100000
        for l in list(string.ascii_lowercase):
            alter_text = list(filter(lambda x: x.lower() != l, text))
            alter_text = ''.join(alter_text)

            reduced = True
            while reduced:
                reduced = False
                size = len(alter_text)-1
                pos = 0
                while pos < size:
                    if compare(alter_text[pos], alter_text[pos+1]):
                        reduced = True
                        alter_text = alter_text[:pos] + alter_text[(pos+2):]
                        size -= 2
                    else:
                        pos += 1

            print(l)
            print(len(alter_text))
            if len(alter_text) < short_size: 
                short_size = len(alter_text)
        print("solution:")
        print(short_size)

def compare(char1, char2):
    if char1.lower() == char2.lower():
        if char1.isupper() and char2.islower():
            return True
        if char2.isupper() and char1.islower():
            return True
    return False
 
main()