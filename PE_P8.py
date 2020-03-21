######################################################################################################################
# Project Euler
# Problem 8
# File name: PE_P8.py
# Compile: python PE_P8.py
# Programer: Alexis Lopez
# Description: Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. 
# What is the value of this product?
######################################################################################################################

print(r"Welcome to 'Project Euler' This is problem #8")

def countDigits(digits):
        return len(str(abs(digits))) 

# Computing square of the sum of natural numbers
def search(lenght):

    # Defining all the arrays need it
    big_fat_array = []
    only_correct_size = []
    final_number = []
    final_number_digits = []
    result_products = []
    
    # Putting our data NOTE it needs to end in zero in order to work.
    big_fat_number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    big_fat_number_str = str(big_fat_number)
    
    # Defining all variables need it
    index_store = 0
    correct_index = 0
    product = 1
    new_b = 0
    
    # Defining all the strings need it
    string_number = ""
    new_string = ""
    
    # Storing all consecutive digits that don't have a zero.
    for sort in range(len(big_fat_number_str)):
        
        # Store the number until a zero is encounter
        if (big_fat_number_str[sort] != '0'):
            string_number = string_number + big_fat_number_str[sort]
        
        # If a zero is encounter store the number before the zero into an array.
        if (big_fat_number_str[sort] == '0'):
            big_fat_array.insert(index_store, string_number)
            index_store = index_store + 1
            string_number = ""
    
    # Just taking numbers that are bigger or equal to the length specified
    for correct_lenght in range(len(big_fat_array)):
        number = big_fat_array[correct_lenght]
        
        # Storing all numbers bigger than the lenght specified into new array
        if (len(number) >= lenght):
            only_correct_size.insert(correct_index, number)
            correct_index = correct_index + 1   
    
    #for x in range(len(big_fat_array)):
    #    print("what is on the array is: ", big_fat_array[x])
        
    #for y in range(len(only_correct_size)):
    #    print("what is on the only correct array is: ", only_correct_size[y])
    
    # Saves all posible numbers of the size specified
    for a in range(len(only_correct_size)):
    
        # Grabs the firts number in the array
        temp_str = only_correct_size[a]
        
        # Sets variables to calculate all possible numbers that can be made with the
        # lenght specified
        b = 0
        new_b = 0
        new_string = ""
        
        # We only want to loop until we reach the end of that specific number
        while b <= (len(temp_str) - 1):
            
            # We keep pushing digits until we get the desired number of digits
            new_string += temp_str[b]
            
            # Once we have reach the specified number of digits we store the number
            # and set our counter(b) to get the next possible number from the same
            # number meaning if we have 1234 and we want possible values with two
            # digits it will store 12, 23, 34.
            if (b - new_b == lenght - 1):
                final_number.append(int(new_string))
                new_string = ""
                new_b = b - (lenght - 2)
                b = new_b
            else: 
                b += 1
    
    #for c in range(len(final_number)):
    #    print("This should be all 13-digits number: ", final_number[c])  
    
    # Computes the product of every 13-digit number i.e. 1234 = 1*2*3*4 = 24
    for i in range(0,len(final_number)):
        
        # Computes the multiplication of each digit
        for g in range(0, lenght):
            product = product * (final_number[i] % 10)
            final_number[i] = final_number[i] // 10
            
            # Stores the result in an array and reset product for next multiplication
            if(g == lenght - 1):
                result_products.insert(i, product)
                product = 1
    
    # return the biggest product of all that have been calculated.    
    return max(result_products)


if __name__ == "__main__":

    input_digits = int(input("\nHow many consecutives digits you want to find?: "))
    
    if(input_digits > 0):
        biggest_product = search(input_digits)
        print("\nThe biggest product of the {}-digit number is: {}".format(input_digits, biggest_product))
        
    elif(input_digits == 0):
        print("\nThe biggest product of the {}-digit number is: NOTHING!! CABRON!! >:(".format(input_digits))
        
    else:
        print("Don't be an ASSHOLE!! and enter positive numbers!! :/")
    