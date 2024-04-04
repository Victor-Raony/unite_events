import uuid
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse


class EventHandler: 
  def __init__(self) -> None:
    self.__events_respositry = EventsRepository()
  
  def register(self, http_request) -> HttpResponse:
      body = http_request.body
      body["uuid"] = str(uuid.uuid4())
      self.__events_respositry.insert_event(body)
      
      return HttpResponse(
        body={ "eventId" : body["uuid"]},
        status_code=200
      )
  
  def find_by_id(self, http_request: HttpRequest) -> HttpResponse:
      event_id = http_request.param["event_id"]
      event = self.__events_respositry.get_eventy_by_id(event_id)
      if not event: raise Exception("Evento nao encontrado")
      
      return HttpResponse(
          body={
              "event": {
                  "id": event.id,
                  "title": event.title,
                  "details": event.details,
                  "slug": event.slug,
                  "maximum_attendees": event.maximum_attendees
                }
          },
          status_code=200
      )   