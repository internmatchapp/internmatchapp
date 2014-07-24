from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models

def validate_future_date(value, pub_date):
    from django.utils import timezone
    if timezone.now() < value:
        return True
    else:
        raise ValidationError(u"%s comes before %s! Please pick a due date that is after the publication date" % (value, timezone.now())

class Applicant(models.Model):
    user = models.OneToOneField(User)

    email = models.EmailField(unique = True, db_index = True)

    def __unicode__(self):
        return self.email

class Business(models.Model):
    user = models.OneToOneField(User)

    email = models.EmailField(unique = True, db_index = True)

    def __unicode__(self):
        return self.email

class Attribute(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

class Posting(models.Model):
    DRAFT, PENDING, PUBLISHED = 'dr', 'pe', 'pb'
    POST_STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PENDING, 'Pending Review'),
        (PUBLISHED, 'Published'),
    )

    poster = models.ForeignKey(Business)
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(auto_now_add = True, verbose_name = 'date published')
    due_date = models.DateTimeField(verbose_name = 'due date', validators = [validate_future_date])
    post_status = models.CharField(max_length = 3, choices = POST_STATUS_CHOICES, default = DRAFT)
    slug = models.SlugField(unique = True)
    attributes = models.ManyToManyField(Attribute)
    body = models.TextField()

    def __unicode__(self):
        return self.title

    @property
    def pub_status(self):
        from django.utils import timezone
        if self.status = PUBLISHED:
            if self.pub_date > timezone.now():
                return 'Queued'
            else:
                return 'Public'
        else:
            return None

    class Meta:
        ordering = ['-pub_date']
