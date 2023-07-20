from dash import Dash, dcc, html, Input, Output, dash_table
import sqlalchemy as db
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
import pandas as pd
import dash

DATABASE = {
    # Тут можно использовать MySQL или другой драйвер
    'drivername': 'postgresql+psycopg2',
    'host': 'localhost',
    'port': '5432',
    'username': 'root',
    'password': 'password',
    'database': 'root'
}

engine = db.create_engine(URL(**DATABASE))
connection = engine.connect()
metadata = db.MetaData()
projects = db.Table('Projects', metadata, autoload=True, autoload_with=engine)
students = db.Table('Students', metadata, autoload=True, autoload_with=engine)
faculties = db.Table('Faculties', metadata,
                     autoload=True, autoload_with=engine)
groups = db.Table('Groups', metadata, autoload=True, autoload_with=engine)
authors = db.Table('Projects_Authors', metadata,
                   autoload=True, autoload_with=engine)
query = db.select(projects)
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
dropdown_list = []

for res in ResultSet:
    dropdown_list.append(res.name)

authors_query = db.select(
    students.columns.surname,
    students.columns.name,
    students.columns.mid_name,
    groups.columns.name,
    faculties.columns.short_name
).join_from(
    authors, students
).join_from(students, groups
).join_from(groups, faculties
).where(
    authors.columns.project_id == ResultSet[0].id)

authors_set = connection.execute(authors_query).fetchall()

columns = ['Фамилия','Имя','Отчество','Группа','Факультет']
authors_df = pd.DataFrame(authors_set,columns=columns)

app = Dash(__name__)
app.layout = html.Div([
    dcc.Dropdown(dropdown_list, dropdown_list[0], id='demo-dropdown'),
    html.Div(dash_table.DataTable(authors_df.to_dict('records')),id='dd-output-table')
])


@app.callback(
    dash.dependencies.Output('dd-output-table', 'children'),
    [dash.dependencies.Input('demo-dropdown', 'value')]
)
def update_output(value):
    res_index = dropdown_list.index(value)
    authors_query = db.select(
        students.columns.surname,
        students.columns.name,
        students.columns.mid_name,
        groups.columns.name,
        faculties.columns.short_name
    ).join_from(
        authors, students
    ).join_from(students, groups
    ).join_from(groups, faculties
    ).where(
        authors.columns.project_id == ResultSet[res_index].id)

    authors_set = connection.execute(authors_query).fetchall()

    columns = ['Фамилия','Имя','Отчество','Группа','Факультет']
    authors_df = pd.DataFrame(authors_set,columns=columns)
    return [dash_table.DataTable(authors_df.to_dict('records'))]
if __name__ == '__main__':
    app.run_server(debug=True)
