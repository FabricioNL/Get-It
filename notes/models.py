from django.db import models

   
class Tag(models.Model):
    tag = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return '{0}'.format(self.tag)


class Note(models.Model):


    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField(default='')
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{0}. {1}'.format(self.id, self.title)
