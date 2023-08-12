import pywhatkit as kit
import datetime

# List of recipients' phone numbers (with country code, without '+' sign)
recipients = ["1234567890", "0987654321"]  # Add recipient phone numbers here

# Message to send
message = "Hello from Python!"

# Get current time
now = datetime.datetime.now()
hours = now.hour
minutes = now.minute + 1  # Send the message 1 minute from now

# Loop through recipients and send messages
for recipient in recipients:
    kit.sendwhatmsg(f"+{recipient}", message, hours, minutes)
    print(f"Message sent to {recipient}")

print("All messages sent!")
