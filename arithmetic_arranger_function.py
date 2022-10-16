ecuation = ['123 + 1', '123 - 1', '123 * 1', '123 / 1']

#Know the arithmetic sign and rewrite
def arithmetic_arranger(ecuation, solve):
    for i in ecuation:


        try:
            if i.index('+') > 0:
                if solve == True:
                    result = i.replace('+', ' ')  
                    result = result.split()              
                    result = [int(x) for x in result]    #Strings becomes an Ints
                    result = sum(result)
                    print(i.replace(' ', '\n', 1) ,'\n---', '\n', result)

                else:print(i.replace(' ', '\n',1),'\n------')
        except:pass

        try:
            if i.index('-') > 0:
                if solve == True:
                    rest = 0
                    result = i.replace('-', ' ')  
                    result = result.split()              
                    result = [int(x) for x in result]
                    for x in result:
                        rest = x - rest
                    rest *= -1
                    print(i.replace(' ', '\n', 1) ,'\n---', '\n', rest)

                else:print(i.replace(' ', '\n',1),'\n------')  
        except:pass


        try:
            if i.index('*') > 0:
                print('Error: Too many problems')
        except:pass
        try:
            if i.index('/') > 0:
                print('Error: Too many problems')
        except:pass



arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)

