from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Friend (models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(validators=[\
            MinValueValidator(0),\
            MaxValueValidator(150)])
    birthday = models.DateField()
    
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ','+ \
        self.name + '(' + str(self.age) + ')>'

class Message(models.Model):
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str(self):
        return '<Message:id=' + str(self.id) + ', ' + \
                self.title + '(' + str(self.pub_date) + ')>'
        
    class Mate:
        ordering = ('pub_date',)
        


class place(models.Model):
    main_place = models.CharField(max_length=15)
    place1 = models.CharField(max_length=15, blank=True)
    place2 = models.CharField(max_length=15, blank=True)
    place3 = models.CharField(max_length=15, blank=True)
    place4 = models.CharField(max_length=15, blank=True)
    place5 = models.CharField(max_length=15, blank=True)
    place6 = models.CharField(max_length=15, blank=True)
    place7 = models.CharField(max_length=15, blank=True)
    place8 = models.CharField(max_length=15, blank=True)
    place9 = models.CharField(max_length=15, blank=True)
    place10 = models.CharField(max_length=15, blank=True)
    place11 = models.CharField(max_length=15, blank=True)
    place12 = models.CharField(max_length=15, blank=True)
    place13 = models.CharField(max_length=15, blank=True)
    place14 = models.CharField(max_length=15, blank=True)
    place15 = models.CharField(max_length=15, blank=True)   
    
    def __str__(self):
        return str(self.main_place)
    
    
class purpose(models.Model):
    main_purpose = models.CharField(max_length=15)
    purpose1 = models.CharField(max_length=15, blank=True)
    purpose2 = models.CharField(max_length=15, blank=True)
    purpose3 = models.CharField(max_length=15, blank=True)
    purpose4 = models.CharField(max_length=15, blank=True)
    purpose5 = models.CharField(max_length=15, blank=True)
    purpose6 = models.CharField(max_length=15, blank=True)
    purpose7 = models.CharField(max_length=15, blank=True)
    purpose8 = models.CharField(max_length=15, blank=True)
    purpose9 = models.CharField(max_length=15, blank=True)
    purpose10 = models.CharField(max_length=15, blank=True)
    purpose11 = models.CharField(max_length=15, blank=True)
    purpose12 = models.CharField(max_length=15, blank=True)
    purpose13 = models.CharField(max_length=15, blank=True)
    purpose14 = models.CharField(max_length=15, blank=True)
    purpose15 = models.CharField(max_length=15, blank=True)
    

    def __str__(self):
        return str(self.main_purpose)