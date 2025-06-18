# plex-playlist-sort
Simple command-line tool to sort plex playlists.

Disclaimer: Code written by ChatGPT.

# Info
Requires python set up on your device, as well as the plexapi package.

I tested this on a Windows 11 machine, and only used music playlists. Not sure how it would handle video playlists.

Before running, replace the PLEX_BASEURL and PLEX_TOKEN with your url and token.

# Usage
Basic usage is
`python pps.py --playlist "[playlist name]" --sort [sort method]`

Example - `python pps.py --playlist "TEST" -sort title`

This will sort the referenced playlist alphabetically by song title.

There a various other sort options -
```
title
artist
duration
track (track number on album)
year
views (play count)
rating (user rating)
original (no sort)
```

And some modifiers - 
```
--desc (sort in reverse/descending order, works for all sort methods except original)
--reverse (only used when using original sort)
--dry-run (preview sorting in cmd without making changes)
--backup (creates "[Playlist Title] Backup" playlist)
```

Here is some example output -
```
PS C:\Users\user\Documents> python pps.py --playlist "TEST" --sort artist --dry-run
Loaded playlist 'TEST' with 22 items.

Preview of sorted order:
 1. Couldnt Have Known - !!!
 2. Here - Alessia Cara
 3. May - American Wolf
 4. Doorstep - ANYA
 5. Half Light I - Arcade Fire
 6. Batphone - Arctic Monkeys
 7. M.I.A. - Avenged Sevenfold
 8. Hail To The King - Avenged Sevenfold
 9. Miracle Man - AWOLNATION
10. How Am I Not Myself - Bad Suns
11. Backboard - Baird
12. Young Pros - Bass Drum of Death
13. Bite Down (Bastille Vs. HAIM) - Bastille
14. Friends in High Places - Bear Hands
15. Wake Me - Bleachers
16. Alma Mater - Bleachers
17. All My Heroes - Bleachers
18. PDLIF - Bon Iver
19. 33 “GOD” - Bon Iver
20. In One Ear - Cage The Elephant
21. Sincerity Is Scary - The 1975
22. I Hate Camera - The Bird and The Bee
PS C:\Users\user\Documents> python pps.py --playlist "TEST" --sort artist --dry-run --desc
Loaded playlist 'TEST' with 22 items.

Preview of sorted order:
 1. I Hate Camera - The Bird and The Bee
 2. Sincerity Is Scary - The 1975
 3. In One Ear - Cage The Elephant
 4. PDLIF - Bon Iver
 5. 33 “GOD” - Bon Iver
 6. Wake Me - Bleachers
 7. Alma Mater - Bleachers
 8. All My Heroes - Bleachers
 9. Friends in High Places - Bear Hands
10. Bite Down (Bastille Vs. HAIM) - Bastille
11. Young Pros - Bass Drum of Death
12. Backboard - Baird
13. How Am I Not Myself - Bad Suns
14. Miracle Man - AWOLNATION
15. M.I.A. - Avenged Sevenfold
16. Hail To The King - Avenged Sevenfold
17. Batphone - Arctic Monkeys
18. Half Light I - Arcade Fire
19. Doorstep - ANYA
20. May - American Wolf
21. Here - Alessia Cara
22. Couldnt Have Known - !!!
PS C:\Users\user\Documents>  python pps.py --playlist "TEST" --sort artist
Loaded playlist 'TEST' with 22 items.
Reordering playlist...
Done.
PS C:\Users\user\Documents>
```
