import orm_sqlite  
from .high_score import High_score

db = orm_sqlite.Database('game/database/database.db')

High_score.objects.backend = db