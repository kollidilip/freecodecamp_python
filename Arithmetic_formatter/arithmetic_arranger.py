def arithmetic_arranger(problems):
    
    # problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    
    # If there are too many problems supplied to the function. The limit is five, anything more will return:
    # "Error: Too many problems."
    if len(problems) >= 5:
        print('Error: Too many problems.')
    else:
        # The appropriate operators the function will accept are addition and subtraction.
        # Multiplication and division will return an error.
        # Other operators not mentioned in this bullet point will not need to be tested.
        # The error returned will be: Error: Operator must be '+' or '-'.
        for prob in problems:
            if (('+' not in prob) and ('-' not in prob)):
                print("Error: Operator must be '+' or '-'.")
                break
            else:
                
                # Each number (operand) should only contain digits.
                # Otherwise, the function will return: Error: Numbers must only contain digits.
                
                if ('+' in prob):
                    qsplit = prob.split('+')
                    check_ifnumbers(qsplit)
                else:
                    qsplit = prob.split('-')
                    check_ifnumbers(qsplit)
                    

                    
                    
                



    return 'end'


def check_ifnumbers(qsplit):
    for ques_ in qsplit:
        if not ques_.strip().isnumeric():
            print("Error: Numbers must only contain digits.")

            
            
            
        
 
    
