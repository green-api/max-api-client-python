from typing import Optional, TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApi


class ServiceMethods:
    def __init__(self, api: "GreenApi"):
        self.api = api

    def checkAccount(self, phoneNumber: int) -> Response:
        """
        The method checks MAX account availability on a phone
        number.

        https://green-api.com/v3/docs/api/service/CheckAccount/
        """

        request_body = locals()
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "checkAccount/{{apiTokenInstance}}"
            ), request_body
        )

    def getAvatar(self, chatId: str) -> Response:
        """
        The method returns a user or a group chat avatar.

        https://green-api.com/v3/docs/api/service/GetAvatar/
        """

        request_body = locals()
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "getAvatar/{{apiTokenInstance}}"
            ), request_body
        )

    def getContacts(self) -> Response:
        """
        The method is aimed for getting a list of the current account
        contacts.

        https://green-api.com/v3/docs/api/service/GetContacts/
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "getContacts/{{apiTokenInstance}}"
            )
        )

    def getContactInfo(self, chatId: str) -> Response:
        """
        The method is aimed for getting information on a contact.

        https://green-api.com/v3/docs/api/service/GetContactInfo/
        """

        request_body = locals()
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "getContactInfo/{{apiTokenInstance}}"
            ), request_body
        )