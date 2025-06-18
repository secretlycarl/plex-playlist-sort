"""
plexsort.py - Sort Plex playlists from the command line
"""
import argparse
from plexapi.server import PlexServer

# --- CONFIGURE YOUR SERVER ---
PLEX_BASEURL = 'http://LOCAL_IP:32400'
PLEX_TOKEN = 'token'

# --- CONNECT TO PLEX ---
plex = PlexServer(PLEX_BASEURL, PLEX_TOKEN)

# --- SORTING OPTIONS ---
SORT_KEYS = {
    'title': lambda item: item.title.lower(),
    'artist': lambda item: getattr(item, 'grandparentTitle', '').lower(),
    'album': lambda item: getattr(item, 'parentTitle', '').lower(),
    'duration': lambda item: getattr(item, 'duration', 0),
    'track': lambda item: getattr(item, 'index', 0),
    'year': lambda item: getattr(item, 'year', 0),
    'views': lambda item: getattr(item, 'viewCount', 0),
    'rating': lambda item: getattr(item, 'userRating', 0),
    'original': None  # Preserve existing order or use --reverse
}


def sort_playlist(playlist, key, descending=False, dry_run=False, backup=False, reverse=False):
    items = playlist.items()
    print(f"Loaded playlist '{playlist.title}' with {len(items)} items.")

    if key == 'original':
        if reverse:
            sorted_items = list(reversed(items))
            if dry_run:
                print("\nPreview of reversed original order:")
                for i, item in enumerate(sorted_items, 1):
                    print(f"{i:2d}. {item.title} - {getattr(item, 'grandparentTitle', 'Unknown Artist')}")
                return
            if backup:
                backup_title = f"{playlist.title} (Backup)"
                print(f"Creating backup playlist '{backup_title}'...")
                plex.createPlaylist(backup_title, items)
            print("Reversing playlist...")
            playlist.removeItems(items)
            playlist.addItems(sorted_items)
            print("Done.")
        else:
            print("Preserving original order. No sorting applied.")
        return

    sorted_items = sorted(items, key=SORT_KEYS[key], reverse=descending)

    if dry_run:
        print("\nPreview of sorted order:")
        for i, item in enumerate(sorted_items, 1):
            print(f"{i:2d}. {item.title} - {getattr(item, 'grandparentTitle', 'Unknown Artist')}")
        return

    if backup:
        backup_title = f"{playlist.title} (Backup)"
        print(f"Creating backup playlist '{backup_title}'...")
        plex.createPlaylist(backup_title, items)

    print("Reordering playlist...")
    playlist.removeItems(items)
    playlist.addItems(sorted_items)
    print("Done.")


def main():
    parser = argparse.ArgumentParser(description="Sort a Plex playlist.")
    parser.add_argument('--playlist', type=str, help='Name of the playlist to sort')
    parser.add_argument('--sort', type=str, choices=SORT_KEYS.keys(), default='title', help='Sort key')
    parser.add_argument('--desc', action='store_true', help='Sort descending')
    parser.add_argument('--reverse', action='store_true', help='Reverse the current playlist order (only with --sort original)')
    parser.add_argument('--dry-run', action='store_true', help='Show sorted order without modifying playlist')
    parser.add_argument('--backup', action='store_true', help='Create a backup of the original playlist')
    args = parser.parse_args()

    # List playlists if none specified
    if not args.playlist:
        print("Available playlists:")
        for pl in plex.playlists():
            print(f" - {pl.title}")
        return

    # Locate target playlist
    playlist = plex.playlist(args.playlist)
    sort_playlist(playlist, args.sort, args.desc, args.dry_run, args.backup, args.reverse)


if __name__ == '__main__':
    main()



if __name__ == '__main__':
    main()
