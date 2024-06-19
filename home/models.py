from django.db import models
from datetime import datetime

# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    # password = models.CharField(max_length = 25, widget=models.PasswordInput)
    phone = models.CharField(max_length = 12)
    desc = models.TextField()
    date = models.DateField()

    # This function is used to change the stored title in the server
    def __str__(self):
        return self.name

class Test(models.Model):
    name = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122 , default='John Doe')
    phone = models.CharField(max_length = 12 , default='johnDoe29@gmail.com')
    test1 = models.CharField(max_length = 122 , default='John Doe' , choices=[('Red', 1), ('Blue', 2), ('Green', 3), ('Black', 4)])
    test2 = models.CharField(max_length = 122 , default='John Doe' , choices=[('Red', 1), ('Blue', 2), ('Green', 3), ('Black', 4)])
    test3 = models.CharField(max_length = 122 , default='John Doe' , choices=[('Red', 1), ('Blue', 1), ('Green', 2), ('Black', 4)])
    test4 = models.CharField(max_length = 122 , default='John Doe' , choices=[('Red', 1), ('Blue', 2), ('Green', 3), ('Black', 4)])
    test5 = models.CharField(max_length = 122 , default='John Doe' , choices=[('Red', 0), ('Blue', 1)])
    test6 = models.CharField(max_length = 122 , default='John Doe' , choices=[('Red', 0), ('Blue', 1)])
    test7 = models.CharField(max_length = 122 , default='John Doe' , choices=[('Red', 0), ('Blue', 1)])
    test8 = models.CharField(max_length = 122 , default='John Doe' , choices=[('Red', 0), ('Blue', 1)])
    test9 = models.CharField(max_length = 122 , default='John Doe' , choices=[('Red', 0), ('Blue', 1)])
    test10 = models.CharField(max_length = 122 , default='John Doe' , choices=[('Red', 0), ('Blue', 1)])
    test11 = models.CharField(max_length = 122 , default='John Doe' , choices=[('Red', 0), ('Blue', 1)])
    test12 = models.CharField(max_length = 122 , default='John Doe' , choices=[('Red', 0), ('Blue', 1)])
    test13 = models.CharField(max_length = 122 , default='John Doe' , choices=[('Red', 0), ('Blue', 1)])
    test14 = models.CharField(max_length = 122 , default='John Doe' , choices=[('Red', 0), ('Blue', 1)])
    test15 = models.CharField(max_length = 255 , default='John Doe' , choices=[('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9)])
    test16 = models.CharField(max_length = 255 , default='John Doe' , choices=[('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8)])
    test17 = models.CharField(max_length = 255 , default='John Doe' , choices=[('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8)])
    date = models.DateField(("Date"), default=datetime.now())

    # This function is used to change the stored title in the server
    def __str__(self):
        return self.name