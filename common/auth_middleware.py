from django.utils.deprecation import MiddlewareMixin
from user.models import User
from lib.http import render_json
from common import error



class AuthMiddleware(MiddlewareMixin):

    '''用户登陆验证中间件'''
    WHITE_LIST = [
        '/api/user/verify',
        '/api/user/login',
    ]
    # 进行登陆检查
    def process_request(self,request):
        # 如果请求的 URL 在白名单内，直接跳过检查
        for path in self.WHITE_LIST:
            if request.path.startswith(path):
                return None
        uid = request.session.get('uid')
        if uid:
            try:
                user = User.objects.get(id=uid)
                request.user = user
                return None
            except User.DoesNotExist:
                request.session.flush()
        return render_json(None, code=error.LOGIN_ERROR)