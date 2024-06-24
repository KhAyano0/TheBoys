from django.db import models

# Create your models here.
class Character(models.Model):
    character_id = models.AutoField(primary_key=True)
    character_fullname = models.CharField(max_length=100, default='')
    character_nickname = models.CharField(max_length=100, default='')
    character_age = models.IntegerField(default=0)
    character_group = models.CharField(max_length=100, default='')
    character_description = models.CharField(max_length=255, default='')
    character_image = models.CharField(max_length=255,default='')

    def __str__(self):
        return f'Fullname: {self.character_fullname} | Nickname: {self.character_nickname} | Age: {self.character_age} | Group: {self.character_group} | Description: {self.character_description}'
    