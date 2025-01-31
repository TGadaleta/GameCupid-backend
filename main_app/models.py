from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
PLATFORMS = (
    ('Blizzard', 'Blizzard'),
    ('Epic',"Epic"),
    ('Microsoft',"Microsoft"),
    ('Nintendo',"Nintendo"),
    ('Sony',"Sony"),
    ('Steam',"Steam"),
    ('Ubisoft',"Ubisoft"),
)

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    gender = models.CharField(
        max_length=20,
        choices = (
            ('default','default'),
            ('he/him','he/him'),
            ('she/her','she/her'),
            ('they/them','they/them'),
            ('other','other'),
        ),
        default='default'
    )
    city = models.CharField(max_length=50)
    profile_likes = models.JSONField(default=list, blank=True, null=True)

    def __str__(self):
        return f"Profile for username {self.user.username} id {self.id}."

class Profile_Match(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='match_initiated')
    match_profile_id =  models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='match_recieved')
    date_matched = models.DateField()
        
    def __str__(self):
        return f"{self.profile_id.user} matched {self.match_profile_id.user} on {self.date_matched}."

class Profile_Block(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='block_initiated')
    blocked_profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='block_recieved')
    date_blocked = models.DateField()

    def __str__(self):
        return f"{self.profile_id.user} blocked {self.blocked_profile_id.user} on {self.date_blocked}."

class Game(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    genre = models.JSONField(default=list)
    fav_rank = models.IntegerField()

    class Meta:
        ordering = ['fav_rank']

    def __str__(self):
        return f"{self.profile_id.user.username} number {self.fav_rank} game - {self.title}" 
    
class Platform(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    brand = models.CharField(
        choices = PLATFORMS,
        default = PLATFORMS[0][0],
        max_length=20
    )
    tag = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.profile_id.user.username} on {self.brand} is named {self.tag}."



class Genre_Scores(models.Model):
    profile_id = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='profile')
    pinball = models.IntegerField(default=0)
    adventure = models.IntegerField(default=0)
    indie = models.IntegerField(default=0)
    arcade = models.IntegerField(default=0)
    visual_novel = models.IntegerField(default=0)
    card_and_board = models.IntegerField(default=0)
    moba = models.IntegerField(default=0)
    point_and_click = models.IntegerField(default=0)
    fighting = models.IntegerField(default=0)
    shooter = models.IntegerField(default=0)
    music = models.IntegerField(default=0)
    platform = models.IntegerField(default=0)
    puzzle = models.IntegerField(default=0)
    racing = models.IntegerField(default=0)
    real_time_strategy = models.IntegerField(default=0)
    role_playing = models.IntegerField(default=0)
    simulator = models.IntegerField(default=0)
    sport = models.IntegerField(default=0)
    strategy = models.IntegerField(default=0)
    turn_based_strategy = models.IntegerField(default=0)
    tactical = models.IntegerField(default=0)
    hand_and_slash = models.IntegerField(default=0)
    quiz_trivia = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.profile_id.user.username} genre scores."