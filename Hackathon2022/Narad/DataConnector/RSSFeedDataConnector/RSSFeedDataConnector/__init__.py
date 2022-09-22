import logging
import datetime
import json
import os
import sys
import azure.functions as func
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
import log_sender
import feed_parser

customer_id = os.environ['LogAnalyticsWorkspaceID']
shared_key = os.environ['LogAnalyticsSharedKey']
feed_url = os.environ['ThreatFeedURL']
log_type = 'ThreatNewsFeed'
log_analytics_uri = ''

def main(mytimer: func.TimerRequest) -> None:

    la_uri = log_sender.build_log_analytics_uri(customer_id, log_analytics_uri)
    feed = feed_parser.get_feed(feed_url)
    entries = feed_parser.get_feed_entries(feed)

    for entry in entries:
        #published_timestamp = feed_parser.convert_to_epoch(feed_parser.get_feed_entry_published(entry))
        #current_timestamp = datetime.datetime.now().timestamp()
        #if (current_timestamp - published_timestamp) <= (24*60*60):
        body = json.dumps(entries)
        log_sender.post_data(customer_id, shared_key, body, log_type, la_uri)

    if mytimer.past_due:
        logging.info('The timer is past due!')

    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    logging.info('Python timer trigger function ran at %s', utc_timestamp)