from django.db import models


from django.db.models import Q
from user.models import User

class Swiped(models.Model):
    '''滑动记录'''
    FLAGS = (
        ('superlike', '超级喜欢'),
        ('like', '喜欢'),
        ('dislike', '不喜欢'),
    )

    uid = models.IntegerField(verbose_name='滑动者的 UID')
    sid = models.IntegerField(verbose_name='被滑动者的 UID')
    flag = models.CharField(max_length=16, choices=FLAGS)
    time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def mark(cls, uid, sid, flag):
        '''标记一次滑动'''
        if flag in ['superlike', 'like', 'dislike']:
            defaults = {'flag': flag}
            cls.objects.update_or_create(uid=uid, sid=sid, defaults=defaults)
            obj = cls.objects.update_or_create(uid=uid, sid=sid, defaults=defaults)
        return obj

    @classmethod
    def is_liked(cls, uid, sid):
        '''检查是否喜欢过某人'''
        return cls.objects.filter(uid=uid, sid=sid,
                                  flag__in=['like', 'superlike']).exists()
    @classmethod
    def like_me(cls,uid):
        return cls.objects.filter(sid=uid,flag__in=['like', 'superlike'])


class Friend(models.Model):
    '''好友'''
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()

    @classmethod
    def be_friends(cls, uid1, uid2):
        '''成为好友'''
        uid1, uid2 = (uid1, uid2) if uid1 < uid2 else (uid2, uid1)
        cls.objects.get_or_create(uid1=uid1, uid2=uid2)

    @classmethod
    def is_friend(cls, uid1, uid2):
        '''检查是否是好友关系'''
        condition = Q(uid1=uid1, uid2=uid2) | Q(uid1=uid2, uid2=uid1)
        return cls.objects.filter(condition).exists()

    @classmethod
    def break_off(cls, uid1, uid2):
        '''绝交'''
        uid1, uid2 = (uid1, uid2) if uid1 < uid2 else (uid2, uid1)
        try:
            cls.objects.filter(uid1=uid1, uid2=uid2).delete()
        except cls.DoesNotExist:
            pass

    @classmethod
    def friends(cls, uid):
        condition = Q(uid1=uid) | Q(uid2=uid)
        relations = cls.objects.filter(condition)  # 过滤出我的好友关系

        friend_id_list = []
        for r in relations:
            friend_id = r.uid2 if r.uid1 == uid else r.uid1
            friend_id_list.append(friend_id)

        return User.objects.filter(id__in=friend_id_list)
