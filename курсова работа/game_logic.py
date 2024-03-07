import cowsay

def logic(user_input, comp_pick):
    
    if user_input == "rock" and comp_pick == "scissors":
        print(cowsay.tux("You won!"))
        return "p"
       
    elif user_input == "paper" and comp_pick == "rock":
        print( cowsay.fox("You won!"))
        return "p"
      
    elif user_input == "scissors" and comp_pick == "paper":
        print (cowsay.ghostbusters("You won!") )
        return "p"
     
    elif user_input == "scissors" and comp_pick == "scissors":
       print("YOU ARE EVEN!") 
  
    elif user_input == "rock" and comp_pick == "rock":
        print("YOU ARE EVEN!")  
         
    elif user_input == "paper" and comp_pick == "paper":
        print("YOU ARE EVEN!")  
        
    else:
        
        print("YOU LOST! :(") 
        return "c"
         