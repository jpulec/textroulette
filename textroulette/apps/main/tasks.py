from django_rq import job
import requests
import logging, os

from textroulette.apps.main.models import Message

logger = logging.getLogger(__name__)

@job
def check_for_messages():
    twilio_number = "+19204866139"
    account_id = "AC426f5764d2d3e0bdf9cc836097655766"
    auth_token = "dea8c817fb0cb573370a6d926ad1f07d"
    url = "https://api.twilio.com/2010-04-01/Accounts/%s/SMS/Messages.json" % account_id
    response = requests.get(url, auth=(account_id, auth_token))
    logger.info(response)
    json = response.json()
    logger.info(json)
    cur_page_num = json['page']
    while cur_page_num != json['num_pages']:
        for message in json['sms_messages']:
            logger.info(message)
            if not Message.objects.filter(id=message['sid']).exists():
                new_msg = Message(id=message['sid'])
                new_msg.save()
                to_field = message["to"]
                from_field= message["from"]
                body = message["body"]
                if to_field == twilio_number:
                    try:
                        sender = UserNumber.objects.get(phone_number=from_field[1:])
                        receiver = sender.connected
                        payload = {"From": twilio_number,
                                   "To": "+" + receiver.phone_number,
                                   "Body": body,
                                }
                        response = requests.post(url, auth=(account_id, auth_token), data=payload)
                        logger.info(response)
                    except Exception as e:
                        logger.exception(e)
        cur_page_num += 1
        if json['next_page_uri'] is not None:
            url = json['next_page_uri']
            response = requests.get(url, auth=(account_id, auth_token))
            logger.info(response)
            json = response.json()
            logger.info(json)
    return
