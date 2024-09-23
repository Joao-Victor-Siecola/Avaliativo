from database.database import Database
from cli import PersonCLI
from database.MotoristaDAO import MotoristaDAO

db = Database(database="Corrida", collection="Motoristas")
motoristaSchema = MotoristaDAO(database=db)

personCLI = PersonCLI(motoristaSchema)
personCLI.run()
