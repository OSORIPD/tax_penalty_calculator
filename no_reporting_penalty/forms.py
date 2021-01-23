from django import forms
from django.contrib.auth.hashers import check_password
 
 
class LoginForm(forms.Form):
    username = forms.CharField(max_length=64,
                               label="사용자 이름",
                               error_messages={'required': '아이디를 입력해주세요.'})
    password = forms.CharField(widget=forms.PasswordInput,
                               label="비밀번호",
                               error_messages={'required': '비밀번호를를 력해주세요.'})
 
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        print('username: ',username)
        print('password: ',password)

        # if username and password:
        #     user = DoonyUsers.objects.get(username = username)
        #     if not check_password(password, user.password):
        #         self.add_error('password', '비밀번호가 틀렸습니다.')
 
        #     else:
        #         self.user_id = user.id



