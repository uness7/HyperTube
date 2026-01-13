import bencodepy
import hashlib
import os
import requests

with open('dobba_graphics/dobba_graphics_archive.torrent', 'rb') as file:
    metadata = bencodepy.decode(file.read())
    print(metadata[b'announce'].decode('utf-8'))

info_dict = metadata[b'info']
info_bencoded = bencodepy.encode(info_dict)
info_hash = hashlib.sha1(info_bencoded).digest()

print(info_hash)

total_size = 0
if b'files' in info_dict:
    for file in info_dict[b'files']:
        total_size += file[b'length']
else:
    total_size = info_dict[b'length']

params = {
    'info_hash': info_hash,       # The tracker identifies the file by this
    'peer_id': b'-PC0001-' + os.urandom(12), # A fake 20-byte ID
    'port': 6881,                 # Standard BitTorrent port
    'uploaded': 0,
    'downloaded': 0,
    'left': total_size,
    'compact': 1                  # Request a compact list of peers (saves bandwidth)
}

# 5. Send the Request
tracker_url = metadata[b'announce'].decode('utf-8')
print(f"Contacting tracker: {tracker_url}")

response = requests.get(tracker_url, params=params)

print(f"Status Code: {response.status_code}")
print(f"Response Content: {response.content}")
