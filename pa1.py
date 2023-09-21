import csv
import sys


def try1(column1, column2):
    link1 = []
    head_values = []
    tail_values = []
    all_links = []
    # possible start of a any link (start point always from column1 in this case)
    for i in range(len(column1)):
        if column1[i] not in column2 and column2[i] in column1:
            head_values.append(column1[i])
        
    # possible end of any link (end point always from column2 in this case)
    for i in range(len(column1)):
        if column2[i] not in column1 and column1[i] in column2:
            tail_values.append(column2[i])    

    # Trying to add head 22:
    for head in head_values:
        value = head
        link1.append(value)
        while value not in tail_values:
            key = column1.index(value)
            link1.append(column2[key])
            value = column2[key]
        all_links.append(link1)
        all_links.append(len(link1))
        link1 = []

    max = 0
    for i in range(1, len(all_links), 2):
        if all_links[i] > max:
            max = all_links[i]
        
    max_length_index = all_links.index(max) - 1
    print(f"{all_links[max_length_index]} with length {max}")


def main():
   
    if len(sys.argv) != 2:
        print("Usage: python pa1.py <input-pa1-small.csv>")
        return
    filename = sys.argv[1]
    try:
        column1 = []
        column2 = []
        file = open(filename, 'r')
        csv_reader = csv.reader(file) 
        for row in csv_reader:
            num1, num2 = int(row[0]), int(row[1])
            column1.append(num1)
            column2.append(num2)      
    except FileNotFoundError:
        print(f"Could not find {filename}")
        return
    
    try1(column1, column2)

    
       
    return
    
main()

'''
link = []
all_possible_links = []
head = []
tail = []
loop from i = 0 to the length:
    if column1[i] is in column1 and column1[i] is not in column2:
        add column1[i] to head
    if column2[i] is in column2 and column2[i] is not in column1:
        add column2[i] to tail
        
loop through each element of head:
    while element of head is not in tail:
        add element of head to link
        add element of column2 corresponding to head to link --> key
        add element of column2 corresponding to column1 that has the key value to link
        
    add link into all_possible_links
    add length of link into all_possible_links
    
Find the longest length in all_possible_links
Print the longest link in all_possible_links

'''