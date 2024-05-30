from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 1000)

    # 2. Print out the random variable that you made in step #1
    print(random_num)
    # 3. Code a for loop to run steps 4-10, 10 times
    for n in range(10):
        # 4. Ask the user for a guess using a pop-up window, and save their response
        yourscrewed=simpledialog.askinteger(title='',prompt='what is the number one in 1000')
        # 5. If the guess is correct
            # 6. Win. Use 'sys.exit(0)' to end the program
        if random_num==yourscrewed:


            messagebox.showinfo(title='',message='you win lol')
            sys.exit(0)
        elif random_num<yourscrewed:
            messagebox.showinfo(title='',message='no too high')
        else:
            messagebox.showinfo(title='',message='no too low')
    messagebox.showinfo(title='',message='you lose lol')
        # 7. if the guess is high
            # 8. Tell them it's too high
        # 9. Else if the guess is low
            # 10. Tell them it's too low

    #11. Outside of the loop, tell the user they lost

    window.mainloop()
