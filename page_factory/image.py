from page_factory.component import Component


class Image(Component):
    @property
    def type_of(self) -> str:
        return 'image'