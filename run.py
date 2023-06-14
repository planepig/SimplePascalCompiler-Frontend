import os
import subprocess
from tkinter import Tk, Text, Button, filedialog, Label, Scrollbar, END, Frame


class App:
    def __init__(self, root):
        self.root = root
        self.textbox = Text(root, height=30, width=100)
        self.textbox.pack()

        self.save_button = Button(root, text="保存并执行", command=self.save_and_execute)
        self.save_button.pack()

        self.open_button = Button(root, text="打开并执行", command=self.open_and_execute)
        self.open_button.pack()

        self.scrollbar = Scrollbar(root, orient='horizontal')
        self.scrollbar.pack(side="bottom", fill="x")

        self.output_frame = Frame(root)
        self.output_frame.pack(fill="both", expand=True)
        self.output_subframes = [Frame(self.output_frame) for _ in range(4)]
        self.output_windows = [Text(frame, height=15, width=25, xscrollcommand=self.scrollbar.set) for frame in
                               self.output_subframes]
        self.output_labels = [Label(frame, text=label_text) for frame, label_text in
                              zip(self.output_subframes, ["Lexical Analysis:", "Parse Processing:", "Quats:", "Syms:"])]

        for frame, label, window in zip(self.output_subframes, self.output_labels, self.output_windows):
            label.pack(side="top")
            window.pack(side="bottom", fill="both", expand=True)
            frame.pack(side="left", fill="both", expand=True)

        self.scrollbar.config(command=self.xview_all_windows)

    def save_and_execute(self):
        # 保存文本框内容到txt文件
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(self.textbox.get("1.0", END))

        # 找到文件路径
        file_path = os.path.abspath("output.txt")

        # 执行程序
        self.execute_program(file_path)


    def open_and_execute(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not file_path:
            return

        file_name = file_path.split('/')[-1]

        # 将文件内容写入到textbox
        with open(file_path, "r", encoding="utf-8") as file:
            self.textbox.delete("1.0", END)
            self.textbox.insert(END, file.read())

        self.execute_program(file_path)

    def execute_program(self, file_path):
        # 刷新四个显示窗口
        for window in self.output_windows:
            window.delete("1.0", END)

        # 找到名叫build的文件夹路径
        project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "build"))
        os.chdir(project_dir)

        # 创建可执行程序进程
        process = subprocess.Popen(['compiler.exe'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

        # 输入
        input_data = file_path + '\n'
        process.stdin.write(input_data.encode('utf-8'))
        process.stdin.flush()

        # 获取输出
        output, errors = process.communicate()
        output_parts = output.decode('utf-8').split("--------")

        # 在窗口中显示结果
        for output_window, output_part in zip(self.output_windows, output_parts):
            output_window.insert(END, output_part + '\n')

        # 在最后一个窗口中显示错误
        self.output_windows[-1].insert(END, errors.decode('utf-8') + '\n')

        # 滚动到最后一行
        self.xview_all_windows("moveto", 1)

    def xview_all_windows(self, *args):
        for window in self.output_windows:
            window.xview(*args)


root = Tk()
root.title("compiler")
app = App(root)
root.mainloop()
