#!/usr/bin/env python

from django.contrib import admin
from basketball.models import Team, Player

admin.site.register(Team)
admin.site.register(Player)



