array = [[0,1,0,0,0],
         [0,0,1,0,0],
         [0,0,0,1,0],
         [0,0,0,0,1],
         [0,0,0,0,0]] 
zero_row_found = True
while(array and zero_row_found):
    zero_row_found = False
    for i,row in enumerate(array):
        length = len(array[i])
        zero_row = [0 for length in range(length)]
        if row==zero_row:
            zero_row_found = True
            array.pop(i)
            for row in array:
                row.pop(i)

if array:
    print("CYCLIC")
else:
    print("ACYCLIC")

       
        
    
# i = 0, row = [0,1,0]  index axis is 0 or the first row inn our case
# i = 1, row = [0,0,1]
            # row[2]
