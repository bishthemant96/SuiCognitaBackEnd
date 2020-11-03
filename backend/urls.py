#Standard Files
from django.contrib import admin
from django.urls import path

#User Generates Views
from dashboard.views.occupational_picks import OccupationalPicks
from dashboard.views.personalised_picks import PersonalisedPicks
from dashboard.views.preferential_picks import PreferentialPicks
from dashboard.views.trending_picks import TrendingPicks
from dashboard.views.ratings import Rating
from signing.views.authenticate import Authenticate
from signing.views.register import Register
from signing.views.preferences import Preferences

urlpatterns = [

    path('admin/', admin.site.urls),

    path('OccupationalPicks/<int:id>', OccupationalPicks.as_view()),
    path('PersonalisedPicks/<int:id>', PersonalisedPicks.as_view()),
    path('PreferentialPicks/<int:id>', PreferentialPicks.as_view()),
    path('TrendingPicks/<int:id>', TrendingPicks.as_view()),
    path('Rating/', Rating.as_view()),

    path('Authenticate/', Authenticate.as_view()),
    path('Register/', Register.as_view()),
    path('Preferences/', Preferences.as_view()),

]
