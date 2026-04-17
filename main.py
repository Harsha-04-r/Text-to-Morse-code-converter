morse = {'A':'.-','B':'-...', 'C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',
         '0':' -----','1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'}

def morse_code_converter(text):
    result = ""
    invalid = False
    for l in text:
        if l in morse:
            result += morse[l]
        else:
            invalid = True
    if invalid:
        print("Invalid characters")
        result = " "
    return result.strip()

should_continue = True
while should_continue:
    text_to_convert = str(input("Enter text to convert to morse code: ")).upper()

    morse_code = morse_code_converter(text_to_convert)
    print(f"Morse code: {morse_code}")

    to_continue = input("Do you wish to continue? (y/n):")

    if to_continue == "y":
        should_continue = True
    else:
        should_continue = False