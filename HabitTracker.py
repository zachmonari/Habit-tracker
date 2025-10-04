import json
import os

print("📝 Welcome to your Personal Habit Tracker!")

# ---------- Load habits if file exists ----------
if os.path.exists("habits.json"):
    with open("habits.json", "r") as f:
        habits = json.load(f)
else:
    habits = []
while True:
    habit = input("Enter a habit to track (or type 'done' when finished): ")
    if habit.lower() == 'done':
      break
    habits.append({'habit': habit, 'completed': 0})
for habit in habits:
   done = input(f"Did you complete '{habit['habit']}' today? (yes/no): ")
   if done.lower() == 'yes':
       habit['completed'] += 1
       print("Great job! Keep up the streak! 🔥")
   else:
       print("No worries! Tomorrow is another chance! 🌤️")

print("\n📅 Your Habit Progress:")
for habit in habits:
   print(f"{habit['habit']}: Completed {habit['completed']} times")

# Add your code here.
for habit in habits:
   if habit['completed'] % 7 == 0 and habit['completed'] != 0:
       print(f"🏆 Amazing! You've hit a weekly streak for {habit['habit']}!")
