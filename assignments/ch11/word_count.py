def main:
    print("this program analyzes word frequency in a file")
    print("and prints a report on the n most frequency words.\n")
    f_name = input("File to analyze: ")
    text = open(f_name, 'r').read()
    text = text.lower()

    #rest is in the text book
