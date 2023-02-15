from datetime import datetime

today = datetime.now()

print(today)


d = today.strftime("%d/%m/%Y")
print("Date:", d)