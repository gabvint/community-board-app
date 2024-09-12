from django.db import models
from enum import Enum
# Create your models here.

class Category(Enum):
    EVENTS = "Events"
    ANNOUNCEMENTS = "Announcements"
    HOUSING = "Housing"
    EDUCATION = "Education"
    VOLUNTEERING = "Volunteering"
    RECOMMENDATIONS = "Recommendations"
    GENERAL_DISCUSSION = "General Discussion"
    HELP_SUPPORT = "Help & Support"
    HEALTH_WELLNESS = "Health & Wellness"
    POLITICS_LOCAL_ISSUES = "Politics & Local Issues"
    TECHNOLOGY = "Technology"
    PARENTING_FAMILY = "Parenting & Family"
    PETS = "Pets"
    LOST_FOUND = "Lost & Found"
    FOR_SALE = "For Sale"
    


class Board(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50, 
        choices=[(key.name, key.value) for key in Category],
        default=Category.GENERAL_DISCUSSION.value
    )
    description = models.TextField(max_length=250)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title