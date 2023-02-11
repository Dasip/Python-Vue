__all__ = ["BaseAPIException"]

from typing import Dict, Union


class BaseAPIException(Exception):
    message: str
    status_code: int

    def attrs_to_dict(self) -> Dict[str, Union[str, int]]:
        try:
            the_type = self.__getattribute__("type")
        except AttributeError:
            the_type = self.__class__.__name__
        return {
            "type": the_type,
            "status_code": self.status_code,
            "message": self.message,
        }
