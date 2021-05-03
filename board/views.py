from django.shortcuts import render
import pymongo
from pymongo import MongoClient
import pandas as pd
from collections import Counter
import os
import folium
from folium import plugins
from mongodbTest.settings import TEMPLATE_DIR
import sys
import requests


# Create your views here.



def main(request):
    return render(request,'main.html')

def jacafetag(request):
    conn=MongoClient('127.0.0.1')
    db=conn.test1
    
    #일본 카페 태그
    jacafetags=db.jacafetags
    ja_result_tags=jacafetags.find({},{'tags':1,'_id':0})
    
    # 형태는 리스트형태로 출력이 되었으나 사실은 하나의 문자로 잡혀있었음.
    # tags 나누어 하나르 리스트형태로 담기
    ja_tags_total=[]
    for tags in ja_result_tags:
        test=str(tags['tags'])
        test=test[1:len(test)-1].replace("'",'')
        # print(test)
        test1=test.split(',')
        # print(test1)
        for tag in test1:
            # print(tag)
            ja_tags_total.append(tag)
    # print(tags_total)
    
    jacafe_tag_counts = Counter(ja_tags_total)
    jarank30 =jacafe_tag_counts.most_common(30)
    
    # 따옴표,쉼표 제거 
    cut_tags_total=[]
    for i in jarank30:
        tag=str(i)[1:len(i)-7].replace("'",'').replace(",",'')

        cut_tags_total.append(tag)

    cafe=[]
    for i in range(len(cut_tags_total)):
        cafe.append(cut_tags_total[i])
    
    return render(request,'board/japTags.html',{'jarank30':jarank30,'cafe':cut_tags_total[4],
                                              'fashion':cut_tags_total[6],'cosmetic':cut_tags_total[7],
                                              'food':cut_tags_total[8],'s_travel':cut_tags_total[9]})
    
    
def cafeinfo(request):
    
    popup=[]
    data_lat_log=[]
    a_path='C:/Users/ADMIN/Documents/카카오톡 받은 파일/'
    df=pd.read_csv(os.path.join(a_path,'cafe_info_1.csv'),encoding='utf-8')
    print(df)
    for data in df.values:
        popup.append(data[0])
        data_lat_log.append([data[8],data[9]])
    
    m=folium.Map([35.16370389566739, 129.15879330965538],zoom_start=11)
    plugins.MarkerCluster(data_lat_log, popups=popup).add_to(m)
    #folium.Marker([35.1803305,129.0516257],popups=popup).add_to(m)
    #m.save(os.path.join(TEMPLATE_DIR,'board/kotags/kocafe/cafe_map.html'))
    
    conn=MongoClient('127.0.0.1')
    db=conn.test1
    
    makeup=db.cafe_info_1
    finds=makeup.find({},{'_id':0})
    
    cafetags=db.cafetags
    cafe15=cafetags.find({},{'_id':0})
    
    return render(request,'board/kotags/kocafe/cafeinfo.html',{'finds':finds,'cafe15':cafe15})

    
    
# 韓國ファッション 선택시 메인화면 & #여자코디(쇼핑몰 홈페이지) 
def kofashiontag1(request):
    conn=MongoClient('127.0.0.1')
    db=conn.test1
    
    # 한국 패션태그 30개 
    kofationtags=db.kopashiontags
    kft30=kofationtags.find({},{'_id':0})
    
    # 쇼핑몰 콜렉션 선택
    shopmall=db.kopashionmall
    finds=shopmall.find({},{'_id':0})
       
    
    return render(request,'board/kotags/kofashion/kofashiontag1.html',{
                                               'finds':finds,
                                               'kft30':kft30,
                                               })

# 여자패션(코디샵)
def kofashiontag2(request):
    conn=MongoClient('127.0.0.1')
    db=conn.test1
    
    # 한국 패션태그 30개 
    kofationtags=db.kopashiontags
    kft30=kofationtags.find({},{'_id':0})
    
    # 코디샵 콜렉션 선택
    shopmall=db.kopashiondocishop
    finds=shopmall.find({},{'_id':0})
       
    
    return render(request,'board/kotags/kofashion/kofashiontag2.html',{
                                                'finds':finds,
                                                'kft30':kft30,
                                               })

# 여자코디추천(코디맵)
def kofashiontag3(request):
    conn=MongoClient('127.0.0.1')
    db=conn.test1
    
    # 한국 패션태그 30개 
    kofationtags=db.kopashiontags
    kft30=kofationtags.find({},{'_id':0})
    
    # 코디맵 콜렉션 선택
    shopmall=db.kopashioncodimap
    finds=shopmall.find({},{'_id':0})
       
    
    return render(request,'board/kotags/kofashion/kofashiontag3.html',{
                                               'finds':finds,
                                               'kft30':kft30,
                                               })
    
# 봄코디(스트리트스냅)
def kofashiontag4(request):
    conn=MongoClient('127.0.0.1')
    db=conn.test1

    # 한국 패션태그 30개 
    kofationtags=db.kopashiontags
    kft30=kofationtags.find({},{'_id':0})
    
    # 스트리트스냅 콜렉션 선택
    shopmall=db.kopashionstreet
    finds=shopmall.find({},{'_id':0})
       
    
    return render(request,'board/kotags/kofashion/kofashiontag4.html',{
                                               'finds':finds,
                                               'kft30':kft30,
                                               })
    
