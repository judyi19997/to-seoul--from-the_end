from django.db import models
from django.contrib.auth.models import abstractUser #상속받을 기본 유저 모델



# Create your models here.

class customModel(abstractUser):
    GENDER = (
        ('M': '남자'),
        ('F': '여자'),
        ('O': '그 밖의 다른 성')
    )

    gender = models.CharField(maxlength = 10,choices = GENDER)
    image = models.ImageField()
    date = models.DateField() #기본 포맷 작성 가능한거 검색해보기.
