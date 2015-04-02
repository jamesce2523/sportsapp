from django.db import models

# Create your models here.

#Team Model
class Team(models.Model):
	name = models.CharField(max_length=50)
	gender = models.CharField(max_length=1)

	class Meta(object):
		verbose_name_plural = "Teams"
		ordering = ('name',)

	def __unicode__(self):
		return self.name

#Players Model
class Player(models.Model):
	name = models.CharField(max_length=50)
	number = models.IntegerField()
	position = models.CharField (max_length=50)
	hometown = models.CharField (max_length=50)
	grade = models.CharField (max_length=50)
	avatar = models.CharField (max_length=255, default="")

	team = models.ForeignKey('Team', related_name='players')

	class Meta(object):
		ordering = ('number', 'name')

		def __unicode__(self):
			return u'%s %s' %(self.name, self.number)

