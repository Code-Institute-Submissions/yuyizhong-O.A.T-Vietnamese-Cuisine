from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from math import floor


class Review(models.Model):
    """
    Model to create reviews on particular menu dish
    """
    # Rating choice fields
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

    class Meta:
        """ Order by time of creation """
        ordering = ["-created_date"]

    def __str__(self):
        return f"Review for {self.menu_item.name} by {self.user.username}"

    @classmethod
    def average_rating(cls, menu_item):
        """
        Function to caculate the average rating to a specific menu
        """
        reviews = cls.objects.filter(menu_item=menu_item)
        if reviews.exists():
            total_rating = sum(review.rating for review in reviews)
            return total_rating / reviews.count()
        else:
            return 0

    @classmethod
    def full_stars(cls, menu_item):
        """
        Function to display the number of full stars
        """
        average_rating = cls.average_rating(menu_item)
        return floor(average_rating)

    @classmethod
    def half_stars(cls, menu_item):
        """ Determine if a half star should be displayed
        based on the average rating of a menu item.

        Parameters:
            menu_item (MenuItem): The menu item to check.

        Returns:
            bool: True if a half star should be displayed, False otherwise.
        """
        average_rating = cls.average_rating(menu_item)
        full_stars = cls.full_stars(menu_item)
        decimal_part = average_rating - full_stars
        return decimal_part > 0.4
