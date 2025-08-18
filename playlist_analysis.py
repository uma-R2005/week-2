def input_playlists():
    playlists = {}
    n = int(input("How many playlists do you want to enter? "))
    for i in range(1, n + 1):
        print(f"\nEnter songs for Playlist {i} (comma-separated):")
        songs = input().strip().lower().split(",")
        # Clean and strip whitespace
        songs = {song.strip() for song in songs if song.strip()}
        playlists[f"Playlist {i}"] = songs
    return playlists

def union_songs(playlists):
    all_songs = set()
    for songs in playlists.values():
        all_songs |= songs
    return all_songs

def intersection_songs(playlists):
    all_sets = list(playlists.values())
    if not all_sets:
        return set()
    common = all_sets[0]
    for s in all_sets[1:]:
        common &= s
    return common

def unique_songs_per_playlist(playlists):
    unique_songs = {}
    for pname, songs in playlists.items():
        others = set()
        for other_pname, other_songs in playlists.items():
            if other_pname != pname:
                others |= other_songs
        unique_songs[pname] = songs - others
    return unique_songs

def songs_in_exactly_two(playlists):
    from collections import Counter
    song_counts = Counter()
    for songs in playlists.values():
        song_counts.update(songs)
    return {song for song, count in song_counts.items() if count == 2}

def main():
    playlists = input_playlists()

    print("\nAll unique songs across playlists:")
    print(sorted(union_songs(playlists)))

    print("\nSongs common to all playlists:")
    common = intersection_songs(playlists)
    print(sorted(common) if common else "No common songs")

    print("\nSongs unique to each playlist:")
    unique_songs = unique_songs_per_playlist(playlists)
    for pname, songs in unique_songs.items():
        print(f"{pname}: {sorted(songs) if songs else 'None'}")

    print("\nSongs that appear in exactly two playlists:")
    exact_two = songs_in_exactly_two(playlists)
    print(sorted(exact_two) if exact_two else "None")

if __name__ == "__main__":
    main()
