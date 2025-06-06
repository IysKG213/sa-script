import os
import shutil

## ファイルコピーのロジックを担当するクラス"""
class FileCopier:
    def __init__(self):
        self.files = []  # コピー元ファイルのリスト
        self.destination = ""  # コピー先のフォルダパス

    # コピー元ファイルを設定
    def set_files(self, files):
        self.files = files

    # コピー先フォルダを設定
    def set_destination(self, destination):
        self.destination = destination

    # ファイルをコピーし、進捗をコールバックで通知
    def copy_files(self, progress_callback=None):
        if not self.files or not self.destination:
            raise ValueError("コピー元ファイルまたはコピー先フォルダが指定されていません")

        if not os.path.exists(self.destination):
            os.makedirs(self.destination)

        total_files = len(self.files)
        errors = 0

        # ファイルコピー処理
        for i, file in enumerate(self.files, start=1):
            try:
                if os.path.isfile(file):
                    shutil.copy(file, os.path.join(self.destination, os.path.basename(file)))
            except Exception as e:
                errors += 1
                if progress_callback:
                    progress_callback(i, total_files, error=f"エラー: {file}")
            finally:
                if progress_callback:
                    progress_callback(i, total_files)

        return total_files - errors, errors
