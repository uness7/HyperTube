import internetarchive as ia

def get_video_torrents(search_title):
    if search_title:
        search_query = (
            f'title:("{search_title}") '
            'AND mediatype:movies '
            'AND format:"Archive BitTorrent"'
        )
        params = {'rows': 2}
    else:
        search_query = ('mediatype:movies AND format:"Archive BitTorrent"')
        params = {'sort': 'downloads desc','rows': 2}
    search_results = ia.search_items(search_query, params=params)
    for result in search_results:
        item_id = result['identifier']
        print(item_id)
        item = ia.get_item(item_id)
        for file in item.files:
            if file['format'] == 'Archive BitTorrent':
                print(f"Downloading: {file['name']}")
                item.download(files=[file['name']], verbose=True)
get_video_torrents("")
