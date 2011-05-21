# moore - a wrestling database
# Copyright (C) 2011  Daniel Watkins
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.contrib import admin

from matches.models import (Card,
                            CardEvent,
                            EventType,
                            Match,
                            MatchType,
                            MatchTypeAspect,
                            Participation,
                            Role,
                            CardType,
                            Venue,
                            CardSeries,
                           )


class CardEventInlineAdmin(admin.TabularInline):

    model = CardEvent


class CardAdmin(admin.ModelAdmin):

    inlines = [
        CardEventInlineAdmin,
    ]


class ParticipationAdmin(admin.TabularInline):

    model = Participation


class CardEventAdmin(admin.ModelAdmin):

    inlines = [
        ParticipationAdmin,
    ]


class MatchAdmin(admin.ModelAdmin):

    inlines = [
        ParticipationAdmin,
    ]
    exclude = ['event_type']


admin.site.register(Card, CardAdmin)
admin.site.register(CardEvent, CardEventAdmin)
admin.site.register(EventType)
admin.site.register(Match, MatchAdmin)
admin.site.register(MatchType)
admin.site.register(MatchTypeAspect)
admin.site.register(Role)
admin.site.register(CardType)
admin.site.register(Venue)
admin.site.register(CardSeries)



