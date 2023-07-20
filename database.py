from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

DATABASE = {
    'drivername': 'postgresql+psycopg2', #Тут можно использовать MySQL или другой драйвер
    'host': 'localhost',
    'port': '5432',
    'username': 'root',
    'password': 'password',
    'database': 'root'
}

DeclarativeBase = declarative_base()

faculties = [
    {
        'name' : 'Факультет прикладной математики и информатики',
        'short_name' : 'ФПМИ'
    },
    {
        'name' : 'Факультет бизнеса',
        'short_name' : 'ФБ'
    },
     {
        'name' : 'Факультет автоматики и вычислительной техники',
        'short_name' : 'АВТФ'
    }
]

groups = [
    {
        'faculty_id' : 4,
        'name' : 'ПМ-91'
    },
     {
        'faculty_id' : 4,
        'name' : 'ПМ-92'
    },
    {
        'faculty_id' : 4,
        'name' : 'ПМ-93'
    },
    {
        'faculty_id' : 5,
        'name' : 'ФБ-91'
    },
     {
        'faculty_id' : 5,
        'name' : 'ФБ-92'
    },
    {
        'faculty_id' : 6,
        'name' : 'АВТ-91'
    },
    {
        'faculty_id' : 6,
        'name' : 'АВТ-92'
    },
    {
        'faculty_id' : 6,
        'name' : 'АВТ-93'
    }
]

students = [
    {
        'group_id':19,
        'surname' : 'Ихутин',
        'name':'Михуил',
        'mid_name':'Александрович'
    },
    {
        'group_id':19,
        'surname' : 'Буркалов',
        'name':'Владимир',
        'mid_name':'Александрович'
    },
    {
        'group_id':19,
        'surname' : 'Патанин',
        'name':'Александр',
        'mid_name':'Александрович'
    },
    {
        'group_id':21,
        'surname' : 'Прыткова',
        'name':'София',
        'mid_name':'Александровна'
    },
    {
        'group_id':22,
        'surname' : 'Сидорова',
        'name':'Александра',
        'mid_name':'Александровна'
    },
    {
        'group_id':24,
        'surname' : 'Зайцев',
        'name':'Иван',
        'mid_name':'Александрович'
    },
]

projects = [
    {
        'name' : 'Разработка элементов системы для человеко-машинного взаимодействия на естественном языке'
    },
    {
        'name' : 'Сравнительный анализ методик прогнозирования доходов субфедеральных бюджетов'
    },
     {
        'name' : 'Разработка решений для индустрии интернета вещей'
    },
]

project_authors = [
    {
        'author_id':7,
        'project_id':1
    },
    {
        'author_id':8,
        'project_id':1
    },
    {
        'author_id':9,
        'project_id':1
    },
    {
        'author_id':10,
        'project_id':2
    },
    {
        'author_id':11,
        'project_id':3
    },
]

class Faculties(DeclarativeBase):
    __tablename__ = 'Faculties'

    id = Column(Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    short_name = Column('short_name', String(4), nullable=False)

    def __repr__(self):
        return "".format(self.code)

class Groups(DeclarativeBase):
    __tablename__ = 'Groups'

    id = Column(Integer, primary_key=True)
    faculty_id = Column(Integer, ForeignKey("Faculties.id"), nullable=False)
    name = Column('name', String, nullable=False)
   
    def __repr__(self):
        return "".format(self.code)
        
class Students(DeclarativeBase):
    __tablename__ = 'Students'

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey("Groups.id"), nullable=False)
    surname = Column('surname', String, nullable=False)
    name = Column('name', String, nullable=False)
    mid_name = Column('mid_name', String, nullable=False)
   
    def __repr__(self):
        return "".format(self.code)

class Projects(DeclarativeBase):
    __tablename__ = 'Projects'

    id = Column(Integer, primary_key=True)
    name = Column('name', String, nullable=False)
   
    def __repr__(self):
        return "".format(self.code)

class Project_Authors(DeclarativeBase):
    __tablename__ = 'Projects_Authors'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("Students.id"), nullable=False)
    project_id = Column(Integer, ForeignKey("Projects.id"), nullable=False)
   
    def __repr__(self):
        return "".format(self.code)

def main():
    engine = create_engine(URL(**DATABASE))
    DeclarativeBase.metadata.create_all(engine)
    # Session = sessionmaker(bind=engine)
    # session = Session()
    # for faculty in faculties:
    #     new_faculty = Faculties(name=faculty['name'], short_name=faculty['short_name'])
    #     session.add(new_faculty)
    # session.commit()

    # for group in groups:
    #     new_group = Groups(faculty_id=group['faculty_id'], name=group['name'])
    #     session.add(new_group)      
    # session.commit()

    # for student in students:
    #     new_student = Students(group_id=student['group_id'], surname=student['surname'], name=student['name'], mid_name=student['mid_name'])
    #     session.add(new_student) 
    # session.commit()

    # for project in projects:
    #     new_project = Projects(name=project['name'])
    #     session.add(new_project) 
    # session.commit()

    # for project_author in project_authors:
    #     new_project_author = Project_Authors(author_id=project_author['author_id'], project_id=project_author['project_id'])
    #     session.add(new_project_author) 
    # session.commit()

if __name__ == "__main__":
    main()