from jamo import *
import sys
import copy
mod = sys.modules[__name__]

#jamo Package 설치 필요
#Powershell 이나 CMD 를 관리자 권한으로 실행해서
#pip3 install jamo
#를 통하여 Jamo 패키지를 설치하세요.
#jamo 패키지는 c의 초/중/종성 분리를 위한 패키지입니다.
hangul_input = str(input('변환할 한글을 입력하세요. 단, 문장은 되지 않고 단어형만 가능합니다'))
hangul_bunli = j2hcj(h2j(hangul_input))
#한글 분리

rome_list = [['ㅇ','ng'],['ㄱ','k'],['ㄱ2','k'],['ㅋ','k'],['ㄷ','t'],['ㄷ2','t'],['ㄸ','tt'],['ㅌ','t'],['ㅂ','p'],['ㅂ2','p'],['ㅃ','pp'],['ㅍ','p'],['ㅈ','j'],['ㅉ','jj'],['ㅊ','ch'],['ㅅ','s'],['ㅆ','ss'],['ㅎ','h'],['ㄴ','n'],['ㅁ','m'],['ㄹ','l'],['ㄹ2','l'],['ㅏ', 'a'], ['ㅓ', 'eo', ], ['ㅗ', 'o'], ['ㅜ', 'u'], ['ㅡ', 'eu'], ['ㅣ', 'i'], ['ㅐ', 'ae'],['ㅔ','e'],['ㅚ','oe'],['ㅟ','wi'],['ㅑ','ya'],['ㅕ','yeo'],['ㅛ','yo'],['ㅠ','yu'],['ㅒ','yae'],['ㅖ','ye'],['ㅘ','wa'],['ㅙ','wae'],['ㅝ','wo'],['ㅞ','we'],['ㅢ','ui']]

jaum = ['ㄱ','ㄲ','ㅋ','ㄷ','ㄸ','ㅌ','ㅂ','ㅃ','ㅍ','ㅈ','ㅉ','ㅊ','ㅅ','ㅆ','ㅎ','ㄴ','ㅁ','ㅇ','ㄹ']
moum = ['ㅏ','ㅓ','ㅗ','ㅜ','ㅡ','ㅣ','ㅐ','ㅔ','ㅚ','ㅟ','ㅑ','ㅕ','ㅛ','ㅠ','ㅒ','ㅖ','ㅘ','ㅙ','ㅝ','ㅞ','ㅢ']

moum_list_1 = copy.copy(moum)
moum_list_2 = copy.copy(moum)
moum_list_3 = copy.copy(moum)
moum_list_4 = copy.copy(moum)
moum_list_5 = copy.copy(moum)
for i in range(19):
    globals()['jaum_change_g_{}'.format(i)] = 'ㄱ'+moum_list_1.pop()
    globals()['jaum_change_d_{}'.format(i)] = 'ㄷ'+moum_list_2.pop()
    globals()['jaum_change_b_{}'.format(i)] = 'ㅂ'+moum_list_3.pop()
    globals()['jaum_change_r_{}'.format(i)] = 'ㄹ'+moum_list_4.pop()
    globals()['jaum_change_w_{}'.format(i)] = 'ㅇ'+moum_list_5.pop()
    print(i,'rd try')

#로마자 표기법
# ※ ㄱ,ㄷ,ㅂ은 모음 앞에서는 g,d,b 로, 자음 앞이나 어말에서는 k,t,p로 발음한다.
'''
for i in range(20):
    globals()['hangul_temp_g{}'.format(i)] = 0
    globals()['hangul_temp_d{}'.format(i)] = 0
    globals()['hangul_temp_b{}'.format(i)] = 0'''

