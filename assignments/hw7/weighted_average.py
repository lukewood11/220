"""
Name: Luke Wood

weighted_average.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    weighted_average()


def weighted_average(infile, outfile):
    infile = open(infile, 'r')
    outfile = open(outfile, 'w')
    class_size = 0
    class_acc = 0
    for line in infile:
        avg_acc = 0
        weight_acc = 0
        newline = line.split(": ")
        score_list = newline[1].split(" ")
        for i in range(0, len(score_list), 2):
            weight = score_list[i]
            weight_acc += int(weight)
        if weight_acc > 100:
            outfile.write(newline[0] + "'s average: Error: The weights are more than 100." + "\n")
        elif weight_acc < 100:
            outfile.write(newline[0] + "'s average: Error: The weights are less than 100." + "\n")
        else:
            class_size += 1
            for i in range(0, len(score_list), 2):
                average = int(score_list[i]) * int(score_list[i + 1])
                avg_acc = avg_acc + average
            avg_acc /= 100
            avg_acc = round(avg_acc, 1)
            class_acc = class_acc + avg_acc
            outfile.write(newline[0] + "'s average: " + str(avg_acc) + "\n")
    # divide class_acc by class_size
    # round that to 1 decimal place
    # output that to the outfile
    if class_size == 0:
        average = 0
    else:
        average = class_acc / class_size
    outfile.write("Class average: " + str(round(average, 1)) + "\n")


if __name__ == '__main__':
    main()
