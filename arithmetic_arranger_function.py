from sys import breakpointhook


def arithmetic_arranger(equation, with_result):
    counter = 1
    sum = 0
    rest = 0
    

    for i in equation:
        if counter > 5:
            print('Error: Too many problems')
            breakpointhook



        try:
            if i.index('+') > 0:                                                                
                
                #Separating the Strign and becoming it in a list
                if with_result == True:
                    operation = i.replace('+', ' ') 
                    operation = operation.split()
                
                #Checking the String does not have digits
                    for x in operation:
                        if len(x) > 4:
                            print("Error: Numbers cannot be more than four digits.")
                            breakpointhook

                    first = operation[0]
                    second = operation[1]
                    
                    #From String to Int
                    try:
                        operation = [int(x) for x in operation]                     
                    except:print("Error: Numbers must only contain digits.")

                    for x in operation:
                        sum = x + sum
                    

                    print("{:>6}".format(first),'\n','+{:>4}'.format(second),"\n", "{:>5}".format('------'),"\n","{:>5}".format(sum), '\n\n\n')
                    
                #The same above but if there is a False parameter
                elif with_result == False:
                    operation = i.replace('+', ' ') 
                    operation = operation.split()

                    for x in operation:
                        if len(x) > 4:
                            print("Error: Numbers cannot be more than four digits.")
                            breakpointhook

                    first = operation[0]
                    second = operation[1]
                    try:
                        operation = [int(x) for x in operation]    
                    except:print("Error: Numbers must only contain digits.")
                    print("{:>6}".format(first),'\n','+{:>4}'.format(second),"\n", "{:>5}".format('------'), '\n\n\n')


                else:pass
        except:pass



        try:
            if i.index('-') > 0:

                #Same above but with negative operations
                if with_result == True:
                    operation = i.replace('-', ' ')  
                    operation = operation.split()

                    for x in operation:
                        if len(x) > 4:
                            print("Error: Numbers cannot be more than four digits.")
                            breakpointhook    

                    try:
                        operation = [int(x) for x in operation]                           
                    except:print("Error: Numbers must only contain digits.")

                    for x in operation:
                        rest = x - rest
                    rest *= -1

                    first = operation[0]
                    second = operation[1]

                    print("{:>6}".format(first),'\n','-{:>4}'.format(second),"\n", "{:>5}".format('------'),"\n","{:>5}".format(rest), '\n\n\n')


                elif with_result == False:
                    operation = i.replace('-', ' ') 
                    operation = operation.split()

                    for x in operation:
                        if len(x) > 4:
                            print("Error: Numbers cannot be more than four digits.")
                            breakpointhook

                    first = operation[0]
                    second = operation[1]

                    try:
                        operation = [int(x) for x in operation]    
                    except:print("Error: Numbers must only contain digits.")

                    print("{:>6}".format(first),'\n','-{:>4}'.format(second),"\n", "{:>5}".format('------'), '\n\n\n')


                else:pass 
        except:pass



        try:
            if i.index('*') > 0:
                print("Error: Operator must be '+' or '-'")
        except:pass
        try:
            if i.index('/') > 0:
                print("Error: Operator must be '+' or '-'")
        except:pass
        counter += 1
        sum = 0
        rest = 0

