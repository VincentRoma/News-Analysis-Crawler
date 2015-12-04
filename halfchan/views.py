from django.shortcuts import render

def HalfChanViews(request):
    import urllib2
    import json
    chan_updates = []
    data = urllib2.urlopen("https://a.4cdn.org/pol/catalog.json")
    chan = json.load(data)
    threads = chan[1]['threads']
    for i in range(1,15) :
        if 'last_replies' in threads[i]:
            chan_updates.append(
                {
                    'com': threads[i]['com'],
                    'last_replies': threads[i]['last_replies'],
                    'link': 'http://boards.4chan.org/pol/thread/{}'.format(threads[i]['no']),
                    'picture': 'http://i.4cdn.org/pol/{}{}'.format(threads[i]['tim'], threads[i]['ext'])
                }
            )
        else:
            chan_updates.append(
                {
                    'com': threads[i]['com'],
                    'link': 'http://boards.4chan.org/pol/thread/{}'.format(threads[i]['no']),
                    'picture': 'http://i.4cdn.org/pol/{}{}'.format(threads[i]['tim'], threads[i]['ext'])
                }
            )
    return render(request, 'halfchan/home.html', {'chan_updates': chan_updates, 'state': 'halfchan'})
