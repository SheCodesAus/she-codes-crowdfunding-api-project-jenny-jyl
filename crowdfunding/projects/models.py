from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    goal=models.IntegerField()
    image=models.URLField()
    is_open=models.BooleanField()
    date_created=models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=200)
        # will need to change this to ForeignKey after we created a user (from CharField)

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
    supporter = models.CharField(max_length=200)
