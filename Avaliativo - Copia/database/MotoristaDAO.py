from pymongo import MongoClient
from bson.objectid import ObjectId
from database.schemas.Cliente import Cliente
from database.schemas.Corrida import Corrida
from database.schemas.Motorista import Motorista

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    # Cria um novo motorista e suas corridas associadas
    def create(self, cliente: Cliente, motorista: Motorista):
        try:
            # Documento do motorista para ser inserido no MongoDB
            motorista_doc = {
                "nome": motorista.nome,
                "nota": motorista.nota,
                "corridas": [
                    {
                        "nota": c.nota,
                        "distancia": c.distancia,
                        "valor": c.valor,
                        "passageiro": {
                            "nome": cliente.nome,
                            "documento": cliente.documento
                        }
                    } for c in motorista.corridas
                ]
            }

            # Insere o documento do motorista na coleção
            motorista_res = self.db.collection.insert_one(motorista_doc)
            motorista_id = motorista_res.inserted_id

            print(f"Motorista created with id: {motorista_id}")
            return motorista_id
        except Exception as e:
            print(f"An error occurred while creating records: {e}")
            return None

    # Lê um motorista pelo seu ID
    def read_by_id(self, id: str):
        try:
            # Busca o motorista no MongoDB usando o ObjectId
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            if res:
                print(f"Motorista encontrado: {res}")
            else:
                print("Motorista não encontrado.")
            return res
        except Exception as e:
            print(f"An error occurred while reading driver: {e}")
            return None    

    # Atualiza a nota de um motorista existente
    def update_driver(self, id: str, nova_nota: str):
        try:
            # Atualiza a nota do motorista no banco de dados
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"nota": nova_nota}}
            )

            if res.modified_count > 0:
                print(f"Nota do motorista atualizada. {res.modified_count} documento(s) modificado(s).")
                return res.modified_count
            else:
                print("Nenhuma modificação realizada.")
                return 0
        except Exception as e:
            print(f"An error occurred while updating driver: {e}")
            return None

    # Deleta um motorista pelo seu ID
    def delete_driver(self, id: str):
        try:
            # Remove o motorista pelo seu ID
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            if res.deleted_count > 0:
                print(f"Motorista deletado. {res.deleted_count} documento(s) deletado(s).")
            else:
                print("Nenhum motorista encontrado para deletar.")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting driver: {e}")
            return None
