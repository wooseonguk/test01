'''
Created on 2021. 3. 22.

@author: ADMIN
'''
import pymongo
from pymongo import MongoClient #from이 있을경우 import뒤에있는건 함수 인데 db연동 모듈 추가역할을 합니다

#db연동
conn=MongoClient('127.0.0.1')

# print(conn) # MongoClient(host=['127.0.0.1:27017'], document_class=dict, tz_aware=False, connect=True)

#db.collection.함수()

#db.collection.함수()

# db 생성
# db = conn.test_db
# collection 생성
# collect = db.collect # collect = conn.test_db.collect 쉽게말하면 이 db와 이 collect를 가지고있는거죠

#document 생성 : {'key':'value'}
# doc1 = {'empno':'10001', 'name':'hong', 'phone':'010-111-111', 'age':35}
# doc2 = {'empno':'10002', 'name':'lee', 'age':45}
# doc3 = {'empno':'10003', 'name':'yoo', 'phone':'010-222-222', 'age':25}
#
# del1 = {'empno':'10001'}
# del2 = {'$set':{'name':'뭐여'}}
# collection에 문서 추가

# collect.insert(doc1)
# collect.insert(doc2)
# collect.insert(doc3)


#문서 삭제 : db.collection.remove() -> collect.remove()
#collect.remove({'empno' : '10002'})

#문서 수정 : db.collection.update()
#collect.update( {'empno':'10001'}, {'$set':{'name':'kim'}}, True)#조건, 수정할거, 똑같은거 모두 수정할건지 true/false

db=conn.test

test=db.test

result=test.find()

print('조건 검색')
result2=test.find({'tag':'AA'})

for i in result:
    print(i)
    
    



