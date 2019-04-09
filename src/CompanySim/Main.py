from src.TkinterTutorial.Window import Window
from Company import Company

companies = []

def AddCompany():
    print("AddCompany called")
    com = Company("Twats R Us")
    companies.append(com)

app = Window("GUI", "1280x720")
app.AddButton("Button", AddCompany, 50, 50)
app.mainloop()

print (len(companies))