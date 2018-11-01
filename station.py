#>>> a = {'boss':'1', 'c':'2'}
#>>> a['boss']
#'1'
#>>>


#===================================================================
# Airport Link
#===================================================================
def al_dict():
    al = {
        'phaya_thai_airlink':'Phaya Thai Airlink',
        'ratchaprarop':'Ratchaprarop',
        'makkasan':'Makkasan',
        'ramkhamhaeng':'Ramkhamhaeng',
        'hua_mak':'Hua Mak',
        'ban_thap_chang':'Ban Thap Chang',
        'latkrabang':'Latkrabang',
        'suvarnabhumi':'Suvarnabhumi'
        }
    return al

#===================================================================
# BTS - Silom Line  (G Line)
#===================================================================
def bts_g_dict():
    bts_g = {
    'national_stadium':'National Stadium',
    'ratchadamri':'Ratchadamri',
    'sala_daeng':'Sala Daeng',
    'chong_nonsi':'Chong Nonsi',
    'surasak':'Surasak',
    'saphan_taksin':'Saphan Taksin',
    'krung_thon_buri':'Krung Thon Buri',
    'wongwian_yai':'Wongwian Yai',
    'pho_nimit':'Pho Nimit',
    'talat_phlu':'Talat Phlu',
    'wutthakat':'Wutthakat',
    'bang_wa':'Bang Wa'
    }
    return bts_g


#===================================================================
# BTS - Sukhumvit Line (LG Line)
#===================================================================
def bts_lg_dict():

    bts_lg = {
    'mo_chit':'Mo Chit',
    'saphan_kwai':'Saphan Kwai',
    'ari':'Ari',
    'sanam_pao':'Sanam Pao',
    'victory_monument':'Victory Monument',
    'phaya_thai':'Phaya Thai',
    'ratchathewi':'Ratchathewi',
    'siam':'Siam',
    'chit_lom':'Chit Lom',
    'ploen_chit':'Ploen Chit',
    'nana':'Nana',
    'asok':'Asok',
    'phrom_phong':'Phrom Phon',
    'thong_lo':'Thong Lo',
    'ekkamai':'Ekkamai',
    'phra_khanong':'Phra Khanong',
    'on_nut':'On Nut',
    'bang_chak':'Bang Chak',
    'punnawithi':'Punnawithi',
    'udom_suk':'Udom Suk',
    'bang_na':'Bang Na',
    'bearing':'Bearing',
    'samrong':'Samrong'
    }

    return bts_lg



#===================================================================
#  MRT Purple Line
#===================================================================

def mrt_p_dict():
    mrt_p = {
    'khlong_bang_phai':'Khlong Bang Phai',
    'talad_bang_yai':'Talad Bang Yai',
    'sam_yaek_bang_yai':'Sam Yaek Bang Yai',
    'bang_phlu':'Bang Phlu',
    'bang_rak_yai':'Bang Rak Yai',
    'bang_rak_noi_tha_it':'Bang Rak Noi Tha It',
    'sai_ma':'Sai Ma',
    'phra_nang_klao_bridge':'Phra Nang Klao Bridge',
    'yaek_nonthaburi1':'Yaek Nonthaburi 1',
    'bang_krasor':'Bang Krasor',
    'nonthaburi_civic_center':'Nonthaburi Civic Center',
    'ministry_of_public_health':'Ministry Of Public Health',
    'yaek_tiwanon':'Yaek Tiwanon',
    'wong_sawang':'Wong Sawang',
    'bang_son':'Bang Son'
    }

    return mrt_p




#===================================================================
#  MRT Blue Line
#===================================================================

def mrt_b_dict():

    mrt_b = {
    'hua_lamphong':'Hua Lamphong',
    'sam_yan':'Sam Yan',
    'si_lom':'Si Lom',
    'lumphini':'Lumphini',
    'klong_toei':'Klong Toei',
    'queen_sirkit_national_covention_center':'Queen Sirkit National Covention Center',
    'sukhumvit':'Sukhumvit',
    'phetchaburi':'Phetchaburi',
    'phra_ram_9':'Phra Ram 9',
    'thailand_cultural_center':'Thailand Cultural Center',
    'huai_kwang':'Huai Kwang',
    'sutthisan':'Sutthisan',
    'ratchadaphisek':'Ratchadaphisek',
    'lat_phrao':'Lat Phrao',
    'phahon_yothin':'Phahon Yothin',
    'chatuchak_park':'Chatuchak Park',
    'kamphaen_phet':'kamphaen Phet',
    'bang_sue':'Bang Sue',
    'tao_poon':'Tao Poon'
    }
    return mrt_b

'''
def all_dict():
    #all_station = al_dict() + bts_g_dict() + bts_lg_dict() + mrt_p_dict() + mrt_b_dict()
    all_station = al_dict().copy
    all_station.update(bts_g_dict())
    
    a = all_station.copy
    a.update(bts_lg_dict())
    
    b = a.copy
    b.update(mrt_p_dict())
    
    c = b.copy
    c.update(mrt_b_dict())
    return c
'''
def merge_dict(x,y):
    z = x.copy()
    z.update(y)
    return z

def all_dict():
    all_station = [al_dict(), bts_g_dict(), bts_lg_dict(), mrt_p_dict(), mrt_b_dict()]
    dict_0_1 = merge_dict(all_station[0],all_station[1])
    dict_0_2 = merge_dict(dict_0_1, all_station[2])
    dict_0_3 = merge_dict(dict_0_2, all_station[3])
    dict_0_4 = merge_dict(dict_0_3, all_station[4])

    return dict_0_4