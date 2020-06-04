from django.shortcuts import render
from lib.http import render_json
from social.logic import get_rcmd_users
from social import logic
from social.models import Swiped,Friend
# Create your views here.

def get_users(request):

    ''' 获取推荐用户 '''
    per_page = 10
    page = int(request.GET.get('page',1))  #‘页码“
    start = (page - 1)*per_page
    end = start + per_page

    users=get_rcmd_users(request.user)[start:end]  #"匹配的所有用户"
    result = [u.to_dict() for u in users]
    return render_json(result)

def like(request):
    """喜欢"""
    sid = int(request.POST.get('sid'))
    is_matched = logic.like_someone(request.user,sid)
    return render_json({'is_matched':is_matched})


def superlike(request):
    """超级喜欢"""
    sid = int(request.POST.get('sid'))
    is_matched = logic.superlike_someone(request.user, sid)
    return render_json({'is_matched': is_matched})


def dislike(request):
    """不喜欢"""
    sid = int(request.POST.get('sid'))
    Swiped.mark(request.user.id, sid, 'dislike')
    return render_json(None)


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
