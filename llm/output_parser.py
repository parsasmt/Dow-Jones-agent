def get_content(response):

    return response["choices"][0]["message"]["content"]


def get_reasoning(response):

    message = response["choices"][0]["message"]

    return message.get("reasoning_details", None)


def get_message(response):

    return response["choices"][0]["message"]