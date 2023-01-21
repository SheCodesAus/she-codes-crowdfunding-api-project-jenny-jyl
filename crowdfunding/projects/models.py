from django.db import models
from django.contrib.auth import get_user_model
# from location_field.models.plain import PlainLocationField

User = get_user_model()


class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    location=models.CharField(max_length=100)
    organization=models.CharField(max_length=200)
    website=models.URLField()
    goal=models.IntegerField()
    image=models.URLField()
    is_open=models.BooleanField()
    # is_favorite=models.ManyToManyField(User)
    date_created=models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='owner_projects'
    )
# on_delete = models.CASCADE means that if user is deleted, then all projects and info on user gets deleted

# class Favorite(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

class Pledge(models.Model):
    amount=models.IntegerField()
    comment=models.CharField(max_length=300)
    anonymous=models.BooleanField()
    project=models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    # will automatically create a project_id for the project
    supporter = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='supporter_pledges'
    )

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
