import struct
import socket

# This is the raw 'peers' string from your response dictionary
peers_raw = b'i\x9d;(\x1a\xe1'

def decode_peers(peers_bytes):
    peers_list = []
    # Step by 6 bytes at a time
    for i in range(0, len(peers_bytes), 6):
        chunk = peers_bytes[i:i+6]
        if len(chunk) < 6:
            break

        # Unpack: 4 bytes (IP), 2 bytes (Port, big-endian '>')
        ip_part, port_part = struct.unpack('>4sH', chunk)

        # Convert binary IP to string (e.g., b'\x7f\x00\x00\x01' -> '127.0.0.1')
        ip_str = socket.inet_ntoa(ip_part)

        peers_list.append((ip_str, port_part))

    return peers_list

print(decode_peers(peers_raw))
# Output: [('105.157.59.40', 6881)]
