
c ="aabaab"
c = list(c) #converts cipher text to list
c_shift = c
for j in range(1, 26): # I want to shift cipher text 26 times
    collisions = 0
    # remove last character from ciphertext
    last: str = c_shift.pop()

    # add last character to front of ciphertext (shifting by 1 every 
    # time for loop iterates)
    c_shift.insert(0, last)

    #this is where my code stops functioning correctly. 

    for k in range(len(c)):
        for l in range(len(c_shift)):
            if c[k] == c_shift[l]: 
                collisions += 1 # adds 1 to collision counter
        print(j, ", ", collisions)
        collisions = 0 
        # resets collision counter for next for loop iteration