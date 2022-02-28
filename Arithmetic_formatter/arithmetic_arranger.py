def arithmetic_arranger(problems,*args):    

    # problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    isvalid = problem_validator(problems)

    if isvalid:
        firstLine = []
        secondLine = []
        thirdline = []
        resultLine = []

        for prob in problems:
            if ('+' in prob):
                qsplit = prob.split('+') # split the problem with operator                
                num1 = qsplit[0].strip() # get the first number
                num2 = qsplit[1].strip() # get the second number
                diffLen = max(len(num1),len(num2)) - min(len(num1),len(num2))
                res = int(num1) + int(num2)
                if len(num1) > len(num2): # if first number len > second number len
                    firstLine.append('  '+num1)
                    secondLine.append('+ '+' '*diffLen+num2)
                else:
                    firstLine.append('  '+' '*diffLen+num1)
                    secondLine.append('+ '+num2)
                
                thirdline.append('--'+'-'*max(len(num1),len(num2)))
                resultLine.append(' '*(len('--'+'-'*max(len(num1),len(num2))) - len(str(res)))+str(res))
            else:
                qsplit = prob.split('-')
                num1 = qsplit[0].strip()
                num2 = qsplit[1].strip()
                diffLen = max(len(num1),len(num2)) - min(len(num1),len(num2))
                res = int(num1) - int(num2)
                if len(num1) > len(num2):
                    firstLine.append('  '+num1)
                    secondLine.append('- '+' '*diffLen+num2)
                else:
                    firstLine.append('  '+' '*diffLen+num1)
                    secondLine.append('- '+num2)
                thirdline.append('--'+'-'*max(len(num1),len(num2)))
                resultLine.append(' '*(len('--'+'-'*max(len(num1),len(num2))) - len(str(res)))+str(res))
    
    if args:
        arranged_problems = format_output(firstLine,secondLine,thirdline,resultLine)
    else:
        arranged_problems = format_output(firstLine,secondLine,thirdline)

    return arranged_problems

def format_output(firstLine,secondLine,thirdline,*args):
    opline1 = ''
    opline2 = ''
    opline3 = ''
    opline4 = ''

    for i in range(0,len(firstLine)-1):
        opline1 = opline1 + str(firstLine[i]) + '    '
        opline2 = opline2 + str(secondLine[i]) + '    '
        opline3 = opline3 + str(thirdline[i]) + '    '
    
    opline1 = opline1 + str(firstLine[len(firstLine)-1])
    opline2 = opline2 + str(secondLine[len(firstLine)-1])
    opline3 = opline3 + str(thirdline[len(firstLine)-1])

    if args:
        resultLine = list(args)[0]
        for i in range(0,len(resultLine)-1):
            opline4 = opline4 + str((resultLine[i])) + '    '
        opline4 = opline4 + str(resultLine[len(resultLine)-1])
        return opline1+'\n'+opline2+'\n'+opline3+'\n'+opline4
    else:
        return opline1+'\n'+opline2+'\n'+opline3
    


def problem_validator(problems):
    isvalid = True

    # If there are too many problems supplied to the function. The limit is five, anything more will return:
    # "Error: Too many problems."
    if len(problems) >= 5:
        print('Error: Too many problems.')
        isvalid = False
    else:
        # The appropriate operators the function will accept are addition and subtraction.
        # Multiplication and division will return an error.
        # Other operators not mentioned in this bullet point will not need to be tested.
        # The error returned will be: Error: Operator must be '+' or '-'.
        for prob in problems:
            if (('+' not in prob) and ('-' not in prob)):
                print("Error: Operator must be '+' or '-'.")
                isvalid = False
                break
            else:
                
                # Each number (operand) should only contain digits.
                # Otherwise, the function will return: Error: Numbers must only contain digits.
                
                if ('+' in prob):
                    qsplit = prob.split('+')
                    isvalid = check_ifnumbers(qsplit)
                else:
                    qsplit = prob.split('-')
                    isvalid = check_ifnumbers(qsplit)
        return isvalid

def check_ifnumbers(qsplit):
    is_valid = True
    for ques_ in qsplit:
        if not ques_.strip().isnumeric():
            print("Error: Numbers must only contain digits.")
            is_valid = False
            break
        else:
        # Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be:
        # Error: Numbers cannot be more than four digits.
            if len(ques_.strip()) > 4:
                print("Error: Numbers cannot be more than four digits.")
                is_valid = False
                break
    return is_valid
            
        
 
    
