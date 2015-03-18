from django.db import models

# Create your models here.

#Team Model
class Team(models.Model):
	name = models.CharField(unique=True, max_length=50)

	class Meta(object):
		verbose_name_plural = "Teams"
		ordering = ('name',)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.name = self.name.upper()
		super(Team, self).save(*args, **kwargs)

#Players Model
class Players(models.Model):
	name = models.CharField(unique=False, max_length=50)
	number = models.CharField(unique=True, max_length=2, null=True)
	position = models.CharField (unique=True, max_length=50)
	hometown = models.CharField (unique=True, max_length=50)
	grade = models.CharField (unique=True, max_length=50, null=True)

	class Meta(object):
		ordering = ('number', 'name')

		def __unicode__(self):
			return u'%s %s' %(self.name, self.number)