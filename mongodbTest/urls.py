from django.contrib import admin
from django.urls import path
from board import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',views.main),
    path('main/translator/',views.translator),
    path('main/japTags/',views.jacafetag),
    
    path('main/japTags/kofashiontags/ftag1',views.kofashiontag1),
    path('main/japTags/kofashiontags/ftag2',views.kofashiontag2),
    path('main/japTags/kofashiontags/ftag3',views.kofashiontag3),
    path('main/japTags/kofashiontags/ftag4',views.kofashiontag4),
    path('main/japTags/kofashiontags/ftag5',views.kofashiontag5),
    
    path('main/dataMain/',views.dataMain),
    path('main/dataMain/board_2015',views.board_2015),
    path('main/dataMain/board_2016',views.board_2016),
    path('main/dataMain/board_2017',views.board_2017),
    path('main/dataMain/board_2018',views.board_2018),
    path('main/dataMain/board_2019',views.board_2019),
    
    path('main/dataMain/board_cafe',views.board_cafe),
    path('main/dataMain/board_fashion',views.board_fashion),
    path('main/dataMain/board_cosmetic',views.board_cosmetic),
    
    path('main/dataMain/purpose',views.purpose),
    
    path('main/japTags/kocafe/cafeinfo',views.cafeinfo),
        
    path('main/japTags/kocosmetictags/cosmetic',views.cosmetic),
    path('main/japTags/kocosmetictags/skincare',views.skincare),
    path('main/japTags/kocosmetictags/makeup',views.makeup),
    path('main/japTags/kocosmetictags/skin',views.skin),
    
    path('translator/',views.translator),
    
    path('main/kotravel/tourinfo',views.tourapi),
]
