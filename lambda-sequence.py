def lambda_handler(event, context):
    
    from os import environ
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    from datetime import datetime

    client = WebClient(token=environ['SLACK_TOKEN'])
    lunch_list = ["とんかつ","牛かつ","お寿司","ラーメン","弁当"]
    today = datetime.now() 
    start_day = datetime(2022,3,8)

    try:
        response = client.chat_postMessage(
            channel=environ['SLACK_CHANNEL'],
            text=f"Today's lunch {(lunch_list[ (today-start_day).days % len(lunch_list) ])}!")
        print(response)
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["error"]    # str like 'invalid_auth', 'channel_not_found'
    return 0