---
title: Speech, Voice & Audio
description: Speech recognition and diarization, TTS and voice cloning, voice conversion and separation, and music/generative-audio tooling.
tags: [machine-learning, audio, generative]
---

# Speech, Voice & Audio

Fetch when the target recognizes, synthesizes, converts, separates, or generates speech, sound, or music. Each entry is one line and a documentation entry point; fetch install and model details from the entry point, never from memory. No entry is a recommendation.

## Speech Recognition

| Tool | One line | Docs |
|---|---|---|
| Whisper | OpenAI's multilingual speech recognition | <https://github.com/openai/whisper> |
| faster-whisper | CTranslate2-accelerated Whisper inference | <https://github.com/SYSTRAN/faster-whisper> |
| whisper.cpp | Whisper in C/C++ for local devices | <https://github.com/ggml-org/whisper.cpp> |
| SpeechBrain | conversational-AI toolkit: ASR, speakers, enhancement, TTS | <https://speechbrain.readthedocs.io/> |
| ESPnet | end-to-end speech processing toolkit | <https://espnet.github.io/espnet/> |
| FunASR | industrial ASR with punctuation and diarization | <https://github.com/modelscope/FunASR> |
| WeNet | production-first streaming ASR | <https://github.com/wenet-e2e/wenet> |
| Kaldi | the classic WFST speech-recognition toolkit | <https://kaldi-asr.org/doc/> |
| k2 | FST algorithms integrated with autograd | <https://k2-fsa.github.io/k2/> |
| icefall | k2-based recognition recipes | <https://k2-fsa.github.io/icefall/> |
| PaddleSpeech | Paddle's speech toolkit: ASR and TTS | <https://github.com/PaddlePaddle/PaddleSpeech> |
| sherpa-onnx | on-device speech pipelines from the k2 family | <https://k2-fsa.github.io/sherpa/> |
| pyannote.audio | speaker diarization pipelines | <https://github.com/pyannote/pyannote-audio> |
| Silero VAD | lightweight voice-activity detection | <https://github.com/snakers4/silero-vad> |
| Montreal Forced Aligner | pronunciation-dictionary forced alignment | <https://montreal-forced-aligner.readthedocs.io/> |

## TTS & Voice

| Tool | One line | Docs |
|---|---|---|
| GPT-SoVITS | few-shot voice cloning TTS | <https://github.com/RVC-Boss/GPT-SoVITS> |
| CosyVoice | multilingual zero-shot TTS | <https://github.com/FunAudioLLM/CosyVoice> |
| Fish Speech | multilingual TTS with voice cloning | <https://github.com/fishaudio/fish-speech> |
| F5-TTS | flow-matching zero-shot TTS | <https://github.com/SWivid/F5-TTS> |
| OpenVoice | instant voice cloning with style control | <https://github.com/myshell-ai/OpenVoice> |
| Piper | fast local neural TTS | <https://github.com/rhasspy/piper> |
| StyleTTS2 | style-diffusion TTS | <https://github.com/yl4579/StyleTTS2> |
| Kokoro | small open-weight TTS | <https://github.com/hexgrad/kokoro> |
| VITS | the end-to-end adversarial TTS baseline | <https://github.com/jaywalnut310/vits> |

## Voice Conversion & Separation

| Tool | One line | Docs |
|---|---|---|
| Retrieval-based Voice Conversion WebUI | the RVC voice-conversion app | <https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI> |
| Applio | streamlined RVC fork with an ecosystem | <https://docs.applio.org/> |
| Seed-VC | zero-shot voice conversion | <https://github.com/Plachtaa/seed-vc> |
| RMVPE | robust vocal pitch estimation used across VC stacks | <https://github.com/Dream-High/RMVPE> |
| ContentVec | speaker-disentangled speech representations | <https://github.com/auspicious3000/contentvec> |
| WORLD | classic vocoder for analysis/synthesis | <https://github.com/mmorise/World> |
| PyWorld | Python bindings for WORLD | <https://github.com/JeremyCCHsu/Python-Wrapper-for-World-Vocoder> |
| Demucs | music source separation | <https://github.com/adefossez/demucs> |
| Ultimate Vocal Remover | GUI over separation models | <https://github.com/Anjok07/ultimatevocalremovergui> |
| librosa | audio analysis and feature extraction | <https://librosa.org/doc/> |
| torchaudio | PyTorch audio I/O, transforms, and models | <https://docs.pytorch.org/audio/> |
| Audiomentations | audio data augmentation | <https://iver56.github.io/audiomentations/> |
| Spotify Pedalboard | studio-quality audio effects in Python | <https://spotify.github.io/pedalboard/> |

## Music & Audio

| Tool | One line | Docs |
|---|---|---|
| Essentia | audio analysis and music information retrieval | <https://essentia.upf.edu/> |
| Meta AudioCraft | MusicGen and AudioGen generative audio | <https://github.com/facebookresearch/audiocraft> |
| EnCodec | neural audio codec | <https://github.com/facebookresearch/encodec> |
| DDSP | differentiable digital signal processing | <https://github.com/magenta/ddsp> |
| Magenta | music and art generation research tools | <https://magenta.tensorflow.org/> |
| pretty_midi | MIDI handling in Python | <https://craffel.github.io/pretty-midi/> |
| Music21 | computational musicology toolkit | <https://music21.org/music21docs/> |

## Gotchas

- Many entries are research repos or cloned applications — the repository README is the documentation.
- Multi-domain toolkits (ESPnet, SpeechBrain, PaddleSpeech) cover several audio tasks (recognition and synthesis, among others) under one entry point — note the tasks actually in use.
- The NVIDIA NeMo framework is recorded with the training stack — see the [training-and-finetuning page](training-and-finetuning.md).
