run = True 
while run == True:
    LoopStart = 1
    LoopEnd = 101
    LoopIncrement = 1
    Mode = 0
    #mode select
    while Mode == 0 or Mode == 5:
        if Mode == 0:
            print('''Please enter the number for the mode you would like to run.
            1) Square all numbers from 1-100
            2) Square numbers from 1 to 100 until the sqaured number is equal to or greater than 200
            3) Input your own range of numbers.
            4) End program''')
        elif Mode == 5:
            print("Please enter 1,2, or 3 to select one of the modes.")
        Mode = int(input())
        if Mode == 1:
            print ("you have chosen mode 1")
        elif Mode == 2:
            print ("you have chosen mode 2")
        elif Mode == 3:
            print ("you have chosen mode 3")
        elif Mode == 4:
            run = False
            #break
        else:
            Mode = 5
    if Mode == 3:
        LoopStart = int(input("Enter the staring number of the range:"))
        LoopEnd = int(input("Enter the ending number of the range, this is the number the loop will stop with. So if you want to loop to 10, enter 11 as it will then loop to 10 and stop at 11:"))
        LoopIncrement = int(input("Enter the amount you want the loop to increment each number:"))
    if Mode == 4:
        break
    
    for i in range(LoopStart, LoopEnd, LoopIncrement):
        Square = i**2
        if Square >= 200 and Mode == 2:
            break
        print (i,"Squared =",Square)
