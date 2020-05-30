OK = 0
VCODE_ERROR = 1000
LOGIN_ERROR = 1001
PROFILE_ERROR = 1002
FILE_NOT_FOUND = 1003
NOT_HAS_PERM = 1004


class LogicError(Exception):
    code=0

    def __str__(self):
        return self.__class__.__name__

def generate_logic_error(name,code):
    base_cls = (LogicError,)
    return type(name,base_cls,{'code':code})


Ok = generate_logic_error('Ok',0)

VcodeError = generate_logic_error('VcodeError',1000)

VcodeExist = generate_logic_error('VcodeExist',1001)

LoginError = generate_logic_error('LoginError',1002)

ProfileErro = generate_logic_error('ProfileError',1003)

FileNotFound = generate_logic_error('FileNotFound',1004)

NotHasPerm = generate_logic_error('NotHasPerm',1005)





