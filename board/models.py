from django.db import models

# Create your models here.

class User(models.Model): # 장고에서 제공하는 models.Model를 상속
    #models.CharField=문자열을 넣을 필드를 생성, 게시글의 경우 models.TextField를 사용
    #verbose_name=나중에 admin페이지에서 보여지는 이름
    username=models.CharField(max_length=64,verbose_name='사용자명')
    password=models.CharField(max_length=64,verbose_name='비밀번호')
    #저장되는 시점의 시간을 자동으로 삽입
    registered_dttm=models.DateTimeField(auto_now_add=True,verbose_name='등록시간')
    
    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table='test_user'