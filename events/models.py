from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length = 15)
    phone = models.CharField('Contact Phone', max_length=25)
    web = models.URLField()
    email_address = models.EmailField() 

    def __str__(self) -> str:
        return self.name

class ClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField("User Email")

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Event(models.Model):
    name = models.CharField(max_length=120)
    event_date = models.DateTimeField()
    venue = models.ForeignKey(Venue, blank=True, null=True,
                              on_delete=models.SET_NULL)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(ClubUser, blank=True)

    def __str__(self):
        return self.name
    
