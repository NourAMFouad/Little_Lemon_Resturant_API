from django.forms import ModelForm 
from .models import Booking 
from .models import Menu

# BookingForm
class BookingForm(ModelForm):
    class Meta:
        model = Booking 
        fields = [
            "first_name",
            "last_name",
            "guest_number",
            "comments"
        ]
