import tkinter as tk
from datetime import datetime


class EventTrackerApp:
    def __init__(self, root):
        self.root: tk.Tk = root
        self.root.title("Event Tracker")
        self.root.configure(bg="black")

        self.root.minsize(450, 350)

        label = tk.Label(
            self.root,
            text="Мои текущие задачи",
            fg="yellow",
            bg="black",
            font=("Helvetica", 16, "underline"),
        )
        label.pack()

        self.events = self._load_events()

        self._display_events()

    def _load_events(self) -> list:
        events = open("tasks.txt", "r", encoding="utf-8").readlines()
        parsed_events = []
        for event in events:
            parsed_event = event.split("|")
            parsed_event[-1] = parsed_event[-1].strip()
            parsed_events.append({
                "name": parsed_event[0],
                "date": datetime.now().strftime("%Y-%m-%d") if  parsed_event[-1] == "now" else parsed_event[-1]
            })
        return parsed_events

    def _display_events(self):
        for event in self.events:
            event_date = datetime.strptime(event["date"], "%Y-%m-%d")
            now = datetime.now()
            days_until = (now - event_date).days

            if days_until > 0:
                label_text = f"Прошло {days_until} дней от {event['name']}"
                font_style = ("Helvetica", 12)
                label = tk.Label(
                    self.root, text=label_text, bg="black", fg="red", font=font_style
                )
            elif days_until == 0:
                label_text = f"Прямо щаз происходит {event['name']}"
                font_style = ("Helvetica", 12)
                label = tk.Label(
                    self.root, text=label_text, bg="black", fg="orange", font=font_style
                )
            elif days_until < 0:
                label_text = f"Осталось {abs(days_until)} дней до {event['name']}"
                font_style = ("Helvetica", 12)
                label = tk.Label(
                    self.root, text=label_text, bg="black", fg="white", font=font_style
                )
            label.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = EventTrackerApp(root)
    root.mainloop()
