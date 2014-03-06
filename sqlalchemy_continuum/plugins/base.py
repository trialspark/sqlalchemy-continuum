class Plugin(object):
    def __init__(self, manager):
        self.manager = manager

    def after_build_tx_class(self):
        pass

    def after_build_history_table_columns(self, table_builder, columns):
        pass

    def before_flush(self, uow, session):
        pass

    def before_create_history_objects(self, uow, session):
        pass

    def after_create_history_objects(self, uow, session):
        pass

    def after_create_history_object(self, uow, parent_obj, history_obj):
        pass

    def before_create_tx_object(self, uow, session):
        pass

    def after_create_tx_object(self, uow, session):
        pass

    def after_history_class_built(self, parent_cls, history_cls):
        pass

    def after_construct_changeset(self, history_obj, changeset):
        pass

    def __repr__(self):
        return '<%s>' % self.__class__.__name__


class ModelFactory(object):
    model_name = None

    def __init__(self, manager):
        self.manager = manager

    def __call__(self):
        """
        Create model class but only if it doesn't already exist
        in declarative model registry.
        """
        registry = self.manager.declarative_base._decl_class_registry
        if self.model_name not in registry:
            return self.create_class()
        return registry[self.model_name]