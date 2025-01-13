print("Welcome to the quiz!")
a=input("In which year India got independent?: ")
if a=='1947':
    print("Correct!")
    b=input("How many days were there in February 1900?: ")
    if b=='28':
        print("Correct!")
        c=input("How many days were there in the year 1800?: ")
        if c=='365':
            print('Correct!')
            d=input("In which year the COVID Pandemic was first Introduced?: ")
            if d=='2019':
                print("Correct!")
                e=input("In which country the COVID Pandemic was first Introduced?: ")
                x=e.lower()
                if x=='china':
                    print("Correct!",'\n',"You've answered all questions correctly")
                else:
                    print("Wrong!",'\n','The correct answer is China.')
                    
            else:
                print("Wrong!",'\n','The correct answer is 2019.')
        else:
            print("Wrong!",'\n','The correct answer is 365.')
            
    else:
        print("Wrong!",'\n','The correct answer is 28.')
else:
    print("Wrong!",'\n','The correct answer is 1947.')