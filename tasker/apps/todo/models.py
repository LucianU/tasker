from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = (
        (0, 'minor'),
        (1, 'normal'),
        (2, 'major'),
        (3, 'critical'),
    )

    title = models.CharField(max_length=255)
    content = models.TextField()
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES)
    deadline = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        return u"<%s:%s>" % (self.title, self.get_priority_display())

    @models.permalink
    def get_absolute_url(self):
        return ('todo:detail', str(self.id))
