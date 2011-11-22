from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = (
        (0, 'minor'),
        (1, 'normal'),
        (2, 'major'),
        (3, 'critical'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES)
    deadline = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='tasks')

    class Meta:
        ordering = ['-priority', '-deadline']

    def __unicode__(self):
        return u"<%s:%s>" % (self.title, self.get_priority_display())

    @models.permalink
    def get_absolute_url(self):
        return ('todo:detail', str(self.id))
