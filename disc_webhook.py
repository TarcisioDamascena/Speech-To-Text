import requests



def postWebhook(params):

    url = 'https://discord.com/api/webhooks/810624402201903174/wLOKJJKn7t-XVEmbFwjOeH4cm1dm9OBum4oOY9tJBKlUd-NccqEzlO0pbKOhGQGfdNq1'
    rawData = {
        "username": "Webhook",
        "avatar_url": "https://pbs.twimg.com/profile_images/1393537590951911425/21PUgRcQ_400x400.jpg",
        "content": params
    }

    result = requests.post(url, json = rawData)