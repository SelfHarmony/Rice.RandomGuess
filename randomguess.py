# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random



d = {'r': 100, 'LIVES': 7, 'secret_number': 25}

# helper function to start and restart the game
def new_game():
    victory = 0
    d['secret_number'] = random.randrange(0, d['r'])
    #print d['secret_number']
    print "starting new game of", str(d['r'])
    print ""
    if d['r'] == 100:
        d['LIVES'] = 7
    elif d['r'] == 1000:
        d['LIVES'] = 10
    
    
    
def button_try():
    input_guess(inp.get_text())


# define event handlers for control panel
def range100():
    d['r'] = 100 # button that changes the range to [0,100) and starts a new game 
    print "range changed to [1, " + str(d['r']) +")"
    #print ""
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    d['r'] = 1000
    print "range changed to [1, " + str(d['r']) +")"
    #print ""
    new_game()
    
def input_guess(guess):

    try:
        if d['LIVES'] != 0 :
            d['LIVES'] = d['LIVES'] - 1
            int_guess = int(guess)	
            print "Your guess is",  int_guess 
            if d['secret_number'] > int_guess :
                print "Higher"
                #print "secret number is", secret_number
                if d['LIVES'] != 0:
                    print "remaining attempts", d['LIVES']
                    print " "
                else: 
                    print "out of attempts, your number was", str(secret_number)
                    print " "
                    print "i'm sorry! try again!"
                    print ""
                    new_game()
            elif d['secret_number'] < int_guess:
                print "Lower"
                #print "secret number is", secret_number
                if d['LIVES'] !=0:
                    print "remaining attempts", d['LIVES']
                    print " "
                else:
                    print "out of attempts, your number was", str(secret_number)
                    print " "
                    print "i'm sorry! try again!"
                    print ""
                    new_game()
            else : 
                
                #d['LIVES'] = 0
                print "Correct"
                print "Hey, lucky winner! Let's start over!"
                print""              
                new_game()
                
        #elif d['LIVES'] == 0: 
            #print "out of attempts, your number was", str(secret_number)
            #print "i'm sorry! try again!"
            #print "" 
            #new_game()

    

    except ValueError:
            print "Oops!  That was not a number.  Try again..."
            print "remaining attempts", d['LIVES']
            print ""


    
# create frame
frame = simplegui.create_frame('Testing', 200, 200)



# register event handlers for control elements and start frame
inp = frame.add_input('Your_guess', input_guess, 150)
inp.set_text('25')
button0 = frame.add_button('guess it', button_try)
button1 = frame.add_button('Guess from 100', range100)
button2 = frame.add_button('Guess from 1000', range1000)
button3 = frame.add_button('newgame', new_game)

#button3 = frame.add_button('Guess from input', input_guess(input()))



# call new_game 
print "In this game you have to guess"
print "the number that computer has set"
print ""
new_game()


# always remember to check your completed program against the grading rubric
    