# 여자스타일(브랜드스냅)
def kofashiontag5(request):
    conn=MongoClient('127.0.0.1')
    db=conn.test1

    # 한국 패션태그 30개 
    kofationtags=db.kopashiontags
    kft30=kofationtags.find({},{'_id':0})

    #브랜드스냅 콜렉션 선택
    shopmall=db.kopashionbrand
    finds=shopmall.find({},{'_id':0})
       
    
    return render(request,'board/kotags/kofashion/kofashiontag5.html',{
                                               'finds':finds,
                                               'kft30':kft30,
                                               })
    
    
def dataMain(request):
    return render(request,'board/traveldata/dataMain.html')

def board_2015(request):
    conn=MongoClient('127.0.0.1')
    db=conn.test1

    countryEntery=db.cntrentercnt
    find=countryEntery.find({},{'_id':0})
    return render(request,'board/traveldata/yesdb/board_2015.html',{'finds':find})

def board_2016(request):
    conn=MongoClient('127.0.0.1')
    db=conn.test1

    genderEntery=db.gendentercnt
    find=genderEntery.find({},{'_id':0})
    return render(request,'board/traveldata/yesdb/board_2016.html',{'finds':find})

def board_2017(request):
    conn=MongoClient('127.0.0.1')
    db=conn.test1

    ageEntery=db.ageentercnt
    find=ageEntery.find({},{'_id':0})
    print(find)
    return render(request,'board/traveldata/yesdb/board_2017.html',{'finds':find})

def board_2018(request):
    conn=MongoClient('127.0.0.1')
    db=conn.test1

    perposeEntry=db.perpentercnt
    find=perposeEntry.find({},{'_id':0})
    return render(request,'board/traveldata/yesdb/board_2018.html',{'finds':find})

def board_2019(request):
    conn=MongoClient('127.0.0.1')
    db=conn.test1

    perposeEntry=db.perpentercnt
    find=perposeEntry.find({},{'_id':0})
    return render(request,'board/traveldata/yesdb/board_2019.html',{'finds':find})

def board_cafe(request):
    return render(request,'board/traveldata/nodb/board_cafe.html')

def board_fashion(request):
    return render(request,'board/traveldata/nodb/board_fashion.html')

def board_cosmetic(request):
    return render(request,'board/traveldata/nodb/board_cosmetic.html')

def purpose(request):
    return render(request,'board/traveldata/nodb/purpose.html')



def cosmetic(request):
    conn=MongoClient('127.0.0.1')
    db=conn.test1
    
    cosmetic_tags=db.cosmetic_tags
    cos15=cosmetic_tags.find({},{'_id':0})
    
    cosmetic_rank=db.cosmetic_rank
    finds=cosmetic_rank.find({},{'_id':0})
    
    
    return render(request,'board/kotags/kocosmetic/cosmetic.html',{'finds':finds,'cos15':cos15})



def skincare(request):
    conn=MongoClient('127.0.0.1')
    db=conn.test1
    
    cosmetic_tags=db.cosmetic_tags
    cos15=cosmetic_tags.find({},{'_id':0})
    
    skincare_rank=db.skincare_rank
    finds=skincare_rank.find({},{'_id':0})
    
    return render(request,'board/kotags/kocosmetic/skincare.html',{'finds':finds,'cos15':cos15})



def makeup(request):
    conn=MongoClient('127.0.0.1')
    db=conn.test1
    
    cosmetic_tags=db.cosmetic_tags
    cos15=cosmetic_tags.find({},{'_id':0})
    
    makeup=db.makeup
    finds=makeup.find({},{'_id':0})
    
    
    return render(request,'board/kotags/kocosmetic/makeup.html',{'finds':finds,'cos15':cos15})
    
    
def skin(request):
    conn=MongoClient('127.0.0.1')
    db=conn.test1
    
    cosmetic_tags=db.cosmetic_tags
    cos15=cosmetic_tags.find({},{'_id':0})
    
    
    return render(request,'board/kotags/kocosmetic/skin.html',{'cos15':cos15})



def translator(request):
    client_id = "r7dSPQHlOz65t3Z28R5M"
    client_secret = "QqBcssymtm"
    
    data = {'text' : request.GET.get('text'),
            'source' : 'ko',
            'target': 'ja'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id":client_id,
              "X-Naver-Client-Secret":client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code
    
    text=request.GET.get('text');
    
    
    if rescode==200:     
        t_data = response.json()
        return render(request,'board/translator/translator.html',{'result':t_data['message']['result']['translatedText'],'text':text})
    else:
        return render(request,'board/translator/translator.html')

#관광정보
def tourapi(request):
    conn=MongoClient('127.0.0.1')
    db=conn.test1
    
    makeup=db.tourapi
    finds=makeup.find({},{'_id':0})
    
    return render(request,'board/kotravel/tourinfo.html',{'finds':finds})
  

