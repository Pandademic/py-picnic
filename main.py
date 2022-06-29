import tkinter as tk
import random

# config:

root = tk.Tk()
root.geometry("400x400")
root.title("Picnic!")


# var's/const's - TODO: remeber to use 'global'

items = ["water bottle","phone","clothes","spare socks"]

bag = []


# functions

def doStuff():
    global bag
    lenOItems = len(items)
    num = random.randint(0,lenOItems -1)
    if items[num] not in bag:
        l2["text"] = "Put item "+str(num)+" in the bag."
        bag.append(items[num])
