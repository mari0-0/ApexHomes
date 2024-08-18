from django import forms

class HotelRoomSearchForm(forms.Form):
    state_choices = [
        ('', 'Any'),  # Empty choice for "Any" location
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CG', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Orissa'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TR', 'Tripura'),
        ('UK', 'Uttarakhand'),
        ('UP', 'Uttar Pradesh'),
        ('WB', 'West Bengal'),
        ('TN', 'Tamil Nadu'),
        ('TR', 'Tripura'),
        ('AN', 'Andaman and Nicobar Islands'),
        ('CH', 'Chandigarh'),
        ('DH', 'Dadra and Nagar Haveli'),
        ('DD', 'Daman and Diu'),
        ('DL', 'Delhi'),
        ('LD', 'Lakshadweep'),
        ('PY', 'Pondicherry'),
    ]
    ROOM_TYPE_CHOICES = [
        ('', 'Any'),  # Empty choice for "Any" room type
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
        # Add more room type choices as needed
    ]
    city = forms.CharField(required=False)
    state = forms.ChoiceField(choices=state_choices, required=False)
    price_min = forms.DecimalField(required=False, min_value=0, label='Minimum Price')
    price_max = forms.DecimalField(required=False, min_value=0, label='Maximum Price')
