from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        # model = User  # django에서는 User를 직접 참조를 권하지 않음
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)  # user name은 default값이라 뺴는거 불가
        # 기존꺼 외에도 이메일 등 넣고 싶으면 공식문서 참고해서 이런식으로 해주면 됨! <- 확장(존재하는 것 중에)
        # 그리고 optional한 것이기 때문에 안 넣어도 가입 됨. // db들어가보면 fields가 머있나 알 수 있음, 혹은 유저 설계도(migrations), 혹은 공식문서
    
class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)  # 관리자 권한 페이지가 보여주기 때문에 공개할 거만 올려주는 것