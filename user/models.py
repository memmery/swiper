import datetime
from lib.orm import ModelMixin
from django.db import models
from django.utils.functional import cached_property


class User(models.Model,ModelMixin):
    '''用户数据模型'''

    SEX = (
        ('男性', '男性'),
        ('女性', '女性'),
    )

    nickname = models.CharField(max_length=32, unique=True)
    phonenum = models.CharField(max_length=16, unique=True)

    sex = models.CharField(max_length=8, choices=SEX)
    avatar = models.CharField(max_length=256,verbose_name='个人形象')
    location = models.CharField(max_length=32,verbose_name='常居地')
    birth_year = models.IntegerField(default=2000,verbose_name='出生年')
    birth_month = models.IntegerField(default=1,verbose_name='出生月')
    birth_day = models.IntegerField(default=1,verbose_name='出生日')

    @property
    def age(self):
        today = datetime.date.today()
        birth_date = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        times = today - birth_date
        return times.days // 365


    # def to_dict(self):  由于每处都需要所以做成多继承,ModelMixin
    #     return {
    #         'id': self.id,
    #         'nickname': self.nickname,
    #         'phonenum': self.phonenum,
    #         'sex': self.sex,
    #         'avatar': self.avatar,
    #         'location': self.location,
    #         'age': self.age,
    #     }
    @property
    def profile(self):
        '''用户的配置项'''
        if not hasattr(self, '_profile'):
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        return self._profile

class Profile(models.Model,ModelMixin):
    '''用户配置项'''

    SEX = (
        ('男性', '男性'),
        ('女性', '女性'),
    )


    dating_sex = models.CharField(default='女性', max_length=8, choices=SEX, verbose_name='匹配的性别')
    location = models.CharField(max_length=32, verbose_name='目标城市')

    min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=10, verbose_name='最大查找范围')

    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=45, verbose_name='最大交友年龄')

    vibration = models.BooleanField(default=True, verbose_name='是否开启震动')
    only_matche = models.BooleanField(default=True, verbose_name='不让为匹配的人看我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='是否自动播放视频')

 
