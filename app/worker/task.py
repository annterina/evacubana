from celery.app import Celery

from app.configuration.db import initialize_db
from app.domain.islands import Islands
from app.domain.models.island import Island
from app.repository.islands import Islands as IslandRepository
from app.service.islands_service import MAX_ISLAND_NOTES

app = Celery(__name__, broker='sqs://')
app.conf.broker_transport_options = {'region': 'eu-north-1'}

db = initialize_db()
repository = IslandRepository(db)
islands = Islands(repository)

SHARE_OF_NOTES = 0.3
SHARE_OF_ISLANDS_WITH_FEW_NOTES = 0.5


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, spawn_island.s(), name='spawn new island')


def has_few_notes(island):
    return len(island.get('notes')) < SHARE_OF_NOTES * MAX_ISLAND_NOTES


def enough_islands_with_few_notes(islands_with_few_notes, all_playable_islands):
    return len(islands_with_few_notes) >= SHARE_OF_ISLANDS_WITH_FEW_NOTES * len(all_playable_islands)


@app.task
def spawn_island():
    playable_islands = islands.get_all_playable()
    islands_with_few_notes = list(filter(has_few_notes, playable_islands))
    if not enough_islands_with_few_notes(islands_with_few_notes, playable_islands):
        islands.create_island(Island())
        print("New island created!")
    else:
        print(f"No need for a new island! "
              f"There are {len(islands_with_few_notes)} islands with few notes "
              f"(out of all {len(playable_islands)} islands)!")
