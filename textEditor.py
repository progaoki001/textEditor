import tkinter as tk


def open_file():
    print('open')


def save_file():
    text_data = text_box.get('1.0', 'end -1c')
    print(text_data)


# main window
root = tk.Tk()
root.title('Text Editor')
root.geometry('500x500')

# instance menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
# メニューバーにメニューを追加
file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label='file', menu=file_menu)
# メニューに操作を追加（open & save）
file_menu.add_command(label='open', command=open_file)
file_menu.add_command(label='save', command=save_file)
# label
label = tk.Label(root, text='Text Box')
label.pack()
# text box
text_box = tk.Text(root)
text_box.pack(padx=10, pady=10)

root.mainloop()

#  gitHub test01
