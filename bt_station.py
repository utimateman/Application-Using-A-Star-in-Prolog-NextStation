
#===================================================================
# Airport Link
#===================================================================
def al_name():
    al = [
    "phaya_thai_airlink",
    "ratchaprarop",
    "makkasan",
    "ramkhamhaeng",
    "hua_mak",
    "ban_thap_chang",
    "latkrabang",
    "suvarnabhumi"
            ]

    return al


#===================================================================
# BTS - Silom Line
#===================================================================
def bts_g_name():
    bts_g = [
    "national_stadium",
    "ratchadamri",
    "sala_daeng",
    "chong_nonsi",
    "surasak",
    "saphan_taksin",
    "krung_thon_buri",
    "wongwian_yai",
    "pho_nimit",
    "talat_phlu",
    "wutthakat",
    "bang_wa"
        ]

    return bts_g



#===================================================================
# BTS - Sukhumvit Line
#===================================================================

def bts_lg_name():

    bts_lg = [
    "mo_chit",
    "saphan_kwai",
    "ari",
    "sanam_pao",
    "victory_monument",
    "phaya_thai",
    "ratchathewi",
    "siam",
    "chit_lom",
    "ploen_chit",
    "nana",
    "asok",
    "phrom_phong",
    "thong_lo",
    "ekkamai",
    "phra_khanong",
    "on_nut",
    "bang_chak",
    "punnawithi",
    "udom_suk",
    "bang_na",
    "bearing",
    "samrong"
    ]

    return bts_lg

#===================================================================
#  MRT Purple Line
#===================================================================

def mrt_p_name():
    mrt_p = [
    "khlong_bang_phai",
    "talad_bang_yai",
    "sam_yaek_bang_yai",
    "bang_phlu",
    "bang_rak_yai",
    "bang_rak_noi_tha_it",
    "sai_ma",
    "phra_nang_klao_bridge",
    "yaek_nonthaburi1",
    "bang_krasor",
    "nonthaburi_civic_center",
    "ministry_of_public_health",
    "yaek_tiwanon",
    "wong_sawang",
    "bang_son"


    ]

    return mrt_p


#===================================================================
#  MRT Blue Line
#===================================================================

def mrt_b_name():

    mrt_b = [
    "hua_lamphong",
    "sam_yan",
    "si_lom",
    "lumphini",
    "klong_toei",
    "queen_sirkit_national_covention_center",
    "sukhumvit",
    "phetchaburi",
    "phra_ram_9",
    "thailand_cultural_center",
    "huai_kwang",
    "sutthisan",
    "ratchadaphisek",
    "lat_phrao",
    "phahon_yothin",
    "chatuchak_park",
    "kamphaen_phet",
    "bang_sue",
    "tao_poon"
    ]

    return mrt_b


def all_name():
    all_station = al_name() + bts_g_name() + bts_lg_name() + mrt_p_name() + mrt_b_name()
    return all_station
