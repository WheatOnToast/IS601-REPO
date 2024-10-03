tries = 0
while(tries != 3):
    sentence = input('Enter Hello World:\n')

    if(sentence == 'Hello World'):
        print('Good job\n')
        exit()
    elif(sentence != 'Hello World'):
        tries += 1
        if(tries == 3):
            print('Attempts exceeded\n')
        else:
            print('Please try again\n')
