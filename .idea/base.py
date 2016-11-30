from sqlalchemy import *

db = create_engine('sqlite:///smagro.db')

db.echo = True

metadata = MetaData(db)

equip = Table('equip', metadata,
    Column('equip_id', Integer, primary_key=True, autoincrement = True),
    Column('name', String(8)),
)

equip.create()

oper = Table('oper', metadata,
    Column('oper_id', Integer, primary_key=True, autoincrement = True),
    Column('matricula', Integer),
    Column('name', String(8)),
)

oper.create()

medicao = Table('medicao', metadata,
    Column('medicao_id', Integer, primary_key=True, autoincrement = True),
    Column('medicao_ini', Time),
    Column('medicao_fim', Time),
    Column('data', DateTime),
)
medicao.create()

imple = Table('imple', metadata,
    Column('imple_id', Integer, primary_key=True, autoincrement = True),
    Column('imple1', String(4)),
    Column('imple2', String(4)),
)

imple.create()

prop = Table('prop', metadata,
    Column('prop_id', Integer, primary_key=True, autoincrement = True),
    Column('descricao', String(50)),
)

prop.create()

mparada = Table('mparada', metadata,
    Column('mparada_id', Integer, primary_key=True, autoincrement = True),
    Column('descricao', String(50)),
    Column('data', DateTime),
)
mparada.create()

