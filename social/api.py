from django.shortcuts import render
from lib.http import render_json
from social.logic import get_rcmd_users
from social import logic
from social.models import Swiped,Friend
from vip.logic import need_perm
# Create your views here.
from lib.rediscache import rds
def get_users(request):

    ''' 获取推荐用户 '''
    per_page = 10
    page = int(request.GET.get('page',1))  #‘页码“
    start = (page - 1)*per_page
    end = start + per_page

    users=get_rcmd_users(request.user)[start:end]  #"匹配的所有用户"
    result = [u.to_dict() for u in users]
    return render_json(result)

def new_rcmd_users(request):
    ''' 基于redis的获取推荐用户 '''
    users=logic.get_rcmd_user_from_redis(request.user)
    result = [u.to_dict() for u in users]
    return render_json(result)

def like(request):
    """喜欢"""
    sid = int(request.POST.get('sid'))
    logic.add_swipe_score(sid, 'like')

    is_matched = logic.like_someone(request.user,sid)
    rds.srem('RCMD-%s' %request.user.id,sid)
    return render_json({'is_matched':is_matched})

@need_perm('superlike')
def superlike(request):
    """超级喜欢"""
    sid = int(request.POST.get('sid'))

    logic.add_swipe_score(sid, 'superlike')

    is_matched = logic.superlike_someone(request.user, sid)
    rds.srem('RCMD-%s' %request.user.id,sid)
    return render_json({'is_matched': is_matched})


def dislike(request):
    """不喜欢"""
    sid = int(request.POST.get('sid'))
    logic.add_swipe_score(sid, 'dislike')

    Swiped.mark(request.user.id, sid, 'dislike')
    rds.srem('RCMD-%s' %request.user.id,sid)
    return render_json(None)

@need_perm('rewind')
def rewind(request):
    """反悔"""
    logic.rewind(request.user)
    return render_json(None)



def show_liked_me(request):
    '''查看喜欢过我的人'''
    users = logic.users_liked_me(request.user)
    result = [u.to_dict() for u in users]
    return render_json(result)


def friends(request):
    '''好友列表'''
    my_friends = Friend.friends(request.user.id)
    friends_info = [frd.to_dict() for frd in my_friends]
    return render_json({'friends': friends_info})

def hot_swiped(request):
    # 获取最热榜单
    data =logic.get_top_n_swiped(10)
    for item in data:
        item[0] = item[0].to_dict()
    return render_json(data)