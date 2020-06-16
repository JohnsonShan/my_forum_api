from django.db import models
# Create your models here.


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    owner = models.ForeignKey(
        'auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
    def __str__(self):
        return '%d: %s' % (self.id, self.title)

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)
    owner = models.ForeignKey(
        'auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    class Meta:
        ordering = ['created']

    def __str__(self):
        return '%s: %s' % (self.owner, self.content)

def save(self, *args, **kwargs):
    options = {'title': self.title} if self.title else {}
    super(Post, self).save(*args, **kwargs)
