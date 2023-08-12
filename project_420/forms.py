from django import forms


class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField()
    strain_name = (forms.CharField(max_length=80))
    strain_THC = (forms.CharField(max_length=80))
    strain_id = (forms.CharField(max_length=80))
    grow_info = (forms.CharField(max_length=500))
    flower_color = (forms.CharField(max_length=80))
    flower_color2 = (forms.CharField(max_length=80))
    flower_texture = (forms.CharField(max_length=80))
    flower_density = (forms.CharField(max_length=80))
    flower_flavor = (forms.CharField(max_length=80))
    flower_flavor2 = (forms.CharField(max_length=80))
    flower_aroma = (forms.CharField(max_length=80))
    flower_effect = (forms.CharField(max_length=80))
    flower_effect2 = (forms.CharField(max_length=80))
    flower_effect3 = (forms.CharField(max_length=80))
    user_rating = (forms.CharField(max_length=80))
    user_notes = (forms.CharField(max_length=500))
