import csv
import re


def findValuesBigIndent(lines):
    pass


def findValuesLittleIndent(lines):
    print("lines", lines)


with open('example2.log') as file:
    lines = file.readlines()

    # Set up our time intervals for our graph output
    timeFrames = [f"Prior {x} to {x + 2} days" for x in range(1, 20, 3)]

    for index, line in enumerate(lines):
        if " use_prior1t3days" in line:
            # If we have a little indent section of code
            if(line.find(" use_prior1t3days") < 10):
                # Send over all the lines necessary to parse data
                findValuesLittleIndent(lines[index: index + 72])
                break
            print(line.find(" use_prior1t3days"))
            IOS = ''.join(lines[index + 1: index + 3]
                          ).replace('\n> ', '')
            IOSnums = re.findall(r'[-0-9.]+', IOS)

            # print("IOS", IOS)
            # print(type(IOSnums))
            # print(IOSnums)

    with open('yourcsv.csv', 'w+') as csvfile:
        w = csv.writer(csvfile)
        w.writerow(lines)
