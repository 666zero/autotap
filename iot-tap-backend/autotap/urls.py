"""
Copyright (C) 2018-2019  Jesse Martinez, Lefan Zhang, Weijia He, Noah Brackenbury

iot-tap-backend is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

iot-tap-backend is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with iot-tap-backend.  If not, see <https://www.gnu.org/licenses/>.
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('fix/', views.fix, name='fix'),
    path('reproduce/', views.reproduce, name='reproduce'),
    path('synthesize/', views.synthesize, name='synthesize'),
    path('multisp/', views.multisp, name='multisp'),
    path('debug/', views.debug, name='debug')
]
