from django import forms


class ContactForm(forms.Form):
    contact_First_name = forms.CharField(required=True)
    contact_Last_Name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_Industry = forms.CharField(required=True)
    contact_Company = forms.CharField(required=True)
    Sujet = forms.CharField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
    )


def __init__(self, *args, **kwargs):
    super(ContactForm, self).__init__(*args, **kwargs)
    self.fields['contact_First_name'].label = "Your  First name:"
    self.fields['contact_Last_name'].label = "Your  Last name:"
    self.fields['contact_Industry'].label = "Your email:"
    self.fields['contact_Company'].label = "Your email:"
    self.fields['Sujet'].label = "Your email:"
    self.fields['content'].label = 'What do you want to say?'
