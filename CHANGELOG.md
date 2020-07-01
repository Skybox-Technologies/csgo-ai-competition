# Changelog

## Version 3
- Added map_crc and patch_version
- Removed kills that occur during freezetime

## Version 2
- Fixed current_score sometimes being wrong ([#1](/../../issues/1), thanks @russointroitoa)
- Fixed tickrate heuristic making incorrect guesses for some corrupted demos, resulting in
  too many snapshots for some rounds ([#4](/../../issues/4), thanks @MiniXC)
- Filtered snapshots with invalid `status_time` during pauses and after bomb exploded (([#4](/../../issues/4), thanks @MiniXC)
- Fixed time leak for bomb plants ([#5](/../../issues/5), thanks @MiniXC)
- Fixed bad smoke data ([#6](/../../issues/6), thanks @russointroitoa)

## Version 1
Initial release

