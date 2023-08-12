from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            strain_name = form.cleaned_data["strain_name"]
            strain_THC = form.cleaned_data["strain_base"]
            strain_id = form.cleaned_data["strain_id"]
            grow_info = form.cleaned_data["grow_info"]
            flower_color = form.cleaned_data["flower_color"]
            flower_color2 = form.cleaned_data["flower_color2"]
            flower_texture = form.cleaned_data["flower_texture"]
            flower_density = form.cleaned_data["flower_density"]
            flower_flavor = form.cleaned_data["flower_flavor"]
            flower_flavor2 = form.cleaned_data["flower_flavor2"]
            flower_aroma = form.cleaned_data["flower_aroma"]
            flower_effect = form.cleaned_data["flower_effect"]
            flower_effect2 = form.cleaned_data["flower_effect2"]
            flower_effect3 = form.cleaned_data["flower_effect3"]
            user_rating = form.cleaned_data["user_rating"]
            user_notes = form.cleaned_data["user_notes"]

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, strain_name=strain_name,
                                strain_THC=strain_THC, strain_id=strain_id,
                                flower_color=flower_color, flower_color2=flower_color2,
                                flower_texture=flower_texture, flower_density=flower_density,
                                flower_flavor=flower_flavor, flower_flavor2=flower_flavor2,
                                flower_effect=flower_effect, grow_info=grow_info,
                                flower_effect2=flower_effect2, flower_effect3=flower_effect3,
                                user_rating=user_rating, user_notes=user_notes, flower_aroma=flower_aroma)

            message_body = f"A new review was submitted. Thank you, {first_name}!! We appreciate it!"
            email_message = EmailMessage("Form submission confirmation", message_body, to=[email])
            email_message.send()

            messages.success(request, "Form Submitted Successfully!")
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
