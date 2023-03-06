from django.db import models

# Create your models here.
NEWSLETTER_OPTION  = [
    ('D', "Daily"),
    ('W', "Weekly"),
    ('M', "Monthly"),
    ('Y', "Yearly"),
]

class Register(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    update_f_name = models.CharField(max_length=200)
    update_l_name = models.CharField(max_length=200)
    option = models.CharField(max_length=2, choices=NEWSLETTER_OPTION, default="D")
