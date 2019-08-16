import sqlite3
conn = sqlite3.connect("answers.db")
cursor = conn.cursor()

cursor.execute("drop table Answers")
cursor.execute("""
create table Answers (

id integer,
ans text
);


""")
cursor.execute("""
insert into Answers 
values (1,"Добро пожаловать на мой сайт! надеюсь, задания, собранные здесь, будут вам полезны и интересны)")
""")
cursor.execute("""
insert into Answers 
values (2,"Не так уж и сложно, не правда ли ?")
""")
cursor.execute("""
insert into Answers 
values (3,"flag{Новый формат ответов}")
""")

cursor.execute("""
insert into Answers 
values (4,"flag{Я с7тан0влюсь р0б070м'%@%'}")
""")

cursor.execute("drop table Answers_symmetry")
cursor.execute("""
create table Answers_symmetry (

id integer,
ans text
);


""")
cursor.execute("""
insert into Answers_symmetry
values (1,"studyflag{test pr0id3n m0l0dec}")
""")


cursor.execute("""
insert into Answers_symmetry
values (2,"studyfLag{welc0me my dar1ing!}")
""")

conn.commit()
conn.close()
