from test_response_llm import get_audio, get_llm_resp
from test_asr import transcibe_mic
# from test_vad import listen_with_vad


def test_pipeline_no_vad():

    user_audio = transcibe_mic()
    res_text = get_llm_resp(user_audio)
    get_audio(res_text)



# def test_pipeline_with_vad():
#     user_text = listen_with_vad()

#     if not user_text.strip():
#         return

#     print("User:", user_text)

#     res_text = get_llm_resp(user_text)
#     get_audio(res_text)


if __name__ == "__main__":
    test_pipeline_no_vad()