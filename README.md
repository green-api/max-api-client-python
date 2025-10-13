# max-api-client-python

![](https://img.shields.io/badge/license-CC%20BY--ND%204.0-green)
![](https://img.shields.io/pypi/status/max-api-client-python)
![](https://img.shields.io/pypi/pyversions/max-api-client-python)
![](https://img.shields.io/github/actions/workflow/status/green-api/max-api-client-python/python-package.yml)
![](https://img.shields.io/pypi/dm/max-api-client-python)

## Поддержка

[![Support](https://img.shields.io/badge/support@green--api.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:support@green-api.com)
[![Support](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/greenapi_support_ru_bot)
[![Support](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/79993331223)

## Руководства и новости

[![Guides](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@green-api)
[![News](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/green_api)
[![News](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://whatsapp.com/channel/0029VaHUM5TBA1f7cG29nO1C)

max-api-client-python - библиотека для интеграции с мессенджером MAX через API сервиса [green-api.com](https://green-api.com/max). Чтобы воспользоваться библиотекой, нужно получить регистрационный токен и ID аккаунта в [личном кабинете](https://console.green-api.com/). Есть бесплатный тариф аккаунта разработчика.

## API

Документация к REST API находится по [ссылке](https://green-api.com/v3/docs/api/). Библиотека является обёрткой к REST API,
поэтому документация по ссылке выше применима и к самой библиотеке.

## Авторизация

Чтобы отправить сообщение или выполнить другие методы GREEN API, аккаунт MAX в приложении телефона должен быть в авторизованном состоянии. Для авторизации аккаунта перейдите в [личный кабинет](https://console.green-api.com/), запросите SMS код. Введите SMS код, после чего инстанс будет авторизован.

## Установка

```shell
python -m pip install max-api-client-python
```

## Импорт

```
from max_api_client_python import API
```

## Примеры

### Как инициализировать объект

```
greenAPI = API.GreenAPI(
    "3100000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)
```

### Отправка текстового сообщения на номер MAX

Ссылка на пример: [sendTextMessage.py](../examples/sendTextMessage.py).

```
response = greenAPI.sending.sendMessage("10000000", "Message text")

print(response.data)
```

### Отправка картинки по URL

Ссылка на пример: [sendPictureByLink.py](../examples/sendPictureByLink.py).

```
response = greenAPI.sending.sendFileByUrl(
    "10000000",
    "https://download.samplelib.com/png/sample-clouds2-400x300.png",
    "sample-clouds2-400x300.png",
    "Sample PNG"
)

print(response.data)
```

### Отправка картинки загрузкой с диска

Ссылка на пример: [sendPictureByUpload.py](../examples/sendPictureByUpload.py).

```
response = greenAPI.sending.sendFileByUpload(
    "10000000",
    "data/rates.png",
    "rates.png",
    "Available rates"
)

print(response.data)
```

### Создание группы и отправка сообщения в эту группу

Ссылка на пример: [createGroupAndSendMessage.py](../examples/createGroupAndSendMessage.py).

```
create_group_response = greenAPI.groups.createGroup(
    "Group Name", ["10000000"]
)
if create_group_response.code == 200:
    send_message_response = greenAPI.sending.sendMessage(
        create_group_response.data["chatId"], "Message text"
    )
```

### Получение входящих уведомлений через HTTP API

Ссылка на пример: [receiveNotification.py](../examples/receiveNotification.py).

Общая концепция получения данных в GREEN API описана [здесь](https://green-api.com/v3/docs/api/receiving/). Для старта
получения уведомлений через HTTP API требуется выполнить метод библиотеки:

```
greenAPI.webhooks.startReceivingNotifications(onEvent)
```

onEvent - ваша функция, которая должен содержать параметры:

| Параметр    | Описание                          |
|-------------|-----------------------------------|
| typeWebhook | тип полученного уведомления (str) |
| body        | тело уведомления (dict)           |

Типы и форматы тел уведомлений находятся [здесь](https://green-api.com/v3/docs/api/receiving/notifications-format/).

Эта функция будет вызываться при получении входящего уведомления. Далее обрабатываете уведомления согласно бизнес-логике
вашей системы.


## Список примеров

| Описание                                             | Модуль                                                                   |
|------------------------------------------------------|--------------------------------------------------------------------------|
| Пример отправки текста                               | [sendTextMessage.py](../examples/sendTextMessage.py)                     |
| Пример отправки картинки по URL                      | [sendPictureByLink.py](../examples/sendPictureByLink.py)                 |
| Пример отправки картинки загрузкой с диска           | [sendPictureByUpload.py](../examples/sendPictureByUpload.py)             |
| Пример создание группы и отправка сообщения в группу | [createGroupAndSendMessage.py](../examples/createGroupAndSendMessage.py) |
| Пример получения входящих уведомлений                | [receiveNotification.py](../examples/receiveNotification.py)             |
| Пример создания инстанса                            | [createInstance.py](https://github.com/green-api/max-api-client-python/blob/master/examples/partherMethods/CreateInstance.py)                          |

## Полный список методов библиотеки

| Метод API                              | Описание                                                                                                                  | Ссылка на документацию                                                                                       |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| `account.getSettings`                  | Метод предназначен для получения текущих настроек аккаунта                                                                | [GetSettings](https://green-api.com/v3/docs/api/account/GetSettings/)                                       |
| `account.getAccountSettings`                | Метод предназначен для получения информации о аккаунте MAX                                                           | [GetAccountSettings](https://green-api.com/v3/docs/api/account/GetAccountSettings/)                                   |
| `account.setSettings`                  | Метод предназначен для установки настроек аккаунта                                                                        | [SetSettings](https://green-api.com/v3/docs/api/account/SetSettings/)                                       |
| `account.getStateInstance`             | Метод предназначен для получения состояния аккаунта                                                                       | [GetStateInstance](https://green-api.com/v3/docs/api/account/GetStateInstance/)                             |
| `account.getStatusInstance`            | Метод предназначен для получения состояния сокета соединения инстанса аккаунта с MAX                                 | [GetStatusInstance](https://green-api.com/v3/docs/api/account/GetStatusInstance/)                           |
| `account.reboot`                       | Метод предназначен для перезапуска аккаунта                                                                               | [Reboot](https://green-api.com/v3/docs/api/account/Reboot/)                                                 |
| `account.logout`                       | Метод предназначен для разлогинивания аккаунта                                                                            | [Logout](https://green-api.com/v3/docs/api/account/Logout/)                                                 |
| `account.setProfilePicture`            | Метод предназначен для установки аватара аккаунта                                                                         | [SetProfilePicture](https://green-api.com/v3/docs/api/account/SetProfilePicture/)                           |
| `account.startAuthorization`         | Метод предназначен для запроса кода для авторизации                                                            | [StartAuthorization](https://green-api.com/v3/docs/api/account/StartAuthorization/)                     |
| `account.sendAuthorizationCode`         | Метод предназначен для авторизации инстанса по номеру телефона                                                            | [SendAuthorizationCode](https://green-api.com/v3/docs/api/account/SendAuthorizationCode/)                     |
| `groups.createGroup`                   | Метод предназначен для создания группового чата                                                                           | [CreateGroup](https://green-api.com/v3/docs/api/groups/CreateGroup/)                                        |
| `groups.updateGroupName`               | Метод изменяет наименование группового чата                                                                               | [UpdateGroupName](https://green-api.com/v3/docs/api/groups/UpdateGroupName/)                                |
| `groups.getGroupData`                  | Метод получает данные группового чата                                                                                     | [GetGroupData](https://green-api.com/v3/docs/api/groups/GetGroupData/)                                      |
| `groups.addGroupParticipant`           | Метод добавляет участника в групповой чат                                                                                 | [AddGroupParticipant](https://green-api.com/v3/docs/api/groups/AddGroupParticipant/)                        |
| `groups.removeGroupParticipant`        | Метод удаляет участника из группового чата                                                                                | [RemoveGroupParticipant](https://green-api.com/v3/docs/api/groups/RemoveGroupParticipant/)                  |
| `groups.setGroupAdmin`                 | Метод назначает участника группового чата администратором                                                                 | [SetGroupAdmin](https://green-api.com/v3/docs/api/groups/SetGroupAdmin/)                                    |
| `groups.removeAdmin`                   | Метод лишает участника прав администрирования группового чата                                                             | [RemoveAdmin](https://green-api.com/v3/docs/api/groups/RemoveAdmin/)                                        |
| `groups.setGroupPicture`               | Метод устанавливает аватар группы                                                                                         | [SetGroupPicture](https://green-api.com/v3/docs/api/groups/SetGroupPicture/)                                |
| `groups.leaveGroup`                    | Метод производит выход пользователя текущего аккаунта из группового чата                                                  | [LeaveGroup](https://green-api.com/v3/docs/api/groups/LeaveGroup/)                                          |
| `journals.getChatHistory`              | Метод возвращает историю сообщений чата                                                                                   | [GetChatHistory](https://green-api.com/v3/docs/api/journals/GetChatHistory/)                                |
| `journals.getMessage`                  | Метод возвращает сообщение чата                                                                                           | [GetMessage](https://green-api.com/v3/docs/api/journals/GetMessage/)                                        |       
| `journals.lastIncomingMessages`        | Метод возвращает крайние входящие сообщения аккаунта                                                                      | [LastIncomingMessages](https://green-api.com/v3/docs/api/journals/LastIncomingMessages/)                    |
| `journals.lastOutgoingMessages`        | Метод возвращает крайние отправленные сообщения аккаунта                                                                  | [LastOutgoingMessages](https://green-api.com/v3/docs/api/journals/LastOutgoingMessages/)                    |
| `journals.getChats`        | Метод возвращает список чатов аккаунта                                                                  | [GetChats](https://green-api.com/v3/docs/api/journals/getChats/)                    |
| `queues.showMessagesQueue`             | Метод предназначен для получения списка сообщений, находящихся в очереди на отправку                                      | [ShowMessagesQueue](https://green-api.com/v3/docs/api/queues/ShowMessagesQueue/)                            |
| `queues.clearMessagesQueue`            | Метод предназначен для очистки очереди сообщений на отправку                                                              | [ClearMessagesQueue](https://green-api.com/v3/docs/api/queues/ClearMessagesQueue/)                          |
| `marking.readChat`                     | Метод предназначен для отметки сообщений в чате прочитанными                                                              | [ReadChat](https://green-api.com/v3/docs/api/marks/ReadChat/)                                               |
| `receiving.receiveNotification`        | Метод предназначен для получения одного входящего уведомления из очереди уведомлений                                      | [ReceiveNotification](https://green-api.com/v3/docs/api/receiving/technology-http-api/ReceiveNotification/) |
| `receiving.deleteNotification`         | Метод предназначен для удаления входящего уведомления из очереди уведомлений                                              | [DeleteNotification](https://green-api.com/v3/docs/api/receiving/technology-http-api/DeleteNotification/)   |
| `receiving.downloadFile`               | Метод предназначен для скачивания принятых и отправленных файлов                                                          | [DownloadFile](https://green-api.com/v3/docs/api/receiving/files/DownloadFile/)                             |
| `sending.sendMessage`                  | Метод предназначен для отправки текстового сообщения в личный или групповой чат                                           | [SendMessage](https://green-api.com/v3/docs/api/sending/SendMessage/)                                       |
| `sending.sendFileByUpload`             | Метод предназначен для отправки файла, загружаемого через форму (form-data)                                               | [SendFileByUpload](https://green-api.com/v3/docs/api/sending/SendFileByUpload/)                             |
| `sending.sendFileByUrl`                | Метод предназначен для отправки файла, загружаемого по ссылке                                                             | [SendFileByUrl](https://green-api.com/v3/docs/api/sending/SendFileByUrl/)                                   |
| `sending.uploadFile`                   | Метод предназначен для загрузки файла в облачное хранилище, который можно отправить методом sendFileByUrl                 | [UploadFile](https://green-api.com/v3/docs/api/sending/UploadFile/)                                         |
| `serviceMethods.checkAccount`         | Метод проверяет наличие аккаунта MAX на номере телефона                                                              | [CheckAccount](https://green-api.com/v3/docs/api/service/CheckAccount/)                                   |
| `serviceMethods.getAvatar`             | Метод возвращает аватар корреспондента или группового чата                                                                | [GetAvatar](https://green-api.com/v3/docs/api/service/GetAvatar/)                                           |
| `serviceMethods.getContacts`           | Метод предназначен для получения списка контактов текущего аккаунта                                                       | [GetContacts](https://green-api.com/v3/docs/api/service/GetContacts/)                                       |
| `serviceMethods.getContactInfo`        | Метод предназначен для получения информации о контакте                                                                    | [GetContactInfo](https://green-api.com/v3/docs/api/service/GetContactInfo/)                                 |
| `webhooks.startReceivingNotifications` | Метод предназначен для старта получения новых уведомлений                                                                 |                                                                                                          |
| `webhooks.stopReceivingNotifications`  | Метод предназначен для остановки получения новых уведомлений                                                              |                                                                                                          |
| `partner.GetInstances`   | Метод предназначен для получения всех инстансов аккаунтов созданных партнёром.                                           | [GetInstances](https://green-api.com/v3/docs/partners/getInstances/)                       |
| `partner.CreateInstance`   | Метод предназначен для создания инстанса от имени партнёра.                                           | [CreateInstance](https://green-api.com/v3/docs/partners/createInstance/)                       |
| `partner.DeleteInstanceAccount`   | Метод предназначен для удаления инстанса аккаунта партнёра.                                           | [DeleteInstanceAccount](https://green-api.com/v3/docs/partners/deleteInstanceAccount/)                       |

## Документация по методам сервиса

[https://green-api.com/v3/docs/api/](https://green-api.com/v3/docs/api/).

## Сторонние продукты

- [requests](https://requests.readthedocs.io/en/latest/) - для HTTP запросов.

## Лицензия

Лицензировано на условиях [
Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)
](https://creativecommons.org/licenses/by-nd/4.0/).
[LICENSE](../LICENSE).