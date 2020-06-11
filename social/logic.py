from user.models import User
import datetime
from social.models import Swiped
from social.models import Friend

# from lib.cache import rds
from django_redis import get_redis_connection

def get_rcmd_users(user):
    '''
    获取推荐用户

       max_year        min_year     current_year
    ----|-----------------|----------------|--------------|-------->
                                          2018           2019
    '''
    sex = user.profile.dating_sex
    location = user.profile.location
    min_age = user.profile.min_dating_age
    max_age = user.profile.max_dating_age

    current_year = datetime.date.today().year
    min_year = current_year - min_age
    max_year = current_year - max_age

    users = User.objects.filter(sex=sex,
                                location=location,
                                birth_year__gte=max_year,
                                birth_year__lte=min_year)
    return users

def like_someone(user,sid,):
    Swiped.mark(user.id,sid,'like')
    if not Swiped.is_liked(sid,user.id):
        Friend.be_friends(user.id,sid)
        return True
    else:
        return False

def superlike_someone(user,sid,):
    Swiped.mark(user.id,sid,'superlike')
    if not Swiped.is_liked(sid,user.id):
        Friend.be_friends(user.id,sid)
        return True
    else:
        return False


def rewind(user):
    '''反悔'''
    '''取出最后一次滑动记录'''
    swiped = Swiped.objects.filter(uid=user.id).latest('id')
    '''删除好友关系'''
    if swiped.flag in ['superlike','like']:
        Friend.break_off(user.id,swiped.sid)
    '''删除好友记录'''
    swiped.delete()


def users_liked_me(user):
    swipes = Swiped.like_me(user.id)
    swiped_uid_list = [s.uid for s in swipes]
    return User.objects.filter(id__in=swiped_uid_list)


def add_swipe_score(uid,flag):
    '''添加被滑动的积分记录'''
    rds=get_redis_connection('default')

    score = {'like':5,'superlike':7,'dislike':-5}[flag]
    rds.zincrby('HotSwiped',uid,score)

def get_top_n_swiped(num=10):
    '''获取topn 的华东数据'''
    rds=get_redis_connection('default')
    origin_data = rds.zrevrange('HotSwiped',0,num-1,withscores=True)
    cleaned = [[int(uid),int(swiped)] for uid, swiped in origin_data]
    uid_list = [uid for uid,_ in cleaned]
    users = User.objects.filter(in__in=uid_list)