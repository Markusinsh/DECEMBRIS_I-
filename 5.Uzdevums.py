from datetime import datetime

# Iegūstu pašreizējo stundu
tagad = datetime.now()
stunda = tagad.hour

# Pārbaudām stundu un izvadam atbilstošu sveicienu
if stunda < 12:
    print("Labrīt!")
elif stunda < 18:
    print("Labdien!")
else:
    print("Labvakar!")
