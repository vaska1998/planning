import uuid
from typing import TypeVar, List, Optional, Type

from src.domain.model.entity import AppEntity
from src.domain.repository.base import Repository, AppQuery
from src.infrastructure.repository.peewee.engine import PeeweeEngine

Entity = TypeVar('Entity', bound=AppEntity)


class PeeweeRepository(Repository[Entity]):
    def __init__(self, engine: PeeweeEngine, entity_class: Type[Entity]):
        self.engine = engine
        self.entity_class = entity_class
        self.engine.connect()

    def get(self, entity_id: int) -> Optional[Entity]:
        return self.entity_class.get_or_none(self.entity_class.id == entity_id)

    def get_by_filter(self, filter_obj: AppQuery[Entity]) -> Optional[Entity]:
        query = self._apply_app_query(self.entity_class.select(), filter_obj)
        return query.get_or_none()

    def find(self, filter_obj: AppQuery[Entity]) -> List[Entity]:
        query = self._apply_app_query(self.entity_class.select(), filter_obj)
        return list(query)

    def get_all(self) -> List[Entity]:
        return list(self.entity_class.select())

    def count(self, filter_obj: AppQuery[Entity] = None) -> int:
        query = self._apply_app_query(self.entity_class.select(), filter_obj)
        return query.count()

    def add(self, entity: Entity) -> Entity:
        entity.save()
        return entity

    def update(self, entity: Entity) -> Entity:
        entity.save()
        return entity

    def delete(self, entity: Entity) -> Entity:
        entity.delete_instance()
        return entity

    def _apply_app_query(self, query, app_query: AppQuery = None):
        if not app_query:
            return query

        app_filter = app_query.filters
        app_orders = app_query.orders
        app_pagination = app_query.pagination

        if app_filter:
            for filter_ in app_filter:
                query = query.where(filter_.condition(self.entity_class))

        if app_orders:
            for order in app_orders:
                sql_order = self.entity_class._meta.fields[order.param]
                query = query.order_by(-sql_order if order.direction == 'desc' else sql_order)

        if app_pagination:
            query = query.limit(app_pagination.limit).offset(app_pagination.skip)

        return query
