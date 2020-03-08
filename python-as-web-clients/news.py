from urllib.request import urlopen


def news(url, topics):
    response = urlopen(url)
    html = response.read()
    content = html.decode().lower()
    for topic in topics:
        n = content.count(topic)
        print('{} appears {} times'.format(topic, n))
