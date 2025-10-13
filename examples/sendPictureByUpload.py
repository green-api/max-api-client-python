from max_api_client_python import API

greenAPI = API.GreenAPI(
    "3100000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)


def main():
    response = greenAPI.sending.sendFileByUpload(
        "10000000",
        "data/rates.png",
        "rates.png",
        "Available rates"
    )

    print(response.data)


if __name__ == '__main__':
    main()
