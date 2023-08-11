from django.db import models


class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    strain_name = models.CharField(max_length=80)
    strain_base = models.CharField(max_length=80)
    strain_id = models.CharField(max_length=80)
    grow_info = models.CharField(max_length=500)
    flower_color = models.CharField(max_length=80)
    flower_color2 = models.CharField(max_length=80)
    flower_texture = models.CharField(max_length=80)
    flower_density = models.CharField(max_length=80)
    flower_flavor = models.CharField(max_length=80)
    flower_flavor2 = models.CharField(max_length=80)
    flower_aroma = models.CharField(max_length=80)
    flower_effect = models.CharField(max_length=80)
    flower_effect2 = models.CharField(max_length=80)
    flower_effect3 = models.CharField(max_length=80)
    user_rating = models.CharField(max_length=80)
    user_notes = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
