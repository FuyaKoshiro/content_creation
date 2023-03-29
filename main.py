from get_video  import GetVideo
from get_script import GetScript
from get_phrase import GetPhrase
from fix_output import FixOutput
import translator
from make_html import MakeHTML
from update_db import UpdateDB
from extract_db import ExtractDB
from update_index_html import UpdateIndexHTML


import time


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
        phrase_list = get_phrase.get_phrase_list()

        fix_ouput= FixOutput(phrase_list=phrase_list)
        phrase_list = fix_ouput.fix_phrase_list()

        deepl_translator= translator.DeepLTranslator(phrase_list=phrase_list)
        meaning_list = deepl_translator.translate()

        make_html = MakeHTML(phrase_list=phrase_list, meaning_list=meaning_list, vcode=vcode, vtitle=vtitle)
        make_html.make_html_page()

        update_db = UpdateDB(vcode=vcode, vtitle=vtitle)
        update_db.insert_value()
        update_db.check_progress()

    extract_db = ExtractDB()
    df = extract_db.get_df()

    updated_index_html = UpdateIndexHTML(df=df)
    updated_index_html.make_page()

    print("="*80, "\ndone")