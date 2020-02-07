from google.cloud import speech_v1
from google.cloud.speech_v1 import enums


def sample_long_running_recognize(storage_uri):
    """
    Transcribe long audio file from Cloud Storage using asynchronous speech
    recognition
    Args:
      storage_uri URI for audio file in Cloud Storage, e.g. gs://[BUCKET]/[FILE]
    """
    client = speech_v1.SpeechClient()
    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 44100
    # The language of the supplied audio
    language_code = "es-US"
    language_codes = ('es-ES', 'es-AR', 'es-CL', 'es-US')
    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    #encoding = enums.RecognitionConfig.AudioEncoding.MP3
    metadata = {
        "original_media_type": enums.RecognitionMetadata.OriginalMediaType.AUDIO,
        "original_mime_type": 'audio/m4a',
        #"recording_device_name": recording_device_name,
    }

    for lc in language_codes:
        config = {
        "metadata": metadata,
        "sample_rate_hertz": sample_rate_hertz,
        "audio_channel_count": 2,
        "language_code": language_code,
        "encoding": encoding,
        }
        audio = {"uri": storage_uri}
        operation = client.long_running_recognize(config, audio)
        print(u"Waiting for operation to complete...{}".format(lc))
        response = operation.result()
        for result in response.results:
            # First alternative is the most probable result
            alternative = result.alternatives[0]
            outname = storage_uri.split('/')[-1]
            with open("{}_{}.txt".format(outname, lc.replace("-","_")), 'w') as textout:
                textout.write(alternative.transcript)
            #print(u"Transcript: {}".format(alternative.transcript))

storage_uri = 'gs://XXXX/brooklyn_bridge.wav'

sample_long_running_recognize(storage_uri)
