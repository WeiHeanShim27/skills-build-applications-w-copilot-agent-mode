from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team='marvel')
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team='marvel')
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team='dc')
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team='dc')

        # Activities
        Activity.objects.create(user='Tony Stark', type='run', duration=30, date='2023-01-01')
        Activity.objects.create(user='Steve Rogers', type='swim', duration=45, date='2023-01-02')
        Activity.objects.create(user='Bruce Wayne', type='cycle', duration=60, date='2023-01-03')
        Activity.objects.create(user='Clark Kent', type='fly', duration=120, date='2023-01-04')

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Situps', description='Do 30 situps')

        # Leaderboard
        Leaderboard.objects.create(user='Tony Stark', score=100)
        Leaderboard.objects.create(user='Steve Rogers', score=90)
        Leaderboard.objects.create(user='Bruce Wayne', score=95)
        Leaderboard.objects.create(user='Clark Kent', score=110)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
