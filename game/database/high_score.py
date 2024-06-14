import orm_sqlite  

class High_score(orm_sqlite.Model):
    id = orm_sqlite.IntegerField(primary_key=True)
    name = orm_sqlite.StringField()
    time = orm_sqlite.FloatField()
    level = orm_sqlite.IntegerField()
    createdAt = orm_sqlite.StringField()