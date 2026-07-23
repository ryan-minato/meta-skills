---
name: meta-ml-audio-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  speech- or audio-processing project to authoritative documentation
  entry points — speech recognition and speaker processing (Whisper
  family, SpeechBrain, ESPnet, Kaldi/k2, pyannote), speech synthesis and
  voice cloning (GPT-SoVITS, CosyVoice, F5-TTS, Piper), voice conversion
  and source separation (RVC family, Demucs, librosa, torchaudio), and
  music and generative audio (AudioCraft, Essentia, Magenta). Use when a
  harness build must record where the docs live for a project that
  recognizes, synthesizes, converts, separates, or generates speech,
  sound, or music. Not for choosing between tools or recommending one,
  and not for non-audio modalities.
---

# Speech & Audio Documentation Map

This skill produces the documentation entry points a harness build
records for a speech or audio project. It expects a harness build in
progress and access to the target's dependency manifests. Per-tool
content is one line plus a URL — install commands and model details are
always fetched from the recorded entry point, never recalled from
memory — and nothing here is a recommendation: when the target lacks a
tool for a need, record the option list with URLs and leave the choice
to the user.

## Workflow

1. Detect the audio stack: dependency manifests and imports (`whisper`,
   `faster_whisper`, `speechbrain`, `espnet`, `pyannote`, `librosa`,
   `torchaudio`, `demucs`), cloned tool checkouts (RVC, GPT-SoVITS,
   UVR), and audio data directories or manifests.
2. Read [speech-recognition.md](references/speech-recognition.md) when
   the target transcribes, aligns, or diarizes speech.
3. Read [tts-and-voice.md](references/tts-and-voice.md) when the target
   synthesizes speech or clones voices.
4. Read
   [voice-conversion-and-separation.md](references/voice-conversion-and-separation.md)
   when the target converts voices, separates sources, or does general
   audio processing and augmentation.
5. Read [music-and-audio.md](references/music-and-audio.md) when the
   target analyzes or generates music and general audio.
6. For every entry point about to be recorded, prefer an agent-oriented
   rendition: a page's `.md` source, then `<docs-root>/llms.txt` (a
   compact index). Fall back to `llms-full.txt` only when neither
   exists, and never read it whole — it is the whole site as one
   file; search it programmatically.
7. Record each detected tool — name, one-line role, documentation entry
   point, and its llms.txt when present — wherever the harness keeps
   conventions.

Done when: every audio tool the target actually uses has a recorded,
live documentation entry point, and nothing recorded ranks or recommends
between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: engine and voice-model selection
  is the user's decision.
- Many tools here are cloned applications or research repos — the
  repository root is the entry point and the install procedure lives in
  its README.
- Multi-domain toolkits (NeMo, ESPnet, SpeechBrain, PaddleSpeech) cover
  recognition and synthesis under one entry point — record it once and
  note both uses.
- Tools this skill does not list are out of scope: record only what its
  tables cover, and leave finding docs for anything else to the agent —
  it is not this skill's job.
