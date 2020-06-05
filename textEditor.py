from tkinter import filedialog
import tkinter as tk


def road_file():
    text_box.delete("1.0", "end")
    ret = tk.filedialog.askopenfilename(initialdir="~/", title="road file")
    print(ret)
    with open(ret) as f:
        road_data = f.read()
        print(road_data)


def save_file():
    text_data = text_box.get('1.0', 'end -1c')
    root.filename = filedialog.asksaveasfilename(initialdir="~/", title="Save as", filetypes=[("text file", "*.txt")])
    print(text_data)
    with open(root.filename, 'w') as f:
        f.write(text_data)


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
file_menu.add_command(label='road', command=road_file)
file_menu.add_command(label='save', command=save_file)
# label
label = tk.Label(root, text='Text Box')
label.pack()
# text box
text_box = tk.Text(root)
text_box.pack(padx=10, pady=10)

root.mainloop()
