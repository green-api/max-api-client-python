import mimetypes
import pathlib
from typing import Dict, List, Optional, TYPE_CHECKING, Union

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApi


class Sending:
    def __init__(self, api: "GreenApi"):
        self.api = api

    def sendMessage(
            self,
            chatId: str,
            message: str,
            quotedMessageId: Optional[str] = None,
            archiveChat: Optional[bool] = None,
            linkPreview: Optional[bool] = None
    ) -> Response:
        """
        The method is aimed for sending a text message to a personal or
        a group chat.

        https://green-api.com/v3/docs/api/sending/SendMessage/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "sendMessage/{{apiTokenInstance}}"
            ), request_body
        )

    def sendFileByUpload(
            self,
            chatId: str,
            path: str,
            fileName: Optional[str] = None,
            caption: Optional[str] = None,
            quotedMessageId: Optional[str] = None
    ) -> Response:
        """
        The method is aimed for sending a file uploaded by form
        (form-data).

        https://green-api.com/v3/docs/api/sending/SendFileByUpload/
        """

        request_body = self.__handle_parameters(locals())

        file_name = pathlib.Path(path).name
        content_type = mimetypes.guess_type(file_name)[0]

        files = {"file": (file_name, open(path, "rb"), content_type)}

        request_body.pop("path")

        return self.api.request(
            "POST", (
                "{{media}}/waInstance{{idInstance}}/"
                "sendFileByUpload/{{apiTokenInstance}}"
            ), request_body, files
        )

    def sendFileByUrl(
            self,
            chatId: str,
            urlFile: str,
            fileName: str,
            caption: Optional[str] = None,
            quotedMessageId: Optional[str] = None,
            archiveChat: Optional[bool] = None
    ) -> Response:
        """
        The method is aimed for sending a file uploaded by URL.

        https://green-api.com/v3/docs/api/sending/SendFileByUrl/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "sendFileByUrl/{{apiTokenInstance}}"
            ), request_body
        )

    def uploadFile(self, path: str) -> Response:
        """
        The method is designed to upload a file to the cloud storage,
        which can be sent using the sendFileByUrl method.

        https://green-api.com/v3/docs/api/sending/UploadFile/
        """

        file_name = pathlib.Path(path).name
        content_type = mimetypes.guess_type(file_name)[0]

        with open(path, "rb") as file:
            return self.api.raw_request(
                method="POST",
                url=(
                    f"{self.api.media}/waInstance{self.api.idInstance}/"
                    f"uploadFile/{self.api.apiTokenInstance}"
                ),
                data=file.read(),
                headers={"Content-Type": content_type,
                         "GA-Filename": file_name}
            )

    @classmethod
    def __handle_parameters(cls, parameters: dict) -> dict:
        handled_parameters = parameters.copy()

        handled_parameters.pop("self")

        for key, value in parameters.items():
            if value is None:
                handled_parameters.pop(key)

        return handled_parameters
