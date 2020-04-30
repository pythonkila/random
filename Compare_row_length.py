## 29/04/2020 Winnipeg Manitoba 
# Oluseyi Oshin
#  This function takes a dataset as a parameter.
#  The function searches through the dataset for rows that are either longer or shorter than the table's first row.

def compare_rows(dataset):
    row_l = len(dataset[0])
    count = 0
    bad_row_shorter = []
    bad_row_shorter_index = []
    bad_row_longer = []
    bad_row_longer_index = []
    for row in dataset:
        current_row_len = len(row)
        count += 1
        if current_row_len < row_l:
            bad_row_shorter.append(row)
            bad_row_shorter_index.append(count)
        elif current_row_len > row_l:
            bad_row_longer.append(row)
            bad_row_longer_index.append(count)
    #return shorter = bad_row_shorter , longer = bad_row_longer , short_index = bad_row_shorter_index , long_index = bad_row_longer_index
    return bad_row_shorter, bad_row_shorter_index, bad_row_longer, bad_row_longer_index
#The function is called below.
compare_rows(list_google)
