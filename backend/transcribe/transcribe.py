'''
The file formats supported by Whisper API are mp3, mp4, mpeg, mpga, m4a, wav, and webm. 
Currently, upload file size is limited to 25MB. If you have larger files, you can break 
them down into smaller chunks using pydub.
'''

# docs: https://github.com/openai/whisper
# basically all from the colab example linked in docs
import os
import numpy as np

try:
    import tensorflow  # required in Colab to avoid protobuf compatibility issues
except ImportError:
    pass

import torch
import pandas as pd
import whisper
import torchaudio
from tqdm.notebook import tqdm
import jiwer
from whisper.normalizers import EnglishTextNormalizer
import openai

import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

openai.api_key = "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"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


def transcribeAudioFile(self, file):
    # import pdb; pdb.set_trace();
    path = default_storage.save('tmp/tempsave.%s' % (file.name.split('.')[-1]), ContentFile(file.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)
    with open(tmp_file, "rb") as audio_file:
        transcript = openai.Audio.transcribe(
            file = audio_file,
            model = "whisper-1",
            response_format="text",
            language="en"
        )
        print(transcript)
    return transcript
    # waveform, sample_rate = torchaudio.load(file)
    # loader = torch.utils.data.DataLoader(dataset, batch_size=16)

    # model = whisper.load_model("base.en")
    # print(
    #     f"Model is {'multilingual' if model.is_multilingual else 'English-only'} "
    #     f"and has {sum(np.prod(p.shape) for p in model.parameters()):,} parameters."
    # )

    # # predict without timestamps for short-form transcription
    # options = whisper.DecodingOptions(language="en", without_timestamps=True)

    # hypotheses = []
    # references = []

    # for mels, texts in tqdm(loader):
    #     results = model.decode(mels, options)
    #     hypotheses.extend([result.text for result in results])
    #     references.extend(texts)

    # data = pd.DataFrame(dict(hypothesis=hypotheses, reference=references))
    # print(data)

    # normalizer = EnglishTextNormalizer()
    # data["hypothesis_clean"] = [normalizer(text) for text in data["hypothesis"]]
    # data["reference_clean"] = [normalizer(text) for text in data["reference"]]

    # wer = jiwer.wer(list(data["reference_clean"]), list(data["hypothesis_clean"]))

    # print(f"WER: {wer * 100:.2f} %")
