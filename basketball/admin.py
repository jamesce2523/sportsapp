#!/usr/bin/env python

from django.contrib import admin
from roster.models import Team

class TeamAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(Team, TeamAdmin)