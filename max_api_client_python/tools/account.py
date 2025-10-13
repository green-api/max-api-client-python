from pathlib import Path
from typing import Dict, TYPE_CHECKING, Union

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApi


class Account:
    def __init__(self, api: "GreenApi"):
        self.api = api

    def getSettings(self) -> Response:
        """
        The method is aimed for getting the current account settings.

        https://green-api.com/v3/docs/api/account/GetSettings/
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "getSettings/{{apiTokenInstance}}"
            )
        )

    def getAccountSettings(self) -> Response:
        """
        The method is aimed to get information about the MAX
        account.

        https://green-api.com/v3/docs/api/account/GetAccountSettings/
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "getAccountSettings/{{apiTokenInstance}}"
            )
        )

    def setSettings(self, requestBody: Dict[str, Union[int, str]]) -> Response:
        """
        The method is aimed for setting account settings.

        https://green-api.com/v3/docs/api/account/SetSettings/
        """

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "setSettings/{{apiTokenInstance}}"
            ), requestBody
        )

    def getStateInstance(self) -> Response:
        """
        The method is aimed for getting the account state.

        https://green-api.com/v3/docs/api/account/GetStateInstance/
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "getStateInstance/{{apiTokenInstance}}"
            )
        )

    def reboot(self) -> Response:
        """
        The method is aimed for rebooting an account.

        https://green-api.com/v3/docs/api/account/Reboot/
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/reboot/{{apiTokenInstance}}"
            )
        )

    def logout(self) -> Response:
        """
        The method is aimed for logging out an account.

        https://green-api.com/v3/docs/api/account/Logout/
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/logout/{{apiTokenInstance}}"
            )
        )

    def setProfilePicture(self, path: str) -> Response:
        """
        The method is aimed for setting an account picture.

        https://green-api.com/v3/docs/api/account/SetProfilePicture/
        """

        file_name = Path(path).name
        files = {"file": (file_name, open(path, "rb"), "image/jpeg")}

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "setProfilePicture/{{apiTokenInstance}}"
            ), files=files
        )

    def startAuthorization(self, phoneNumber: int) -> Response:
        """
        The method is designed to receive SMS for instance authorization.

        https://green-api.com/v3/docs/api/account/StartAuthorization/
        """

        request_body = locals()
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "startAuthorization/{{apiTokenInstance}}"
            ), request_body
        )

    def sendAuthorizationCode(self, code: str) -> Response:
        """
        The method is designed to authorize an instance by SMS.

        https://green-api.com/v3/docs/api/account/SendAuthorizationCode/
        """

        request_body = locals()
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "sendAuthorizationCode/{{apiTokenInstance}}"
            ), request_body
        )
