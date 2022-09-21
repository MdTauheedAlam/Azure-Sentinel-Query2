import datetime
import base64
import hashlib
import requests
import hmac
import re
import logging


def build_log_analytics_uri(customer_id, log_analytics_uri):

    if ((log_analytics_uri in (None, '') or str(log_analytics_uri).isspace())):    
        log_analytics_uri = 'https://' + customer_id + '.ods.opinsights.azure.com'

    pattern = r'https:\/\/([\w\-]+)\.ods\.opinsights\.azure.([a-zA-Z\.]+)$'
    match = re.match(pattern,str(log_analytics_uri))
    if(not match):
        raise Exception("Invalid Log Analytics Uri.")

    return log_analytics_uri

def build_signature(customer_id, shared_key, date, content_length, method, content_type, resource):
    '''
        Returns authorization header which will be used when sending data into Azure Log Analytics.    
    '''
    x_headers = 'x-ms-date:' + date
    string_to_hash = method + "\n" + str(content_length) + "\n" + content_type + "\n" + x_headers + "\n" + resource
    bytes_to_hash = bytes(string_to_hash, encoding="utf-8")
    decoded_key = base64.b64decode(shared_key)
    encoded_hash = base64.b64encode(hmac.new(decoded_key, bytes_to_hash, digestmod=hashlib.sha256).digest()).decode()
    authorization = "SharedKey {}:{}".format(customer_id,encoded_hash)
    return authorization

def post_data(customer_id, shared_key, body, log_type, log_analytics_uri):
    '''
        Sends data into Azure Log Analytics.
    '''
    method = 'POST'
    content_type = 'application/json'
    resource = '/api/logs'
    rfc1123date = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    content_length = len(body)
    signature = build_signature(customer_id, shared_key, rfc1123date, content_length, method, content_type, resource)
    uri = log_analytics_uri + resource + '?api-version=2016-04-01'

    headers = {
        'content-type': content_type,
        'Authorization': signature,
        'Log-Type': log_type,
        'x-ms-date': rfc1123date
    }
    response = requests.post(uri, data=body, headers=headers)
    if (response.status_code >= 200 and response.status_code <= 299):
        print('Accepted data:', len(body))
        logging.info("Data is processed successfully.")
    else:
        print("Response code: {}".format(response.status_code), response.text)
        logging.warning("Response code: {}".format(response.status_code))

if __name__ == "__main__":
    customer_id = 'a9ac8e7e-2d85-489d-b22b-e75c4a2da1ac'
    shared_key = 'fl6+8Rjm5sfkGccaQgB2fQPTGCY3ZGoPWa0+ZDAnESRVwiAbQnKIj137pHbfNugyd68nWO25cGynu/mlD+7gwg=='
    log_type = 'Testfeed'
    log_analytics_uri = ''
    la_uri = build_log_analytics_uri(customer_id, log_analytics_uri)
    body = '{ "records": [ { "Computer": "Meow", "Message": "Hello2" } ] }'
    post_data(customer_id, shared_key, body, log_type, la_uri)
