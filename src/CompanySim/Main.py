from src.TkinterTutorial.Window import Window
from Company import Company

companies = []

def AddCompany(app):
    name = app.CreateEntryBox()
    com = Company(name)
    companies.append(com)

app = Window("GUI", "1280x720")
app.AddButton("Button", AddCompany(app), 50, 50)
app.mainloop()

for company in companies:
    print (company.name)

