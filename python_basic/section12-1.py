# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now : ', now)

nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDateTime : ', nowDateTime)

# sqlite3
print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqlite_version : ', sqlite3.sqlite_version)

# DB생성 & Auto Commit
conn = sqlite3.connect('C:/python_basic/resource/database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print('cursor type : ' , c)

# 테이블 생성(Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
c.execute("INSERT INTO users VALUES(1, 'JEONG', 'isaac@gmail.com', '010-2222-4444', 'Jeong.com', ?)", (nowDateTime,))
c.execute("INSERT INTO users (id, username, email, phone, website, regdate ) VALUES(?,?,?,?,?,?)", (2, 'Park', 'Park@daum.net', '010-1111-2222', 'Park.com', nowDateTime) )

# Many 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-333-3333', 'Lee.com', nowDateTime),
    (4, 'Joe', 'Joe@naver.com', '010-444-5444', 'Joe.com', nowDateTime),
    (5, 'Choi', 'Choi@naver.com', '010-555-5555', 'Choi.com', nowDateTime)
)

c.executemany("INSERT INTO users (id, username, email, phone, website, regdate) VALUES(?,?,?,?,?, ?)", userList)

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")
# rowcount로 지워진 결과값을 반환
# print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level=None 일 경우 자동 반영(auto commit)
# conn.commit() : 옵션이 없다면 
# 롤백
# conn.rollback() 

# 리소스를 사용했으면 항상 닫아주어야 한다
conn.close()