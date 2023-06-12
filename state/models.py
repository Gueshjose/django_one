from django.db import models
from django.core.validators import MaxLengthValidator, MaxValueValidator,MinLengthValidator,MinValueValidator,FileExtensionValidator

# Create your models here.
class State(models.Model):
    name= models.CharField(max_length=50, validators=[MinLengthValidator(3),MaxLengthValidator(50)], default="First")
    population=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(999999)],default=1)
        
    def __str__(self):
        return str(self.name)

class President(models.Model):
    class Geender(models.TextChoices):
        Homme = "H",
        Femme = "F"
    nom= models.CharField(max_length=50,validators=[MinLengthValidator(3),MaxLengthValidator(50)])
    age=models.IntegerField(validators=[MinValueValidator(18),MaxValueValidator(99)])
    genre=models.CharField(choices=Geender.choices,max_length=5)
    image=models.ImageField(upload_to='img/', default='img/avatar-default.png',validators=[FileExtensionValidator(["JPEG","JPG","PNG","WEBP"])])
    pays=models.OneToOneField(State,on_delete=models.PROTECT,primary_key=True)

    def __str__(self):
        return str(self.name)


