"""비밀번호 토큰을 생성하기 위해 사용한다."""
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.id) + six.text_type(timestamp) +
             six.text_type(user.activate)
        )

account_activation_token = AccountActivationTokenGenerator()
