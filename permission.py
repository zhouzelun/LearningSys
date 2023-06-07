from functools import wraps
from flask import abort,render_template,flash
import database 

class Permissions:
    """
    权限类
    """
    ANONYMOUS_PERMISSION = 1               
    USER_PERMISSION = 2
    MANAGEMENT_PERMISSION = 255


def permission_can(current_user, permission):
    """
    检测用户是否有特定权限
    :param current_user
    :param permission
    :return:
    """
    role = database.get_role_byuser(current_user)
    if(role is None):
        return False
    elif (role.roleid == 1):
        return True
    else:
        return  (role.rolepower & permission) == permission


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            current_user = database.get_user_bysession()
            flag = not permission_can(current_user, permission)
            if(current_user is None):
                message ='请先登录'
                return render_template('login.html',message = message)
            if flag:
                message = '您权限不足，请联系管理员'
                return render_template('login.html',message = message)
            return f(*args, **kwargs)
        return decorated_function
    return decorator