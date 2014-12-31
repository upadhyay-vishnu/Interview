from django.db import models

# Create your models here.


class Bookmark(models.Model):
    bookmark = models.URLField(unique=True, db_column='URL', default='')

    def __unicode__(self):
        return '%s' % unicode(self.bookmark)


class Tags(models.Model):
    bookmark = models.ManyToManyField(Bookmark, db_table='URL_Tag',
                                      symmetrical=False, related_name='url_tag')
    tag = models.CharField(unique=True, max_length=50, db_column='Tag', default='')

    def __unicode__(self):
        return '%s' % unicode(self.tag)
