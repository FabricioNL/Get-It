from django.db import models


class Note(models.Model):


    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField(default='')

    def __str__(self):
        return '{0}. {1}'.format(self.id, self.title)
    