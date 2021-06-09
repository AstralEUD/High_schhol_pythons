from jamo import *
import sys
mod = sys.modules[__name__]

#jamo Package 설치 필요
#Powershell 이나 CMD 를 관리자 권한으로 실행해서
#pip3 install jamo
#를 통하여 Jamo 패키지를 설치하세요.
#jamo 패키지는 한글의 초/중/종성 분리를 위한 패키지입니다.
hangul_input = str(input('변환할 한글을 입력하세요. 단, 문장은 되지 않고 단어형만 가능합니다'))
hangul_bunli = j2hcj(h2j(hangul_input))
#한글 분리

rome_list = [['ㄱ','k'],['ㄱ2','g'],['ㅋ','k'],['ㄷ','d'],['ㄷ2','t'],['ㄸ','tt'],['ㅌ','t'],['ㅂ','b'],['ㅂ2','p'],
             ['ㅃ','pp'],['ㅍ','p'],['ㅈ','j'],['ㅉ','jj'],['ㅊ','ch'],['ㅅ','s'],['ㅆ','ss'],['ㅎ','h'],['ㄴ','n'],['ㅁ','m'],['ㄹ','r'],['ㄹ2','l'],
             ['ㅏ','a'],['ㅓ','eo',],['ㅗ','o'],['ㅜ','u'],['ㅡ','eu'],['ㅣ','i'],['ㅐ','ae'],['ㅔ','e'],['ㅚ','oe'],['ㅟ','wi'],['ㅑ','ya'],['ㅕ','yeo'],['ㅛ','yo'],
             ['ㅠ','yu'],['ㅒ','yae'],['ㅖ','ye'],['ㅘ','wa'],['ㅙ','wae'],['ㅝ','wo'],['ㅞ','we'],['ㅢ','ui']]

jaum = ['ㄱ','ㄲ','ㅋ','ㄷ','ㄸ','ㅌ','ㅂ','ㅃ','ㅍ','ㅈ','ㅉ','ㅊ','ㅅ','ㅆ','ㅎ','ㄴ','ㅁ','ㅇ','ㄹ']
moum = ['ㅏ','ㅓ','ㅗ','ㅜ','ㅡ','ㅣ','ㅐ','ㅔ','ㅚ','ㅟ','ㅑ','ㅕ','ㅛ','ㅠ','ㅒ','ㅖ','ㅘ','ㅙ','ㅝ','ㅞ','ㅢ']

moum_list_1 = moum
moum_list_2 = moum
moum_list_3 = moum
for i in range(19):
    setattr(mod, 'jaum_change_g_{}'.format(i), 'ㄱ'+moum_list_1.pop())
for i in range(19):
    setattr(mod, 'jaum_change_d_{}'.format(i), 'ㄱ'+moum_list_2.pop())
for i in range(19):
    setattr(mod, 'jaum_change_b_{}'.format(i), 'ㄱ'+moum_list_3.pop())

#로마자 표기법
# ※ ㄱ,ㄷ,ㅂ은 모음 앞에서는 g,d,b 로, 자음 앞이나 어말에서는 k,t,p로 발음한다.


hangul_bunli_list = [hangul_bunli]
for i in range (19):
    if hangul_bunli in 'jaum_change_g{}'.format(i):
        hangul_bunli.replace("'jaum_change_g{}'.format(i)",'ㄱ2')
if hangul_bunli_list in
