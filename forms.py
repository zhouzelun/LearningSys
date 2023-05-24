
import wtforms
from wtforms.validators import length,email,EqualTo
class LoginForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3,max=20)])
    password = wtforms.StringField(validators=[length(min=0,max=20)])