#memo: hangul_bunli.find('variable's name)
#if it exists: 0
#if it doesn't exist: -1
#if hangul_bunli.find(globals()["jaum_change_g_{}".format(i)]) == 0:
hangul_bunli_list = [hangul_bunli]
for i in range (19):
    #if hangul_bunli in globals()["jaum_change_g_{}".format(i)]:
    if hangul_bunli.find(globals()["jaum_change_g_{}".format(i)]) >= 0:
        #globals()['hangul_temp_g{}'.format(i)] = globals()["jaum_change_g_{}".format(i)]
        #globals()["hangul_temp_g{}".format(i)].replace("ㄱ","ㄱ2")
        #hangul_bunli.replace(globals()["jaum_change_g_{}".format(i)],globals()["hangul_temp_g{}".format(i)])
        hangul_bunli = hangul_bunli.replace(globals()["jaum_change_g_{}".format(i)][0],"g")
        #hangul_bunli = hangul_bunli.replace(globals()["jaum_change_g_{}".format(i)],globals()["jaum_change_g_{}".format(i)].replace("ㄱ","ㄱ2"))
        #hangul_bunli.replace(globals()["jaum_change_g_{}.format(i)]","#")
        print('found',globals()["jaum_change_g_{}".format(i)])
        #hangul_bunli.replace("globals()['jaum_change_g_{}'.format(i)]","globals['hangul_temp_g{}'.format(i)]")
    #if hangul_bunli in globals()["jaum_change_d_{}".format(i)]:
    if hangul_bunli.find(globals()["jaum_change_d_{}".format(i)]) >= 0:
        #globals()["hangul_temp_d{}".format(i)] = globals()["jaum_change_d{}".format(i)]
        #globals()["hangul_temp_d{}".format(i)].replace("ㄷ","ㄷ2")
        #hangul_bunli = hangul_bunli.replace(globals()["jaum_change_d_{}".format(i)],globals()["jaum_change_d_{}".format(i)].replace("ㄷ","ㄷ2"))
        hangul_bunli = hangul_bunli.replace(globals()["jaum_change_d_{}".format(i)][0],"d")
        print('found',globals()["jaum_change_d_{}".format(i)])
        #hangul_bunli.replace(globals()["jaum_change_d_{}".format(i)],globals()["hangul_temp_d{}".format(i)])
        #hangul_bunli.replace("'jaum_change_d_{}'.format(i)",'hangul_temp_d{}.format(i)')
    #if hangul_bunli in globals()["jaum_change_b_{}".format(i)]:
    if hangul_bunli.find(globals()["jaum_change_b_{}".format(i)]) >= 0:
        #globals()["hangul_temp_b{}".format(i)] = globals()["jaum_change_d{}".format(i)]
        #globals()["hangul_temp_b{}".format(i)].replace("Q","Q2")
        #hangul_bunli = hangul_bunli.replace(globals()["jaum_change_b_{}".format(i)],globals()["jaum_change_b_{}".format(i)].replace("ㅂ","ㅂ2"))
        hangul_bunli = hangul_bunli.replace(globals()["jaum_change_b_{}".format(i)][0],"b")
        print('found',globals()["jaum_change_b_{}".format(i)])
        #hangul_bunli.replace(globals()["jaum_change_b_{}".format(i)],globals()["hangul_temp_b{}".format(i)])
       #hangul_bunli.replace("'jaum_change_b_{}'.format(i)",'hangul_temp_b{}.format(i)')
    if hangul_bunli.find(globals()["jaum_change_r_{}".format(i)]) >= 0:
        hangul_bunli = hangul_bunli.replace(globals()["jaum_change_r_{}".format(i)][0],"r")
        print('found',globals()["jaum_change_r_{}".format(i)])
    if hangul_bunli.find(globals()["jaum_change_w_{}".format(i)]) >= 0:
        hangul_bunli = hangul_bunli.replace(globals()["jaum_change_w_{}".format(i)],globals()["jaum_change_w_{}".format(i)][1])
        
if hangul_bunli.find("ㄹㄹ") >= 0:
    hangul_bunli = hangul_bunli.replace("ㄹㄹ",'ll')
for i in range(41):
    if rome_list[i][0] in hangul_bunli:
        hangul_bunli = hangul_bunli.replace(rome_list[i][0],rome_list[i][1])

print(hangul_bunli)
