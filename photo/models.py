from django.db import models
from accounts.models import CustomUser

# 投稿する写真のカテゴリを管理するモデル    
class Category(models.Model):
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20
    )
    def __str__(self):
        # オブジェクトを文字列に変換して返す
        # Returns(str):投稿記事のタイトル
        return self.title

# 投稿されたデータを管理するモデル    
class PhotoPost(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )
    
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
    )
    
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
    )
    
    comment = models.TextField(
        verbose_name='コメント',
    )

    image1 = models.ImageField(
        verbose_name='イメージ1',
        upload_to='photos'          # MEDIA_ROOT以下のphotosにファイルを保存
    )

    image2 = models.ImageField(
        verbose_name='イメージ2',
        upload_to='photos',         # MEDIA_ROOT以下のphotosにファイルを保存
        blank=True,                 # フィールド値の設定は必須ではない
        null=True                   # データベースにnullが保存されることを許容
    )

    posted_at =models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True           # 日時を自動追加 
    )
    
    def __str__(self):
        # オブジェクトを文字列に変換して返す
        # Returns(str):投稿記事のタイトル
        return self.title
