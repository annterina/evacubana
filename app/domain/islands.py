from app.domain.models.island import Island
from app.repository.islands import Islands as IslandsRepository


class Islands:
    def __init__(self, repository: IslandsRepository) -> None:
        self.__repository = repository

    def get_all(self):
        return self.__repository.get_all()

    def get_seeds(self):
        seeds = self.__repository.get_seeds() or []
        return [int(seed['seed']) for seed in seeds]

    def get_island(self, seed: int):
        return self.__repository.get_island(seed)

    def create_island(self, island: Island):
        return self.__repository.create_island(island.model_dump())

    def update_island(self, island: Island):
        return self.__repository.update_island(island.model_dump())
