import datetime
import json
import tkinter as tk
from tkinter import messagebox, simpledialog

class DreamApp:
    def __init__(self, master):
        self.master = master
        self.master.title("夢が叶うアプリ")
        self.goals = []
        self.schedule = []
        self.load_data()

        # GUI要素
        self.goal_listbox = tk.Listbox(master, width=50)
        self.goal_listbox.pack(pady=10)

        self.add_goal_button = tk.Button(master, text="目標を追加", command=self.add_goal_gui)
        self.add_goal_button.pack()

        self.add_schedule_button = tk.Button(master, text="予定を追加", command=self.add_schedule_gui)
        self.add_schedule_button.pack()

        self.suggest_actions_button = tk.Button(master, text="アクションを提案", command=self.suggest_actions_gui)
        self.suggest_actions_button.pack()

        self.update_goal_list()

    def add_goal_gui(self):
        goal = simpledialog.askstring("目標追加", "新しい目標を入力してください：")
        if goal:
            self.goals.append({"goal": goal, "sub_goals": []})
            self.break_down_goal(len(self.goals) - 1)
            self.save_data()
            self.update_goal_list()

    def break_down_goal(self, goal_index, level=0):
        if level > 2:  # 最大3レベルまでブレイクダウン
            return
        
        goal = self.goals[goal_index]["goal"]
        sub_goals = simpledialog.askstring("目標のブレイクダウン", 
                                           f"{'  ' * level}目標: {goal}\n"
                                           f"{'  ' * level}この目標をブレイクダウンしてください（カンマ区切り、もしくはキャンセルでスキップ）:")
        
        if sub_goals:
            for sub_goal in sub_goals.split(','):
                self.goals[goal_index]["sub_goals"].append({"goal": sub_goal.strip(), "sub_goals": []})
                self.break_down_goal(goal_index, level + 1)
        
        self.save_data()

    def add_schedule_gui(self):
        event = simpledialog.askstring("予定追加", "新しい予定を入力してください：")
        if event:
            date = datetime.date.today()  # 簡略化のため、今日の日付を使用
            self.schedule.append({"date": date.isoformat(), "event": event})
            self.save_data()
            messagebox.showinfo("予定追加", "予定が追加されました。")

    def suggest_actions_gui(self):
        today = datetime.date.today()
        suggestions = []
        for event in self.schedule:
            if datetime.date.fromisoformat(event["date"]) == today:
                suggestions.append(f"今日の予定: {event['event']}")
                for goal in self.goals:
                    if goal["goal"].lower() in event["event"].lower():
                        suggestions.append(f"- {goal['goal']}に関連する作業を進めましょう。")
        
        if suggestions:
            messagebox.showinfo("アクション提案", "\n".join(suggestions))
        else:
            messagebox.showinfo("アクション提案", "今日の予定に関連するアクションはありません。")

    def update_goal_list(self):
        self.goal_listbox.delete(0, tk.END)
        for goal in self.goals:
            self.goal_listbox.insert(tk.END, goal["goal"])

    def save_data(self):
        data = {
            "goals": self.goals,
            "schedule": self.schedule
        }
        with open("dream_app_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_data(self):
        try:
            with open("dream_app_data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.goals = data["goals"]
                self.schedule = data["schedule"]
        except FileNotFoundError:
            print("データファイルが見つかりません。新しいデータファイルを作成します。")

if __name__ == "__main__":
    root = tk.Tk()
    app = DreamApp(root)
    root.mainloop()