from tkinter import *
import random

root= Tk()

root.title("Unluckey Ways to die in minecraft")
root.geometry("400x400")


list1 = ["Struck by lightning", "Squished to mutch", "Blown up by a creeper whilst escaping skeliton.", "Priked to death by swwet berry bush whilsttrying to escape MinecraftSweet987" , "Killed By a firework from MinecraftPro useing  NoobslayerCrossbow whilst escaping MinecraftGuy" ]
print(list1)

def random_number():
    random_no = random.randint(0,4)
    print(random_no)
    random_way_to_die_in_minecraft = list1[random_no]
    print("You died buy getting " +   random_way_to_die_in_minecraft)
    
    btn = Button(root)
    btn = Button(root, text=("How Will You Die? "), command = random_number)
    btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
    
root.mainloop()


