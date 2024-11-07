from django.db import models
# AbstractUserクラスをインポート
from django.contrib.auth.models import AbstractUser

# ユーザークラスを継承したカスタムユーザーモデル
class CustomUser(AbstractUser):
    pass
