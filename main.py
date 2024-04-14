# Import necessary modules
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import datetime
import pyqrcode

# Define the app layout
class QRCodeGenerator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Set the orientation of the layout
        self.orientation = 'vertical'
        
        # Add app name label
        self.add_widget(Label(text='QR Code Generator', size_hint=(1, 0.1)))
        
        # Add input field for name
        self.name_input = TextInput(hint_text='Enter your name', size_hint=(1, 0.1))
        self.add_widget(self.name_input)
        
        # Add input field for roll number
        self.rollno_input = TextInput(hint_text='Enter your rollno', size_hint=(1, 0.1))
        self.add_widget(self.rollno_input)
        
        # Add button to generate details and QR code
        self.generate_button = Button(text='Generate Details and QR Code', size_hint=(1, 0.1))
        self.generate_button.bind(on_press=self.generate_details_and_qr)
        self.add_widget(self.generate_button)
        
        # Add label to display details
        self.details_label = Label(text='', size_hint=(1, 0.6))
        self.add_widget(self.details_label)
    
    # Function to generate details and QR code
    def generate_details_and_qr(self, instance):
        name = self.name_input.text
        rollno = self.rollno_input.text
        if name and rollno:
            current_datetime = datetime.datetime.now()
            # Formatting date and time
            date_formatted = current_datetime.strftime("%d-%m-%Y")
            time_formatted = current_datetime.strftime("%H:%M:%S")
            details = f"{name} {rollno} {date_formatted} {time_formatted}"
            self.details_label.text = details
            
            # Generate QR code
            qr_content = f"{name} {rollno} {date_formatted} {time_formatted}"
            qr = pyqrcode.create(qr_content)
            qr.svg("myyoutube.svg", scale=8)
            
            # Open the generated SVG file
            import os
            os.system("myyoutube.svg")
        else:
            self.details_label.text = 'Please enter name and roll number'

# Define the Kivy app
class QRCodeApp(App):
    def build(self):
        return QRCodeGenerator()

# Run the app
if __name__ == '__main__':
    QRCodeApp().run()
