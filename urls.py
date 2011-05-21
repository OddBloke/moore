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

from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',direct_to_template, {'template':'index.html'}),
    # Examples:
    # url(r'^$', 'moore.views.home', name='home'),
    # url(r'^moore/', include('moore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

)

#if settings.DEBUG:
#    urlpatterns += patterns('',
#        (r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),
#    )

