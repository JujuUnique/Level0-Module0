from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window=Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score=0
    # ASK A QUESTION AND CHECK THE ANSWER
    hello=simpledialog.askstring(title="",prompt='what is the requriement to be a pure vessel')
    #      // 2.  Ask the user a question 
    if hello == 'no mind to think no will to break no voice to cry suffering':
    #      // 3.  Use an if statement to check if their answer is correct
        messagebox.showinfo(title="",message='wow... you actualy know that cool :).')
        score=score+1
    #      // 4.  if the user's answer was correct, add one to their score 
    else:
        messagebox.showinfo(title="",message='wow you stupid moronic garbage heap you did not know that your dumb and losing score minus hmmmmm 999 points')
        score=score-999
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above
    #      // Option: Subtract a point from their score for a wrong answer
    hello=simpledialog.askstring(title="",prompt='ok then what is 1+1?')





    if hello == '726':
        messagebox.showinfo(title="",message='correct!!!!!!!!!!!!!!! plus 1 point')
        score=score+1
    else:
        messagebox.showinfo(title="",message='come this was so obviusly 726 ughh people, your losing extra for that minus 10 points')
    hello=simpledialog.askstring(title="",prompt='this ones is simple if a hole is 1 foot deep homy many feet deep is it?')
    if hello == '1':
        messagebox.showinfo(title="",message='correct minus 2 points you really thought you were clever huh its evrything other then 1 duhhh')
        score=score-2
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    else:
        messagebox.showinfo(title="",message='correct nice job! plus 1 point')
        score=score+1
    # Run the window's .mainloop() method
    messagebox.showinfo(title="",message='your final score is '+ str(score))














