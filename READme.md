## Как запустить

1. Запустить докер контейнер командой docker
```bash
docker run -p 8000:8000 kikijjx/vk-user-parser
```


## Как пользоваться - вариант 1

1. Зайти по [адресу](http://127.0.0.1:8000/docs)
2. Открыть маршрут /data
3. Получить [токен VK API](https://vkhost.github.io) и указать его в поле token.
4. Получить [ID пользователя](https://regvk.com/id/) и указать его в поле user_id.
5. Нажать execute

## Как пользоваться - вариант 2

1. Зайти по адресу
```bash
http://127.0.0.1:8000/data?token={token}&user_id={id}
```
где:
- {token} — [токен VK API](https://vkhost.github.io).
- {id} — [ID пользователя](https://regvk.com/id/).

## Пример ответа

```bash
{
    "user_info": {
        "id": 1,
        "followers_count": 4750344,
        "first_name": "Павел",
        "last_name": "Дуров",
        "can_access_closed": true,
        "is_closed": false
    },
    "followers": [
        175483533,
        291932031,
        292748284,
    ],
    "subscriptions": []
}
```