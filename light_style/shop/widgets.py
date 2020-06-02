from django import forms


class DateTimeInput(forms.Widget):
    def __init__(self):
        #self.attrs['type'] = 'datetime'
        super().__init__(self)
