Name:		kokoro-voice-am_liam
Version:	1.0
Release:	1
Summary:	American English male Kokoro voice am_liam
URL:		https://huggingface.co/hexgrad/Kokoro-82M/tree/main/voices
License:	Apache-2.0
BuildArch:	noarch
Group:		System/Multimedia
Provides:	kokoro-voice
Provides:	kokoro-voice-en
Provides:	kokoro-voice-en_US
Requires:	kokoro-model >= 1.0

%sourcelist
https://huggingface.co/hexgrad/Kokoro-82M/resolve/main/voices/am_liam.pt

%description
%{summary}.
Uses the shared checkpoint in kokoro-model.
Pronunciation uses the misaki English lexicon.
Select it with: kokoro -m am_liam

%install
mkdir -p %{buildroot}%{_datadir}/kokoro/voices
install -c -m 644 %{S:0} %{buildroot}%{_datadir}/kokoro/voices/am_liam.pt

%files
%{_datadir}/kokoro/voices/am_liam.pt
