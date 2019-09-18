from django.db import models


Rating_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
)


class Feedback(models.Model):
    customer_name = models.CharField(max_length=120, default=None, blank=True, null=True)
    agency_name = models.CharField(max_length=120, default=None, blank=True, null=True)
    customer_email = models.EmailField(max_length=255, default=None, blank=True, null=True)
    review = models.TextField(default=None, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    is_favorite = models.IntegerField(choices=Rating_CHOICES, default=1, blank=True, null=True)
    behaviour = models.IntegerField(choices=Rating_CHOICES, default=1, blank=True, null=True)
    professionalism = models.IntegerField(choices=Rating_CHOICES, default=1, blank=True, null=True)
    price_fairness = models.IntegerField(choices=Rating_CHOICES, default=1, blank=True, null=True)
    overall = models.IntegerField(choices=Rating_CHOICES, default=1, blank=True, null=True)
    Average = models.IntegerField(choices=Rating_CHOICES, default=1, blank=True, null=True)

    # def __str__(self):
    #    return self.customer_name

