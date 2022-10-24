def arithmetic_arranger(equation, with_result):
    counter = 1
    sum = 0
    rest = 0
    

    for i in equation:
        if counter > 5:
            print('Error: Too many problems')
        else:



            try:
                if i.index('+') > 0:                                                                
                    
                    #Separating the Strign and becoming it in a list
                    if with_result == True:
                        operation = i.replace('+', ' ') 
                        operation = operation.split()
                    
                    #Checking the String does not have digits
                        for x in operation:
                            if len(x) > 4:
                                operation_rule = False
                                break
                            else:
                                operation_rule = True
                    
                        first = operation[0]
                        second = operation[1]
                        
                        #From String to Int & Checking number rule
                        try:
                            operation = [int(x) for x in operation]                     
                        except:print("Error: Numbers must only contain digits.")

                        for x in operation:
                            sum = x + sum
                        
                        #Display-Positive-True
                        if operation_rule == True:
                            print("{:>6}".format(first),'\n','+{:>4}'.format(second),"\n", "{:>5}".format('------'),"{:>5}".format(sum), '\n\n\n')
                        elif operation_rule == False:
                            print("Error: Numbers cannot be more than four digits.")

                        
                    #Same above but with False parameter
                    elif with_result == False:
                        operation = i.replace('+', ' ') 
                        operation = operation.split()

                        for x in operation:
                            if len(x) > 4:
                                operation_rule = False
                                break
                            else:
                                operation_rule = True

                        first = operation[0]
                        second = operation[1]

                        try:
                            operation = [int(x) for x in operation]    
                        except:print("Error: Numbers must only contain digits.")

                        for x in operation:
                            sum = x + sum

                        #Display-Positive-False
                        if operation_rule == True:
                            print("{:>6}".format(first),'\n','+{:>4}'.format(second),"\n", "{:>5}".format('------'), '\n\n\n')
                        elif operation_rule == False:
                            print("Error: Numbers cannot be more than four digits.")
                            

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
                                operation_rule = False
                                break
                            else:
                                operation_rule = True

                        first = operation[0]
                        second = operation[1]

                        
                        try:
                            operation = [int(x) for x in operation]                           
                        except:print("Error: Numbers must only contain digits.")

                        for x in operation:
                            rest = x - rest
                        rest *= -1

                        #Display-Negative-True
                        if operation_rule == True:
                            print("{:>6}".format(first),'\n','-{:>4}'.format(second),"\n", "{:>5}".format('------'),"\n","{:>5}".format(rest), '\n\n\n')
                        elif operation_rule == False:
                            print("Error: Numbers cannot be more than four digits.")

                    elif with_result == False:
                        operation = i.replace('-', ' ') 
                        operation = operation.split()

                        for x in operation:
                            if len(x) > 4:
                                operation_rule = False
                                break
                            else:
                                operation_rule = True
                        
                        first = operation[0]
                        second = operation[1]

                        try:
                            operation = [int(x) for x in operation]    
                        except:print("Error: Numbers must only contain digits.")

                        for x in operation:
                            rest = x - rest
                        rest *= -1                    

                        #Display-Negative-False
                        if operation_rule == True:
                            print("{:>6}".format(first),'\n','-{:>4}'.format(second),"\n", "{:>5}".format('------'),"\n","{:>5}".format(rest), '\n\n\n')
                        elif operation_rule == False:
                            print("Error: Numbers cannot be more than four digits.")


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


arithmetic_arranger(['111 + 1','111 + 2','111 + 3','111 + 4','111 + 5','111 + 6'], False)
