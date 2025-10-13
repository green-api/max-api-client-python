from max_api_client_python import API

greenAPI = API.GreenAPI(
    "3100000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)


def main():
    settings = {
        "webhookUrl": "https://webhook.url",
        "webhookUrlToken": "auth_token",
        "delaySendMessagesMilliseconds": 5000,
        "markIncomingMessagesReaded": "yes",
        "markIncomingMessagesReadedOnReply": "yes",
        "outgoingWebhook": "yes",
        "outgoingMessageWebhook": "yes",
        "outgoingAPIMessageWebhook": "yes",
        "stateWebhook": "yes",
        "incomingWebhook": "yes"
    }

    response = greenAPI.account.setSettings(settings)
    print(response.data)


if __name__ == '__main__':
    main()
