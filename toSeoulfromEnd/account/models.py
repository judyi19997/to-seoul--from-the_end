from django.db import models
from django.contrib.auth.models import AbstractUser #상속받을 기본 유저 모델



# Create your models here.

class customModel(AbstractUser):
    GENDER = (
        ('M', '남자'),
        ('F', '여자'),
        ('O', '그 밖의 다른 성')
    )

    gender = models.CharField(max_length = 10, null = True, blank = True,choices = GENDER)
    image = models.ImageField(null = True, blank = True)
    date = models.DateField(null = True, blank = True) #기본 포맷 작성 가능한거 검색해보기.
