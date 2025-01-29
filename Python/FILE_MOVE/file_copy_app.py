import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from file_copier import FileCopier

# GUIを担当するクラス
class FileCopyApp:
    def __init__(self):
        self.copier = FileCopier()  # FileCopierオブジェクト
        self.root = tk.Tk()  # GUIのルートウィンドウ
        self.root.title("ファイルコピー")
        self._setup_gui()

    # GUIの設定
    def _setup_gui(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill="both", expand=True)

        # コピー元ファイルのリスト表示
        ttk.Label(frame, text="コピー元ファイル:").grid(row=0, column=0, sticky="w")
        self.file_list = tk.Listbox(frame, selectmode="extended", height=10, width=50)
        self.file_list.grid(row=1, column=0, columnspan=2, pady=5)
        ttk.Button(frame, text="ファイル選択", command=self._select_files).grid(row=1, column=2, padx=5)

        # コピー先フォルダの入力欄
        ttk.Label(frame, text="コピー先フォルダ:").grid(row=2, column=0, sticky="w", pady=(10, 0))
        self.destination_entry = ttk.Entry(frame, width=50)
        self.destination_entry.grid(row=3, column=0, columnspan=2, pady=5)
        ttk.Button(frame, text="フォルダ選択", command=self._select_folder).grid(row=3, column=2, padx=5)

        # 進捗バー
        ttk.Label(frame, text="進捗:").grid(row=4, column=0, sticky="w", pady=(10, 0))
        self.progress_bar = ttk.Progressbar(frame, length=400, mode="determinate")
        self.progress_bar.grid(row=5, column=0, columnspan=3, pady=5)

        # 実行ボタン
        ttk.Button(frame, text="コピー実行", command=self._execute_copy).grid(row=6, column=0, columnspan=3, pady=(10, 0))

        # ウィンドウサイズ調整
        self.root.geometry("600x400")
        self.root.resizable(False, False)

    # ファイル選択ダイアログ
    def _select_files(self):
        files = filedialog.askopenfilenames(title="コピーするファイルを選択してください")
        if files:
            self.file_list.delete(0, tk.END)  # 既存のリストを削除
            for file in files:
                self.file_list.insert(tk.END, file)  # 選択されたファイルをリストに追加
            self.copier.set_files(files)  # FileCopierにファイル設定

    # フォルダ選択ダイアログ
    def _select_folder(self):
        folder = filedialog.askdirectory(title="コピー先フォルダを選択してください")
        if folder:
            self.destination_entry.delete(0, tk.END)  # 現在の入力をクリア
            self.destination_entry.insert(0, folder)  # 選択されたフォルダを入力欄に表示
            self.copier.set_destination(folder)  # FileCopierにコピー先設定

    # コピー処理実行
    def _execute_copy(self):
        self.progress_bar["value"] = 0  # プログレスバーをリセット

        try:
            # 進捗更新用のコールバック
            def progress_callback(current, total, error=None):
                self.progress_bar["value"] = current
                self.progress_bar["maximum"] = total
                self.root.update_idletasks()  # GUIを更新
                if error:
                    messagebox.showerror("エラー", error)

            # コピー実行
            success, errors = self.copier.copy_files(progress_callback)
            if errors == 0:
                messagebox.showinfo("成功", f"{success} 件のファイルをコピーしました")
            else:
                messagebox.showwarning("完了", f"{success} 件をコピーしましたが、{errors} 件のエラーが発生しました")
        except ValueError as e:
            messagebox.showwarning("警告", str(e))  # コピー元やコピー先が未設定の場合
        except Exception as e:
            messagebox.showerror("エラー", f"予期しないエラーが発生しました: {e}")

    # アプリケーションを実行
    def run(self):
        self.root.mainloop()
