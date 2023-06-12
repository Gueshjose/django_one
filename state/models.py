from django.db import models
from django.core.validators import MaxLengthValidator, MaxValueValidator,MinLengthValidator,MinValueValidator

# Create your models here.
class State(models.Model):
    

    def __str__(self):
        name= models.CharField(max_length=50)
        population=models.IntegerField(validators=[MinValueValidator(1000),MaxValueValidator(999999999)])
        
        def __str__(self):
            return str(self.name)

class President(models.Model):
    class Geender(models.TextChoices):
        Homme = "H",
        Femme = "F"
    nom= models.CharField(max_length=50)
    age=models.IntegerField(validators=[MinValueValidator(18),MaxValueValidator(99)])
    genre=models.CharField(choices=Geender.choices,max_length=5)
    image=models.ImageField(upload_to='img/', default='img/avatar-default.png')
    pays=models.OneToOneField(State,on_delete=models.PROTECT,primary_key=True)

    def __str__(self):
        return str(self.name)


