# Auxilium approved voiceover voices (picked by Rob, 15 Nov 2026)

Rob's FAVOURITES are the Northern Irish voices 13–16. Use them for most AI videos.

| No. | Voice | Accent | Use |
|---|---|---|---|
| 13 | Male | Northern Irish | favourite |
| 14 | Male | Northern Irish | favourite |
| 15 | Female | Northern Irish | favourite |
| 16 | Female | Northern Irish | favourite |
| 1 | Male, deep and steady | British | occasional |
| 2 | Male, younger, warmer | British | occasional |
| 3 | Male, crisp | British | occasional |
| 4 | Male, softer | British | occasional |
| 5 | Female, clear and warm | British | occasional |
| 6 | Female, polished | British | occasional |
| 7 | Female, brighter | British | occasional |
| 8 | Female, gentle | British | occasional |
| 9 | Male, blend of 1+2 | British | occasional |
| 10 | Male, blend of 3+4 | British | occasional |
| 11 | Male, blend of 1+3 | British | occasional |
| 12 | Female, blend of 5+6 | British | occasional |

## Rules
- Only these 16 voices. Never American, never a clone of Rob, never any other voice.
- Rotation: about 3 in every 4 AI videos use a Northern Irish voice (13–16); the rest use 1–12. Never the same voice on two videos in a row. One voice per video.
- Setup once per run: `bash voice/setup_voices.sh /home/claude/voicework`
- Make each line: `python3 voice/make_vo.py --voice 13 --text "..." --out line01.wav`
- Northern Irish voices (13–16) are slower to generate; make all lines for a video in one go and reuse the work folder.
