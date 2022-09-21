import feed_parser
import log_sender
import json

customer_id = 'a9ac8e7e-2d85-489d-b22b-e75c4a2da1ac'
shared_key = 'fl6+8Rjm5sfkGccaQgB2fQPTGCY3ZGoPWa0+ZDAnESRVwiAbQnKIj137pHbfNugyd68nWO25cGynu/mlD+7gwg=='
log_type = 'ThreatNewsFeed'
log_analytics_uri = ''
la_uri = log_sender.build_log_analytics_uri(customer_id, log_analytics_uri)

#feed = feed_parser.get_feed('https://feeds.feedburner.com/TheHackersNews')
feed = feed_parser.get_feed('https://www.darkreading.com/rss.xml')
entries = feed_parser.get_feed_entries(feed)

for entry in entries:
    body = json.dumps(entries, )
    log_sender.post_data(customer_id, shared_key, body, log_type, la_uri)