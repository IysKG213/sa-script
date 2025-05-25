import tkinter as tk
from tkinter import filedialog, messagebox
from logic import modify_excel_file

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        dir_entry.delete(0, tk.END)
        dir_entry.insert(0, directory)

def run_process():
    directory = dir_entry.get()
    filename = file_entry.get()
    theme_number = theme_entry.get()
    cell_address = cell_entry.get()
    yyyymm = date_entry.get()

    if not all([directory, filename, theme_number, cell_address, yyyymm]):
        messagebox.showerror("入力エラー", "すべての項目を入力してください。")
        return

    success, message = modify_excel_file(directory, filename, theme_number, cell_address, yyyymm)
    if success:
        messagebox.showinfo("成功", f"保存しました:\n{message}")
    else:
        messagebox.showerror("エラー", message)

# GUI構築
root = tk.Tk()
root.title("Excel テーマ番号変更ツール")

tk.Label(root, text="1. ディレクトリ:").grid(row=0, column=0, sticky="e")
dir_entry = tk.Entry(root, width=50)
dir_entry.grid(row=0, column=1)
tk.Button(root, text="参照", command=browse_directory).grid(row=0, column=2)

tk.Label(root, text="2. ファイル名:").grid(row=1, column=0, sticky="e")
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=1, column=1, columnspan=2)

tk.Label(root, text="3. テーマ番号:").grid(row=2, column=0, sticky="e")
theme_entry = tk.Entry(root, width=50)
theme_entry.grid(row=2, column=1, columnspan=2)

tk.Label(root, text="4. 修正するセル:").grid(row=3, column=0, sticky="e")
cell_entry = tk.Entry(root, width=50)
cell_entry.grid(row=3, column=1, columnspan=2)

tk.Label(root, text="5. 年月 (YYYY.MM):").grid(row=4, column=0, sticky="e")
date_entry = tk.Entry(root, width=50)
date_entry.grid(row=4, column=1, columnspan=2)

tk.Button(root, text="実行", command=run_process, bg="lightgreen").grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()
