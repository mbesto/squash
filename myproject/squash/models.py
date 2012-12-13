from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class MySiteProfile(models.Model):
	userid = models.ForeignKey(User, unique=True)
	status = models.CharField(max_length=60)
	nation = models.CharField(max_length=2)
	def __unicode__(self):
		return "%s %s" % (self.status, self.nation)
		
class Court(models.Model):
	location_name = models.CharField(max_length=100)
	number = models.IntegerField()
	def __unicode__(self):
		return "%s %s %s" % (self.id, self.location_name, self.number)

class Attend(models.Model):
	date = models.DateField()
	time = models.TimeField()
	userid = models.ForeignKey(User)
	def __unicode__(self):
		return "%s" % (self.id)
        
class Match(models.Model):
	date = models.DateTimeField()
	court = models.ForeignKey(Court)
	players = models.ManyToManyField(User, through='Participant')
	def __unicode__(self):
		return "%s %s" % (self.id, self.date)

class Participant(models.Model):
	match = models.ForeignKey(Match)
	userid = models.ForeignKey(User)
	games_won = models.IntegerField()
	def __unicode__(self):
		return "%s %s %s" % (self.id, self.games_won, self.userid)

class AttendForm(ModelForm):
	class Meta:
		model = Attend
		fields = ('date', 'time', 'userid')

class MatchForm(ModelForm):
	class Meta:
		model = Match
		
class ParticipantForm(ModelForm):
	class Meta:
		model = Participant
		
		
#Update 2
class LocationTwo(models.Model):
    name = models.CharField(max_length=60)

class CourtTwo(models.Model):
    location = models.ForeignKey(LocationTwo)
    number = models.PositiveIntegerField()
    
class MatchTwo(models.Model):
    player_1 = models.ForeignKey(User, related_name='player_1')
    score_1 = models.PositiveIntegerField(null=True, blank=True)
    player_2 = models.ForeignKey(User, related_name='player_2')
    score_2 = models.PositiveIntegerField(null=True, blank=True)
    court = models.ForeignKey(CourtTwo)
    date = models.DateField()
    time = models.TimeField()

    @property
    def winner(self):
        "None means not played yet, or a draw."
        if self.score_1 > self.score_2:
            return self.player_1
        if self.score_1 < self.score_2:
            return self.player_2

    @property
    def is_draw(self):
        return self.score_1 == self.score_2 and self.score_1 is not None



