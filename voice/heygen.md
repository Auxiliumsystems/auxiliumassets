# Auxilium voiceover: HeyGen Irish voices (live from 15 Nov 2026)

The robotic local voices (voice/voices.md, make_vo.py) are retired. Do not use them.

## Approved voices (HeyGen public instant voices, southern Irish, locale en-IE)
| Name | voice_id | Gender | Style |
|---|---|---|---|
| Conor | 0f7bdc5d6f9045d3b960eeb0b28d107a | male | rich, expressive |
| Cian | a0321c4213d842e99c1f4d31b5006a47 | male | punchy, spirited |
| Orlaith | 314e57d116b64159b40907ddaea4015e | female | lively, informative |
| Deirdre | 84bc506c91674034aa1d32e22903f627 | female | gentle, instructive |

Rotation: one voice per video, never the same voice on two videos in a row; roughly 2 male : 1 female.
Never use Rob's own voice clone ("Robert Whelan") — the brand rules forbid an AI clone of Rob.
Rob may narrow this list; if a "Picked:" line exists below, use only those voices.

## How to make the audio (inside a scheduled run)
1. Use the HeyGen connector tool `create_speech_without_player` (load it with ToolSearch if deferred) with
   voiceId from the table, language "en", and the line of script. Generate one clip per beat so you know each
   beat's length. Write numbers and times as words. Audio tags like [pause] are allowed sparingly.
2. The tool returns `audio_url` (on resource2.heygen.ai) and `duration`. Download it in the sandbox:
   `curl -sSL -o lineNN.wav "<audio_url>"` (the domain is allow-listed).
3. Time the video's beats to the clips, join them with short gaps into one track, then:
   `ffmpeg -i silent.mp4 -i vo.wav -c:v copy -c:a aac -b:a 160k -af loudnorm=I=-14:TP=-1.5:LRA=11 -shortest out.mp4`
4. Confirm with ffprobe there is an audio stream. In the approval doc write "Voiceover: {Name} (Irish, male/female)" and the script.
5. If a HeyGen call fails, do not retry more than once; deliver the video silent with the script and say so.
