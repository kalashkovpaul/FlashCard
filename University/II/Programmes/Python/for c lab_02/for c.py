lengths = [10, 500, 1000, 5000, 10000]
file_ten = open("10.txt", 'w')
file_hundred = open('500.txt', 'w')
file_thousand = open('1000.txt', 'w')
file_five_thousand = open('5000.txt', 'w')
file_ten_thousand = open('10000.txt', 'w')
for i in range(lengths[0], 0, -1):
    file_ten.write(str(i) + "\n")
for i in range(lengths[1], 0, -1):
    file_hundred.write(str(i) + "\n")
for i in range(lengths[2], 0, -1):
    file_thousand.write(str(i) + "\n")
for i in range(lengths[3], 0, -1):
    file_five_thousand.write(str(i) + "\n")
for i in range(lengths[4], 0, -1):
    file_ten_thousand.write(str(i) + "\n")
file_ten.close()
file_hundred.close()
file_thousand.close()
file_five_thousand.close()
file_ten_thousand.close()