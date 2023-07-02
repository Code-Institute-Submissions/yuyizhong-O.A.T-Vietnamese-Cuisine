from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Review(models.Model):
    RATING_CHOICES = (
        (0, '0 - Very Poor'),
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    )

    menu_item = models.ForeignKey('menu.MenuItem', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = CloudinaryField('image', default=None, blank=True, null=True)
    visit_date = models.DateField()

    def get_total_reviews(self):
        print('sfdsgdfdsgfesgfdg')
        # return self.rating.count()

    class Meta:
        """ Order by time of creation """
        ordering = ["-created_date"]

    def __str__(self):
        return f"Review for {self.menu_item.name} by {self.user.username}"
