def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    total = 0
   
    for x in range(5):
        total += (int)(input("Enter a number to add to total: "))
    
    print(total)
    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
