from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        marvel_team = Team.objects.create(name='Marvel', members=['Spider-Man', 'Iron Man', 'Captain America'])
        dc_team = Team.objects.create(name='DC', members=['Batman', 'Superman', 'Wonder Woman'])

        User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='Marvel', is_superhero=True)
        User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel', is_superhero=True)
        User.objects.create(email='batman@dc.com', name='Batman', team='DC', is_superhero=True)
        User.objects.create(email='superman@dc.com', name='Superman', team='DC', is_superhero=True)

        Activity.objects.create(user='Spider-Man', activity_type='Running', duration=30, date='2026-03-10')
        Activity.objects.create(user='Iron Man', activity_type='Cycling', duration=45, date='2026-03-09')
        Activity.objects.create(user='Batman', activity_type='Swimming', duration=60, date='2026-03-08')

        Leaderboard.objects.create(team='Marvel', points=175)
        Leaderboard.objects.create(team='DC', points=160)

        Workout.objects.create(name='Pushups', description='Upper body exercise', difficulty='Easy')
        Workout.objects.create(name='Squats', description='Lower body exercise', difficulty='Medium')
        Workout.objects.create(name='Plank', description='Core exercise', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
