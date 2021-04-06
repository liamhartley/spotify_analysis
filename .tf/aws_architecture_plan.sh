#!/usr/bin/env bash

# Run this script pointing to all libraries required to package them for the Lambda.

terraform init

cp -r /Users/liamhartley/IdeaProjects/fpl/venv/lib/python3.7/site-packages/spotipy ../lambda_payloads/avg_album_length_playlist_payload/
cp -r /Users/liamhartley/IdeaProjects/fpl/venv/lib/python3.7/site-packages/requests ../lambda_payloads/avg_album_length_playlist_payload/

cp /Users/liamhartley/IdeaProjects/spotify_analysis/avg_album_length_playlist.py ../lambda_payloads/avg_album_length_playlist_payload/
cp /Users/liamhartley/IdeaProjects/spotify_analysis/config/playlists.py ../lambda_payloads/avg_album_length_playlist_payload/config/
cp /Users/liamhartley/IdeaProjects/spotify_analysis/tools/playlists.py ../lambda_payloads/avg_album_length_playlist_payload/tools/

cd ../lambda_payloads/avg_album_length_playlist_payload/

zip -r ../../payload.zip *

cd ../../.tf/

terraform plan

