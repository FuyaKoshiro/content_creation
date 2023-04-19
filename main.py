from get_video  import GetVideo
from get_script import GetScript
from get_phrase import GetPhrase
from fix_output import FixOutput
import translator
from update_db import UpdateDB


if __name__ == "__main__":
    get_video = GetVideo()
    vcode_list = get_video.get_vcode()
    vtitle_list = get_video.get_vtitle(vcode_list=vcode_list)

    for i in range(len(vcode_list)):
        
        vcode = vcode_list[i]
        vtitle = vtitle_list[i]

        get_script= GetScript(vcode=vcode)
        script = get_script.get_script_string()

        get_phrase = GetPhrase(script=script)
        answer = get_phrase.get_answer()
        answer_bs_removed = get_phrase.remove_backslash(answer=answer)
        phrase_list = get_phrase.get_phrase_list(answer_bs_removed=answer_bs_removed)

        fix_output= FixOutput(phrase_list=phrase_list)
        phrase_list = fix_output.fix_phrase_list()

        if phrase_list is None: #occasionally fail to pass a value, thus exclude it when it is the case
            pass
        
        else:
            gpt_translator= translator.gptTranslator(phrase_list=phrase_list)
            meaning_list = gpt_translator.translate()

            update_db = UpdateDB(vcode=vcode, vtitle=vtitle, phrase_list=phrase_list, meaning_list=meaning_list, vcode=vcode, vtitle=vtitle)
            update_db.insert_value_video()
            update_db.insert_value_video_vcode()

    print("="*80, "\ndone")