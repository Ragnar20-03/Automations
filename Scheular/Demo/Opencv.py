import tk
import time
import schedule

# Function to create and display the popup window
def popup_window():
    popup = tk.Toplevel()
    popup.title("Popup Window")
    label = tk.Label(popup, text="It's time to do something!")
    label.pack()
    popup.geometry("300x100")

# Schedule the popup window to appear at a specific time (e.g., 15:30)
schedule.every(10).seconds.do(popup_window)

# Main loop to continuously check the schedule
while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for 1 second to avoid high CPU usage
