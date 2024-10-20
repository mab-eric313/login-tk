from tkinter import *
from tkinter import ttk

def resizeImage(img, newWidth, newHeight):
    oldWidth = img.width()
    oldHeight = img.height()
    newPhotoImage = PhotoImage(width=newWidth, height=newHeight)
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x*oldWidth/newWidth)
            yOld = int(y*oldHeight/newHeight)
            rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))
    return newPhotoImage   

root = Tk()
root.title('login')

# Frame
content = ttk.Frame(root, padding=10)
canvas = Canvas(root, borderwidth=5, relief='ridge', width=100, height=100) # Image
contentButton = ttk.Frame(root)
contentSwitch = ttk.Frame(root)

# Image
image = PhotoImage(file='beluga-cat.png')
resize_image = resizeImage(image, 120, 120)

# Content frame
login = ttk.Label(content, text='LOGIN', font='monospace 20 bold')
canvas.create_image(0, 0, anchor=NW, image=resize_image)
label_Username = ttk.Label(content, text='Username: ')
label_Password = ttk.Label(content, text='Password: ')
entry_Username = ttk.Entry(content)
entry_Password = ttk.Entry(content, show='*')
# contentButton frame
button = ttk.Button(contentButton, text='Enter', width=30)
# contentSwitch frame
switchButton = ttk.Button(contentSwitch, text='Switch', width=10)

# Content frame grid
canvas.grid(column=2, row=1)
content.grid(column=1, row=1)
login.grid(column=0, row=0)
label_Username.grid(column=0, row=1, pady=10)
label_Password.grid(column=0, row=2)
entry_Username.grid(column=1, row=1)
entry_Username.focus()
entry_Password.grid(column=1, row=2)
contentButton.grid(column=1, row=2, pady=5)
contentSwitch.grid(column=2, row=2)
button.grid()
switchButton.grid()

root.mainloop()
