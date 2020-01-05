import  requests,json
from tkinter import *
from tkinter import  messagebox
class Weather:
    def __init__(self,root):
        self.root = root
        self.root.title('Weather App')
        self.root.geometry('600x500')
        self.root.config(bg = 'white')
        self.root.resizable(0,0)
        self.api_key = '9524bb51cf5f8675427d00260d806fbb'
        self.city = StringVar()
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def userText(self,event):
        self.e1.delete(0,END)

    def clear(self):
        self.e1.delete(0, END)
        self.temp_entry.delete(0, END)
        self.pressure_entry.delete(0, END)
        self.humidity_entry.delete(0, END)
        self.description_entry.delete(0, END)

        self.e1.focus_set()

    def city_input(self):

        frame1 = Frame(self.root , height = 80 , width = 600 , bd = 1 , relief = GROOVE,bg = 'white' ).pack()
        label1 = Label(frame1,text = 'Weather Forecast',font = ('Helvetica',25,'bold'),bg = 'white').place(x = 5 , y = 18)

        frame2 = Frame(self.root , height = 85 , width = 600 , bd = 1 , relief = GROOVE,bg = '#ee8841' ).place(x = 0 , y = 81)
        self.e1 = Entry(frame2,textvariable = self.city , font = ('New Courier',13,'bold'),bd = 5 , relief = GROOVE,width = 25 )
        self.e1.place(x = 95 , y = 107)

        self.e1.insert(0, "Your City Name")
        self.e1.bind("<Button>",self.userText)

        btn1 = Button(self.root , text = '? Search' , font = ('New Times Roman',11,'bold')
                     ,bg = 'crimson',fg = 'white',command = lambda :self.get_input())
        btn1.place(x = 350 , y = 107)

        frame3 = Frame(self.root , height = 335,width = 600 , bd = 1 , relief = GROOVE ,bg = 'light green' ).place(x = 0, y = 166)

        temp = Label(frame3, text = 'Temperature', fg = 'black',bg = 'light green',font = ('Times New Roman',17,'bold')).place(x = 10,y = 190)
        pressure = Label(frame3, text = 'Pressure', fg = 'black',bg = 'light green',font = ('Times New Roman',17,'bold')).place(x = 10,y = 240)
        humidity = Label(frame3, text = 'Humidity', fg = 'black',bg = 'light green',font = ('Times New Roman',17,'bold')).place(x = 10,y = 290)
        description = Label(frame3, text = 'Description', fg = 'black',bg = 'light green',font = ('Times New Roman',17,'bold')).place(x = 10,y = 340)
        self.temp_entry = Entry(frame3,width = 30,font = ('Courier New' , 13 , 'bold')).place(x = 180, y = 193)
        self.pressure_entry = Entry(frame3,width = 30,font = ('Courier New' , 13 , 'bold')).place(x = 180, y = 243)
        self.humidity_entry = Entry(frame3,width = 30,font = ('Courier New' , 13 , 'bold')).place(x = 180, y = 293)
        self.description_entry = Entry(frame3,width = 30,font = ('Courier New' , 13 , 'bold')).place(x = 180, y = 343)

        btn1 = Button(self.root , text = '    Clear    ' , font = ('New Times Roman',11,'bold')
                     ,bg = 'crimson',fg = 'white',command = lambda :self.clear())
        btn1.place(x = 220 , y = 400)

    def get_input(self):

        #frame2 = Frame(self.root ,height = 40 , width = 600 ,bd = 1 , relief = GROOVE , bg = 'white').place(x = 0,y=150)
       # label2 = Label(frame2 , text = 'Weather of your city ',font = ('Times New Roman',18,'underline') , fg = 'red',bg = 'white').place(x = 195, y = 153)
        name = self.city.get()
        complete_url = self.base_url + 'appid =' + self.api_key + '&q = ' +name

        response = requests.get(complete_url)

        x = response.json()

        if x["cod"] != "404":
            y = x['main']
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            self.temp_entry.insert(190, str(current_temperature) + " Kelvin")
            self.pressure_entry.insert(190, str(current_pressure) + " hPa")
            self.humidity_entry.insert(190, str(current_humidiy) + " %")
            self.description_entry.insert(190, str(weather_description))
        else:
            messagebox.showerror("Error", "City Not Found \n"
                                          "Please enter valid city name")
            self.e1.delete(0, END)

root = Tk ()
obj = Weather(root)
obj.city_input()
root.mainloop()