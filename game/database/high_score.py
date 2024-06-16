import orm_sqlite  

class High_score_model(orm_sqlite.Model):
    id = orm_sqlite.IntegerField(primary_key=True)
    name = orm_sqlite.StringField()
    score = orm_sqlite.IntegerField()
    createdAt = orm_sqlite.StringField()