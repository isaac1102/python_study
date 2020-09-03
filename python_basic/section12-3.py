# Section12-3
# 파이썬 데이터베이스 연동(sqlite)
# 테이블 데이터 수정 및 삭제

import  sqlite3

# DB생성 (파일)
conn = sqlite3.connect('D:/python_basic/resource/database.db')

# Cursor 연결
c = conn.cursor()


# 데이터 수정1
# c.execute('update users set username = ? where id = ?', ('nicemane', 2))

# 데이터 수정2
# c.execute('update users set username = :name where id = :id', {'name':'goodman','id':5 })

# 데이터 수정3
# c.execute('update users set username = "%s" where id = "%s" ' % ('badboy', 3))

# 중간 데이터 확인
for user in c.execute('select * from users'):
    print(user)

# Row delete1 (튜플)
# c.execute('delete from users where id = ?', (2,))

# Row delete2(딕셔너리)
# c.execute('delete from users where id =:id', {'id':5})

# Row delete3
# c.execute('delete from users where id =%s' % 4)

# 테이블 전체 데이터 삭제
print("user db delete : ", conn.execute("delete from users").rowcount, 'rows')
conn.commit()

# 접속 해제
conn.close()