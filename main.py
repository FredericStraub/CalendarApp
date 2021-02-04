from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.theming import ThemeManager
from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.picker import MDDatePicker, MDThemePicker, MDTimePicker

from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
import datetime
from kivymd.uix.label import MDLabel
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
class Inputtext(FloatLayout):
    pass
class Content(BoxLayout):
    pass
class MainApp(MDApp):

#define builder 
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.meetingname = ""
        self.dates = {}
        self.temp_date_storage = None
        self.popup = None
#sets meeting name and picks time
    def set_meeting_name(self):
        self.meetingname = self.popup.content.ids.input.text
        self.popup.dismiss()
        self.show_timepicker()
#pick date 
    def show_datepicker(self):
        picker = MDDatePicker(callback = self.got_date)
        picker.open()
        
#saves date in dict (database still in progress) and opens popup  for description 
    def got_date(self, the_date):
        print(the_date)
        if the_date in self.dates.keys():
            pass
        else:
            self.dates[the_date] = 0
        self.temp_date_storage = the_date
        self.popup = Popup(title="Name of Meeting",content=Inputtext(), size_hint=(None,None),size=(300, 300))
        self.popup.open()
        
#sets time
    def show_timepicker(self):
        picker = MDTimePicker()
        picker.bind(time = self.got_time)
        picker.open()
#saves time in dict (database still in progress)
    def got_time(self, picker_widget,the_time):
        print(the_time)
    
        p=Inputtext()
        if self.dates.get(self.temp_date_storage) == 0:
            self.dates[self.temp_date_storage] = [the_time]
        else:
            self.dates.get(self.temp_date_storage).append(the_time)

        dropdown = Content()
        dropdown.ids.drawout.text = self.popup.content.ids.input2.text

        self.root.ids.box.add_widget(MDExpansionPanel(
                        
                    content=dropdown,
                    panel_cls=MDExpansionPanelThreeLine(
                        text=self.meetingname,
                        secondary_text=str(the_time),
                        tertiary_text=str(self.temp_date_storage)
                    )))
        self.temp_date_storage = None
        
        
       
#define themepicker
    def show_themepicker(self):
        picker = MDThemePicker()
        picker.open()
#define bar of current weekdays (will be connected later accrodingly with the dates)      
    def show_getday(self,dayint):
        l = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        x = datetime.datetime.today().weekday() + dayint
        if x >= 7:
            x -= 7
        return l[x]

MainApp().run()

