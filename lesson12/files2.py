file_path = "files/data/AAPL.csv"
#
# vol_sum = 0
# vol_cnt = 0
# with open(file_path) as f:
#     # skip the header
#     f.readline()
#     for line in f:
#         vol_sum += int(line.split(',')[3])
#         vol_cnt += 1
# print(vol_sum/vol_cnt)

import csv


with open(file_path) as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row['Volume'])
