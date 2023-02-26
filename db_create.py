import sqlalchemy as sa

engine = sa.create_engine('sqlite:///sqlite3.db')
connection = engine.connect()
metadata = sa.MetaData()

products = sa.Table('products', metadata,
                    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column('price', sa.Integer),
                    sa.Column('name', sa.Text),
                    )

metadata.create_all(engine)
