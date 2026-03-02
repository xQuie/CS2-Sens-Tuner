import tkinter as tk
from tkinter import messagebox

class SensTuner:
    def __init__(self, root):
        self.root = root
        self.root.title("CS2 Sens Tuner")
        self.root.geometry("400x450")
        
        self.low = 0.0
        self.high = 0.0
        self.current = 0.0
        
        tk.Label(root, text="Мінімальна сенса (фліки):").pack(pady=5)
        self.ent_low = tk.Entry(root)
        self.ent_low.pack()
        
        tk.Label(root, text="Максимальна сенса (180°):").pack(pady=5)
        self.ent_high = tk.Entry(root)
        self.ent_high.pack()
        
        self.btn_start = tk.Button(root, text="ПОЧАТИ ТЕСТ", command=self.start_test, bg="lightgray")
        self.btn_start.pack(pady=10)
        
        self.lbl_current = tk.Label(root, text="Поточна сенса: ---", font=("Arial", 14, "bold"))
        self.lbl_current.pack(pady=20)
        
        self.btn_high = tk.Button(root, text="ЗАШВИДКА (Висока)", width=20, command=self.process_high, state="disabled", fg="red")
        self.btn_high.pack(pady=2)
        
        self.btn_low = tk.Button(root, text="ЗАПОВІЛЬНА (Низька)", width=20, command=self.process_low, state="disabled", fg="blue")
        self.btn_low.pack(pady=2)
        
        self.btn_done = tk.Button(root, text="ІДЕАЛЬНО (Зберегти)", width=20, command=self.finish, state="disabled", bg="green", fg="white")
        self.btn_done.pack(pady=10)

    def log_step(self, action):
        with open("sens_log.txt", "a", encoding="utf-8") as f:
            f.write(f"Дія: {action} | Сенса: {self.current:.3f} | Межі: [{self.low:.3f} - {self.high:.3f}]\n")

    def start_test(self):
        try:
            self.low = float(self.ent_low.get())
            self.high = float(self.ent_high.get())
            self.update_sens()
            self.btn_high["state"] = "normal"
            self.btn_low["state"] = "normal"
            self.btn_done["state"] = "normal"
            with open("sens_log.txt", "w", encoding="utf-8") as f:
                f.write("--- Нова сесія калібрування ---\n")
        except ValueError:
            messagebox.showerror("Помилка", "Введіть числові значення")

    def update_sens(self):
        self.current = (self.low + self.high) / 2
        self.lbl_current.config(text=f"Сенса: {self.current:.3f}")

    def process_high(self):
        self.log_step("Зависока")
        self.high = self.current
        self.current = (self.low * 2 + self.high) / 3
        self.lbl_current.config(text=f"Сенса: {self.current:.3f}")

    def process_low(self):
        self.log_step("Занизька")
        self.low = self.current
        self.current = (self.low + self.high * 2) / 3
        self.lbl_current.config(text=f"Сенса: {self.current:.3f}")

    def finish(self):
        self.log_step("ФІНАЛ")
        messagebox.showinfo("Результат", f"Твоя сенса: {self.current:.3f}\nДані збережені в sens_log.txt")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = SensTuner(root)
    root.mainloop()
    