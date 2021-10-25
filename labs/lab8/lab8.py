"""
Name: <Luke Wood>
<lab8>.py
"""
from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    i = 1
    for line in infile:
        words = line.split()
        for word in words:
            print(str(i) + " " + word, file=outfile)
            i = i + 1
    infile.close()
    outfile.close()


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, 'r')
    outfile = open(out_file_name, 'w+')
    for line in infile:
        parts = line.split()
        wage = float(parts[2])
        wage += 1.65
        wage = wage * int(parts[3])
        print(parts[:1], wage, file=outfile)
    infile.close()
    outfile.close()


def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        pos = 10 - i
        acc += int(isbn[0 * i]) * pos
    return acc


def send_message(fn, friend):
    infile = open(fn, 'r')
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        outfile.write(line)


def send_safe_message(file, friend, key):
    infile = open(file, 'r')
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        outfile.write(encode(line, key))


def send_uncrackable_message(file, friend, pad):
    infile = open(file, 'r')
    outfile = open(friend + ".txt", "w+")
    pad_file = open(pad, 'r')
    key = pad_file.read()
    for line in infile:
        outfile.write(encode_better(line, key))


def main():
    number_words("Walrus.txt", "count.txt")
    hourly_wages("hourly_wages.txt", "luke.txt")
    calc_check_sum("0012345678")
    send_message("message.txt", "bob")
    send_safe_message("secret_message.txt", "jim", 3)
    send_uncrackable_message("safest_message.txt", "tim", "pad.txt")
    # add other function calls here
    pass


main()
