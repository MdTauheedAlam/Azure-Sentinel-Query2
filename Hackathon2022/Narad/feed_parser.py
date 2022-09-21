import feedparser

def get_feed(url):
    feed = feedparser.parse(url)
    return feed

def get_feed_entries(feed):
    if 'entries' in feed:
        return feed['entries']

def get_feed_entry_title(entry):
    if 'title' in entry:
        return entry['title']

def get_feed_entry_link(entry):
    if 'link' in entry:
        return entry['link']

def get_feed_entry_summary(entry):
    if 'summary' in entry:
        return entry['summary']

def get_feed_entry_published(entry):
    if 'published' in entry:
        return entry['published']

def get_feed_entry_published_parsed(entry):
    if 'published_parsed' in entry:
        return entry['published_parsed']

def get_feed_entry_updated(entry):
    if 'updated' in entry:
        return entry['updated']

def get_feed_entry_updated_parsed(entry):
    if 'updated_parsed' in entry:
        return entry['updated_parsed']

def get_feed_entry_id(entry):
    if 'id' in entry:
        return entry['id']

def get_feed_entry_guidislink(entry):
    if 'guidislink' in entry:
        return entry['guidislink']

def get_feed_entry_tags(entry):
    if 'tags' in entry:
        return entry['tags']

def get_feed_entry_links(entry):
    if 'links' in entry:
        return entry['links']

def get_feed_entry_author(entry):
    if 'author' in entry:
        return entry['author']

def get_feed_entry_author_detail(entry):
    if 'author_detail' in entry:
        return entry['author_detail']

def get_feed_entry_comments(entry):
    if 'comments' in entry:
        return entry['comments']

def get_feed_entry_source(entry):
    if 'source' in entry:
        return entry['source']

def get_feed_entry_enclosures(entry):
    if 'enclosures' in entry:
        return entry['enclosures']
    
def get_feed_entry_media_content(entry):
    if 'media_content' in entry:
        return entry['media_content']

def get_feed_entry_media_thumbnail(entry):
    if 'media_thumbnail' in entry:
        return entry['media_thumbnail']

def get_feed_entry_media_credit(entry):
    if 'media_credit' in entry:
        return entry['media_credit']

def get_feed_entry_media_description(entry):
    if 'media_description' in entry:
        return entry['media_description']

def get_feed_entry_media_keywords(entry):
    if 'media_keywords' in entry:
        return entry['media_keywords']

def get_feed_entry_media_title(entry):
    if 'media_title' in entry:
        return entry['media_title']

def get_feed_entry_media_category(entry):
    if 'media_category' in entry:
        return entry['media_category']

def get_feed_entry_media_credit(entry):
    if 'media_credit' in entry:
        return entry['media_credit']

if __name__ == '__main__':
    feed = get_feed('https://feeds.feedburner.com/TheHackersNews')
    entries = get_feed_entries(feed)
    #for entry in entries:
    #    print(get_feed_entry_title(entry))
    #    print(get_feed_entry_link(entry))
    #    print(get_feed_entry_summary(entry))
    #    print(get_feed_entry_published(entry))
    #    print(get_feed_entry_published_parsed(entry))
    #    print(get_feed_entry_updated(entry))
    #    print(get_feed_entry_updated_parsed(entry))
    #    print(get_feed_entry_id(entry))
    #    print(get_feed_entry_guidislink(entry))
    #    print(get_feed_entry_tags(entry))
    #    print(get_feed_entry_links(entry))
    #    print(get_feed_entry_author(entry))
    #    print(get_feed_entry_author_detail(entry))
    #    print(get_feed_entry_comments(entry))
    #    print(get_feed_entry_source(entry))
    #    print(get_feed_entry_enclosures(entry))
    #    print(get_feed_entry_media_content(entry))
    #    print(get_feed_entry_media_thumbnail(entry))
    #    print(get_feed_entry_media_credit(entry))
    #    print(get_feed_entry_media_description(entry))
    #    print(get_feed_entry_media_keywords(entry))
    #    print(get_feed_entry_media_title(entry))
    #    print(get_feed_entry_media_category(entry))
    #    print(get_feed_entry_media_credit(entry))

