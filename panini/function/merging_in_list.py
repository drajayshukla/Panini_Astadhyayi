import re

def merge_characters(word):
    merged_word = word.replace("्ओ", "ो").replace("्औ", "ौ").replace("्आ", "ा").replace("्अ", "").replace(':',':').replace('शइ','शि').replace('कउ','कु').replace('म्औ','मौ').replace('म्ऐ','मै').replace('म्ए','मे').replace('त्','त्').replace('ष्उ','षु').replace('व्ए','वे').replace('व्ऐ','वै').replace('प्ऊ','पू').replace('त्ए','ते').replace('त्ऐ','तै')\
            .replace('न्इ','नि').replace('च्ए','चे').replace('न्ए','ने').replace('व्इ','वि').replace('र्इ','रि').replace('त्इ','ति')\
        .replace('ज्ए','जे').replace('व्ए', 'वे').replace('व्ऐ', 'वै').replace('प्ऊ', 'पू').replace('त्ए', 'ते') \
                .replace('त्ऐ', 'तै').replace('न्इ', 'नि').replace('य्ए', 'ये').replace('र्इ', 'रि')\
                .replace('य्उ','यु').replace('क्ऋ','कृ').replace('त्इ','ति').replace('प्इ','पि')\
        .replace('ग्उ','गु').replace('द्ए','दे').replace('न्उ','नु').replace('स्उ','सु').replace('न्ई','नी').replace('भ्र्ए','भ्रे')

    merged_word = re.sub(r'([इईउऊएऐऔअंअ:])्', r'\1', merged_word)
    return merged_word
