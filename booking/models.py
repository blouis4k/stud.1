from django.db import models

class Booking(models.Model):
    studio_name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_block_booking = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.studio_name} booking on {self.date} from {self.start_time} to {self.end_time}"
