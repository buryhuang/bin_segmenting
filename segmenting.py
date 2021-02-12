#!/usr/bin/python
import sys

fileName = sys.argv[1]

cal_window = 32
seg_window = 1*1024

def max_of_list(data):
    max_val = -1
    max_index = 0
    curr_index = 0
    for d in data:
        if d > max_val:
            max_val = d
            max_index = curr_index
        curr_index += 1
    return (max_index, max_val)

with open(fileName, mode='rb') as file: # b is important -> binary
    fileContent = file.read()

file_sums = []

current_byte_index = 0
while True:
    window_values = []
    curr_sum = 0
    for i in range(cal_window):
        byte_val = ord(fileContent[current_byte_index + i])
        curr_sum += byte_val*byte_val
    file_sums.append(curr_sum)
    current_byte_index += 1
    if current_byte_index >= len(fileContent):
        break

# print(file_sums)

current_start = 0
chunk_index = 0
while True:
    current_end = current_start+seg_window
    if current_end > len(file_sums):
        current_end = len(file_sums)

    (curr_index, curr_max) = max_of_list(file_sums[current_start:current_end])

    # print((current_start, current_start + curr_index, curr_index, curr_max))
    print((curr_index, curr_max))
    current_start = current_start + curr_index + 1
    chunk_index += 1
    if current_start >= len(file_sums):
        break
