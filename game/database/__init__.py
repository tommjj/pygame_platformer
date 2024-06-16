import orm_sqlite  
from .high_score import High_score_model

db = orm_sqlite.Database('game/database/database.db')

High_score_model.objects.backend = db