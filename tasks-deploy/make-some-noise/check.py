import math
import random


def check(attempt, context):
    if attempt.answer == flags[attempt.participant.id % len(flags)]:
        return Checked(True)
    for i in range(len(flags)):
        if attempt.answer == flags[i]:
            return CheckedPlagiarist(False, i)
    return Checked(False)


flags = ['QCTF{g00D_N0isss3_jiEaOU}', 'QCTF{g00D_N0isss3_VQaWEI}', 'QCTF{g00D_N0isss3_Vxsqw8}', 'QCTF{g00D_N0isss3_zjUhdQ}', 'QCTF{g00D_N0isss3_p64kwM}', 'QCTF{g00D_N0isss3_fBKv4S}', 'QCTF{g00D_N0isss3_AedMfV}', 'QCTF{g00D_N0isss3_8lsYSh}', 'QCTF{g00D_N0isss3_JNq341}', 'QCTF{g00D_N0isss3_3ZVvuS}', 'QCTF{g00D_N0isss3_BgRlyj}', 'QCTF{g00D_N0isss3_RXJChj}', 'QCTF{g00D_N0isss3_wMlmoF}', 'QCTF{g00D_N0isss3_JGzupU}', 'QCTF{g00D_N0isss3_aBIF9j}', 'QCTF{g00D_N0isss3_CaJTSl}', 'QCTF{g00D_N0isss3_tOmrNl}', 'QCTF{g00D_N0isss3_4Y3q6c}', 'QCTF{g00D_N0isss3_U2WPAe}', 'QCTF{g00D_N0isss3_Ln2Y1n}', 'QCTF{g00D_N0isss3_sBIah4}', 'QCTF{g00D_N0isss3_zMER1O}', 'QCTF{g00D_N0isss3_dEVWEm}', 'QCTF{g00D_N0isss3_Z2Hxlh}', 'QCTF{g00D_N0isss3_pd5ceC}', 'QCTF{g00D_N0isss3_VxijOw}', 'QCTF{g00D_N0isss3_fE9E0H}', 'QCTF{g00D_N0isss3_YrquEl}', 'QCTF{g00D_N0isss3_r90sxB}', 'QCTF{g00D_N0isss3_02Rszw}', 'QCTF{g00D_N0isss3_QEfZty}', 'QCTF{g00D_N0isss3_9k6NvY}', 'QCTF{g00D_N0isss3_PYJjdw}', 'QCTF{g00D_N0isss3_TBsglU}', 'QCTF{g00D_N0isss3_8ZEA3s}', 'QCTF{g00D_N0isss3_p6iNzm}', 'QCTF{g00D_N0isss3_xqmIyT}', 'QCTF{g00D_N0isss3_eIWvek}', 'QCTF{g00D_N0isss3_C2cnrd}', 'QCTF{g00D_N0isss3_GdCHIu}', 'QCTF{g00D_N0isss3_eb4ZtG}', 'QCTF{g00D_N0isss3_NYxIhG}', 'QCTF{g00D_N0isss3_6rHEeO}', 'QCTF{g00D_N0isss3_kAJaOe}', 'QCTF{g00D_N0isss3_F8RYb8}', 'QCTF{g00D_N0isss3_1iFpCj}', 'QCTF{g00D_N0isss3_WlUTYC}', 'QCTF{g00D_N0isss3_eGKkR0}', 'QCTF{g00D_N0isss3_nU6MZg}', 'QCTF{g00D_N0isss3_8dmuco}', 'QCTF{g00D_N0isss3_uHbNc4}', 'QCTF{g00D_N0isss3_OIIolE}', 'QCTF{g00D_N0isss3_IESt8P}', 'QCTF{g00D_N0isss3_3NnN3n}', 'QCTF{g00D_N0isss3_XSfWHy}', 'QCTF{g00D_N0isss3_NerCct}', 'QCTF{g00D_N0isss3_gdYmDB}', 'QCTF{g00D_N0isss3_QVLq2h}', 'QCTF{g00D_N0isss3_fBj04l}', 'QCTF{g00D_N0isss3_I9ChLe}', 'QCTF{g00D_N0isss3_2TjUAu}', 'QCTF{g00D_N0isss3_rc7P60}', 'QCTF{g00D_N0isss3_IBLM2q}', 'QCTF{g00D_N0isss3_CeG6qO}', 'QCTF{g00D_N0isss3_q9RCyn}', 'QCTF{g00D_N0isss3_F2rqor}', 'QCTF{g00D_N0isss3_LShMUF}', 'QCTF{g00D_N0isss3_BtZhbF}', 'QCTF{g00D_N0isss3_RzfiKe}', 'QCTF{g00D_N0isss3_AnltCs}', 'QCTF{g00D_N0isss3_oAhECv}', 'QCTF{g00D_N0isss3_PRMOXI}', 'QCTF{g00D_N0isss3_7wQjws}', 'QCTF{g00D_N0isss3_OL8YDQ}', 'QCTF{g00D_N0isss3_vkIb10}', 'QCTF{g00D_N0isss3_jMqlWC}', 'QCTF{g00D_N0isss3_skuZ1h}', 'QCTF{g00D_N0isss3_XmZsYh}', 'QCTF{g00D_N0isss3_0FKEcL}', 'QCTF{g00D_N0isss3_Ky8jzg}', 'QCTF{g00D_N0isss3_pZLUWl}', 'QCTF{g00D_N0isss3_RzDjNd}', 'QCTF{g00D_N0isss3_JOWnzz}', 'QCTF{g00D_N0isss3_sueCxQ}', 'QCTF{g00D_N0isss3_AmMnmU}', 'QCTF{g00D_N0isss3_Yr5QvQ}', 'QCTF{g00D_N0isss3_f6x5HY}', 'QCTF{g00D_N0isss3_qvfQmX}', 'QCTF{g00D_N0isss3_tZLJFE}', 'QCTF{g00D_N0isss3_CVNbdV}', 'QCTF{g00D_N0isss3_U1zHtH}', 'QCTF{g00D_N0isss3_QN8cjQ}', 'QCTF{g00D_N0isss3_WYzWV9}', 'QCTF{g00D_N0isss3_07rqNE}', 'QCTF{g00D_N0isss3_0MVGPJ}', 'QCTF{g00D_N0isss3_aYRKDV}', 'QCTF{g00D_N0isss3_eCiyIV}', 'QCTF{g00D_N0isss3_6WmE4m}', 'QCTF{g00D_N0isss3_B0akLp}', 'QCTF{g00D_N0isss3_4XcPat}', 'QCTF{g00D_N0isss3_Lwzewo}', 'QCTF{g00D_N0isss3_AD5HfG}', 'QCTF{g00D_N0isss3_1pEhcW}', 'QCTF{g00D_N0isss3_L5uh8H}', 'QCTF{g00D_N0isss3_tUo9sO}', 'QCTF{g00D_N0isss3_M8UTi7}', 'QCTF{g00D_N0isss3_XIikkd}', 'QCTF{g00D_N0isss3_Vat8Nn}', 'QCTF{g00D_N0isss3_hY81Nw}', 'QCTF{g00D_N0isss3_LB2Ayd}', 'QCTF{g00D_N0isss3_ldSmDK}', 'QCTF{g00D_N0isss3_wtYZJb}', 'QCTF{g00D_N0isss3_Xk2Ark}', 'QCTF{g00D_N0isss3_jnWMXb}', 'QCTF{g00D_N0isss3_mhOW2e}', 'QCTF{g00D_N0isss3_Wl9DFA}', 'QCTF{g00D_N0isss3_xu02G8}', 'QCTF{g00D_N0isss3_Tc3IRC}', 'QCTF{g00D_N0isss3_HohtpZ}', 'QCTF{g00D_N0isss3_u2HG9m}', 'QCTF{g00D_N0isss3_iDZOS0}', 'QCTF{g00D_N0isss3_FpOR4F}', 'QCTF{g00D_N0isss3_h5vBRZ}', 'QCTF{g00D_N0isss3_81adOh}', 'QCTF{g00D_N0isss3_8r1WmI}', 'QCTF{g00D_N0isss3_S9cfaE}', 'QCTF{g00D_N0isss3_YawxHI}', 'QCTF{g00D_N0isss3_nUfv0m}', 'QCTF{g00D_N0isss3_nXZxn9}', 'QCTF{g00D_N0isss3_NftcHW}', 'QCTF{g00D_N0isss3_K6sQhj}', 'QCTF{g00D_N0isss3_M0j4HB}', 'QCTF{g00D_N0isss3_TRd8yd}', 'QCTF{g00D_N0isss3_FyJVvu}', 'QCTF{g00D_N0isss3_32ZuxE}', 'QCTF{g00D_N0isss3_4bhwMi}', 'QCTF{g00D_N0isss3_bOmGxQ}', 'QCTF{g00D_N0isss3_VXvcpN}', 'QCTF{g00D_N0isss3_2qXM5k}', 'QCTF{g00D_N0isss3_mM4HpX}', 'QCTF{g00D_N0isss3_6PVg7h}', 'QCTF{g00D_N0isss3_lgmspQ}', 'QCTF{g00D_N0isss3_Nggsu5}', 'QCTF{g00D_N0isss3_SUopRv}', 'QCTF{g00D_N0isss3_BbVkUb}', 'QCTF{g00D_N0isss3_UzzxU1}', 'QCTF{g00D_N0isss3_xjaJjg}', 'QCTF{g00D_N0isss3_ielxa0}', 'QCTF{g00D_N0isss3_q0Egy7}', 'QCTF{g00D_N0isss3_4oR22M}', 'QCTF{g00D_N0isss3_D8kD3k}', 'QCTF{g00D_N0isss3_zXk54H}', 'QCTF{g00D_N0isss3_sivLHO}', 'QCTF{g00D_N0isss3_YJPNpf}', 'QCTF{g00D_N0isss3_8defHg}', 'QCTF{g00D_N0isss3_2K7Z0A}', 'QCTF{g00D_N0isss3_R0Kwfo}', 'QCTF{g00D_N0isss3_Jq7Xs4}', 'QCTF{g00D_N0isss3_xSIhh2}', 'QCTF{g00D_N0isss3_cvOimW}', 'QCTF{g00D_N0isss3_GlOJtk}', 'QCTF{g00D_N0isss3_Dib24W}', 'QCTF{g00D_N0isss3_Gq4ibO}', 'QCTF{g00D_N0isss3_KzwPur}', 'QCTF{g00D_N0isss3_Qwrflo}', 'QCTF{g00D_N0isss3_nC3zvG}', 'QCTF{g00D_N0isss3_htqfS9}', 'QCTF{g00D_N0isss3_DhA1sK}', 'QCTF{g00D_N0isss3_Zlkgwz}', 'QCTF{g00D_N0isss3_sFExey}', 'QCTF{g00D_N0isss3_5A9dTG}', 'QCTF{g00D_N0isss3_icNB74}', 'QCTF{g00D_N0isss3_mjqwRz}', 'QCTF{g00D_N0isss3_bWLrzU}', 'QCTF{g00D_N0isss3_Go87iu}', 'QCTF{g00D_N0isss3_MRuxC1}', 'QCTF{g00D_N0isss3_O8B85D}', 'QCTF{g00D_N0isss3_WFRCw2}', 'QCTF{g00D_N0isss3_6QFOM0}', 'QCTF{g00D_N0isss3_YtFXTD}', 'QCTF{g00D_N0isss3_WTtELu}', 'QCTF{g00D_N0isss3_4Jlhif}', 'QCTF{g00D_N0isss3_hkWugN}', 'QCTF{g00D_N0isss3_z26nND}', 'QCTF{g00D_N0isss3_DrcO9D}', 'QCTF{g00D_N0isss3_b4xkxH}', 'QCTF{g00D_N0isss3_NDegIP}', 'QCTF{g00D_N0isss3_zrTIqz}', 'QCTF{g00D_N0isss3_8ngDnK}', 'QCTF{g00D_N0isss3_gW6CJ5}', 'QCTF{g00D_N0isss3_1WXfEU}', 'QCTF{g00D_N0isss3_9vAaDv}', 'QCTF{g00D_N0isss3_IjiGKW}', 'QCTF{g00D_N0isss3_iM5YCQ}', 'QCTF{g00D_N0isss3_yoTpEC}', 'QCTF{g00D_N0isss3_n12odK}', 'QCTF{g00D_N0isss3_FPYTi0}', 'QCTF{g00D_N0isss3_ZmiAns}', 'QCTF{g00D_N0isss3_pbTpms}', 'QCTF{g00D_N0isss3_utOMpN}', 'QCTF{g00D_N0isss3_0zoe1Z}', 'QCTF{g00D_N0isss3_UBPlFw}', 'QCTF{g00D_N0isss3_5Xa7MT}', 'QCTF{g00D_N0isss3_q9xsqZ}', 'QCTF{g00D_N0isss3_7dwKr2}', 'QCTF{g00D_N0isss3_0hGZdd}', 'QCTF{g00D_N0isss3_4lYG30}', 'QCTF{g00D_N0isss3_ZYgcVG}', 'QCTF{g00D_N0isss3_7lCT6Y}', 'QCTF{g00D_N0isss3_ZkVe8t}', 'QCTF{g00D_N0isss3_Gt3sdk}', 'QCTF{g00D_N0isss3_Eu6BCG}', 'QCTF{g00D_N0isss3_CrmReX}', 'QCTF{g00D_N0isss3_LLCTy1}', 'QCTF{g00D_N0isss3_PhYJT1}', 'QCTF{g00D_N0isss3_IbPuSm}', 'QCTF{g00D_N0isss3_ejLbuQ}', 'QCTF{g00D_N0isss3_JxBqDB}', 'QCTF{g00D_N0isss3_uHQMRo}', 'QCTF{g00D_N0isss3_oMSoD3}', 'QCTF{g00D_N0isss3_psifc1}', 'QCTF{g00D_N0isss3_WacQES}', 'QCTF{g00D_N0isss3_xgkZoC}', 'QCTF{g00D_N0isss3_KjgXtN}', 'QCTF{g00D_N0isss3_dmr7g6}', 'QCTF{g00D_N0isss3_iATnzA}', 'QCTF{g00D_N0isss3_pSSDBY}', 'QCTF{g00D_N0isss3_w2yJ9g}', 'QCTF{g00D_N0isss3_n3Jv6Z}', 'QCTF{g00D_N0isss3_mzU2Gq}', 'QCTF{g00D_N0isss3_x4ABsb}', 'QCTF{g00D_N0isss3_b3H8e3}', 'QCTF{g00D_N0isss3_u7q2my}', 'QCTF{g00D_N0isss3_cnDge7}', 'QCTF{g00D_N0isss3_oiQAPj}', 'QCTF{g00D_N0isss3_s6oT4B}', 'QCTF{g00D_N0isss3_5YsYLC}', 'QCTF{g00D_N0isss3_FufBtY}', 'QCTF{g00D_N0isss3_ancdyE}', 'QCTF{g00D_N0isss3_4JjR0X}', 'QCTF{g00D_N0isss3_YoFnmc}', 'QCTF{g00D_N0isss3_suBk23}', 'QCTF{g00D_N0isss3_lkYeYl}', 'QCTF{g00D_N0isss3_0924zE}', 'QCTF{g00D_N0isss3_twgFUR}', 'QCTF{g00D_N0isss3_Z7XG2l}', 'QCTF{g00D_N0isss3_pAFuer}', 'QCTF{g00D_N0isss3_4xqfnm}', 'QCTF{g00D_N0isss3_8MYtF4}', 'QCTF{g00D_N0isss3_yevk6n}', 'QCTF{g00D_N0isss3_9HNZ5r}', 'QCTF{g00D_N0isss3_45xLye}', 'QCTF{g00D_N0isss3_ig3XsX}', 'QCTF{g00D_N0isss3_80EbLi}', 'QCTF{g00D_N0isss3_k1pX0c}', 'QCTF{g00D_N0isss3_Kmt3jd}', 'QCTF{g00D_N0isss3_2la9Cz}', 'QCTF{g00D_N0isss3_gQb5cf}', 'QCTF{g00D_N0isss3_xvZn1R}', 'QCTF{g00D_N0isss3_wnop8G}', 'QCTF{g00D_N0isss3_xSJkA8}', 'QCTF{g00D_N0isss3_L6hplv}', 'QCTF{g00D_N0isss3_ZfTXyx}', 'QCTF{g00D_N0isss3_bnzjAp}', 'QCTF{g00D_N0isss3_0FTW94}', 'QCTF{g00D_N0isss3_8Gd5oi}', 'QCTF{g00D_N0isss3_oIhGWI}', 'QCTF{g00D_N0isss3_eIy1Xl}', 'QCTF{g00D_N0isss3_wCyGQZ}', 'QCTF{g00D_N0isss3_0cLtXQ}', 'QCTF{g00D_N0isss3_ylfy77}', 'QCTF{g00D_N0isss3_5G4NGE}', 'QCTF{g00D_N0isss3_veHYSD}', 'QCTF{g00D_N0isss3_TjlgGD}', 'QCTF{g00D_N0isss3_sGehxo}', 'QCTF{g00D_N0isss3_Z9GRrh}', 'QCTF{g00D_N0isss3_RlKIqm}', 'QCTF{g00D_N0isss3_wEKogc}', 'QCTF{g00D_N0isss3_qkTXQu}', 'QCTF{g00D_N0isss3_PhdYt2}', 'QCTF{g00D_N0isss3_FpTnST}', 'QCTF{g00D_N0isss3_QhMRyT}', 'QCTF{g00D_N0isss3_hLjbax}', 'QCTF{g00D_N0isss3_ToRzGs}', 'QCTF{g00D_N0isss3_qMGe5p}', 'QCTF{g00D_N0isss3_SzRK2o}', 'QCTF{g00D_N0isss3_aaQgQg}', 'QCTF{g00D_N0isss3_2y9x50}', 'QCTF{g00D_N0isss3_WFeaXu}', 'QCTF{g00D_N0isss3_jE9kjM}', 'QCTF{g00D_N0isss3_aNufFL}', 'QCTF{g00D_N0isss3_Armz1R}', 'QCTF{g00D_N0isss3_GsWsLj}', 'QCTF{g00D_N0isss3_DEW22c}', 'QCTF{g00D_N0isss3_zKvFV5}', 'QCTF{g00D_N0isss3_Q2LzS5}', 'QCTF{g00D_N0isss3_wac2bc}', 'QCTF{g00D_N0isss3_obz90g}', 'QCTF{g00D_N0isss3_PjlcBQ}', 'QCTF{g00D_N0isss3_XqwUSP}', 'QCTF{g00D_N0isss3_mUgYDl}', 'QCTF{g00D_N0isss3_wNc4qh}', 'QCTF{g00D_N0isss3_Jj5wm5}', 'QCTF{g00D_N0isss3_ERzOdE}', 'QCTF{g00D_N0isss3_oxdRcC}', 'QCTF{g00D_N0isss3_ir3qGp}', 'QCTF{g00D_N0isss3_K1zM6b}', 'QCTF{g00D_N0isss3_PwSvWS}', 'QCTF{g00D_N0isss3_UlEL8F}', 'QCTF{g00D_N0isss3_y2SXQ8}', 'QCTF{g00D_N0isss3_YhIsko}', 'QCTF{g00D_N0isss3_6qKaYo}', 'QCTF{g00D_N0isss3_WCs6OL}', 'QCTF{g00D_N0isss3_cIw4C2}', 'QCTF{g00D_N0isss3_KNKNXt}', 'QCTF{g00D_N0isss3_A2fnne}', 'QCTF{g00D_N0isss3_RWiZsv}', 'QCTF{g00D_N0isss3_8izARN}', 'QCTF{g00D_N0isss3_1vVO7o}', 'QCTF{g00D_N0isss3_u6GSM1}', 'QCTF{g00D_N0isss3_95NxDt}', 'QCTF{g00D_N0isss3_3Sruhx}', 'QCTF{g00D_N0isss3_jfzkNB}', 'QCTF{g00D_N0isss3_aKL0wJ}', 'QCTF{g00D_N0isss3_I5NNah}', 'QCTF{g00D_N0isss3_encrmO}', 'QCTF{g00D_N0isss3_YhLmwH}', 'QCTF{g00D_N0isss3_KPzvKO}', 'QCTF{g00D_N0isss3_BitdCC}', 'QCTF{g00D_N0isss3_vgnV2h}', 'QCTF{g00D_N0isss3_9RYnWn}', 'QCTF{g00D_N0isss3_czOnD2}', 'QCTF{g00D_N0isss3_lbqlwT}', 'QCTF{g00D_N0isss3_AR1QAK}', 'QCTF{g00D_N0isss3_KKSH5c}', 'QCTF{g00D_N0isss3_RYGF0I}', 'QCTF{g00D_N0isss3_3qojkS}', 'QCTF{g00D_N0isss3_U8qiCK}', 'QCTF{g00D_N0isss3_MaJ1b8}', 'QCTF{g00D_N0isss3_oiyqnt}', 'QCTF{g00D_N0isss3_MLGR6F}', 'QCTF{g00D_N0isss3_jeQm6R}', 'QCTF{g00D_N0isss3_y4rsKY}', 'QCTF{g00D_N0isss3_rrzJwg}', 'QCTF{g00D_N0isss3_eK3enx}', 'QCTF{g00D_N0isss3_nBHTH9}', 'QCTF{g00D_N0isss3_oL2KGt}', 'QCTF{g00D_N0isss3_avD0Y1}', 'QCTF{g00D_N0isss3_68yqgy}', 'QCTF{g00D_N0isss3_7b21kw}', 'QCTF{g00D_N0isss3_9xWghq}', 'QCTF{g00D_N0isss3_zfViGk}', 'QCTF{g00D_N0isss3_oumoks}', 'QCTF{g00D_N0isss3_JlFD2C}', 'QCTF{g00D_N0isss3_2FJsSL}', 'QCTF{g00D_N0isss3_RsIkDP}', 'QCTF{g00D_N0isss3_1XvwOW}', 'QCTF{g00D_N0isss3_L2xDSN}', 'QCTF{g00D_N0isss3_1GaMZe}', 'QCTF{g00D_N0isss3_TL56M2}', 'QCTF{g00D_N0isss3_Dq68vg}', 'QCTF{g00D_N0isss3_2h4ad1}', 'QCTF{g00D_N0isss3_Qe1YIs}', 'QCTF{g00D_N0isss3_4GrEHT}', 'QCTF{g00D_N0isss3_NfZZgq}', 'QCTF{g00D_N0isss3_THUyzv}', 'QCTF{g00D_N0isss3_fNrHMm}', 'QCTF{g00D_N0isss3_grtjeh}', 'QCTF{g00D_N0isss3_YOpUJD}', 'QCTF{g00D_N0isss3_u0Rfse}', 'QCTF{g00D_N0isss3_QnElt1}', 'QCTF{g00D_N0isss3_xvAaH4}', 'QCTF{g00D_N0isss3_PdN7WV}', 'QCTF{g00D_N0isss3_IM0D2c}', 'QCTF{g00D_N0isss3_TRH5iJ}', 'QCTF{g00D_N0isss3_uNZmeL}', 'QCTF{g00D_N0isss3_71GXTY}', 'QCTF{g00D_N0isss3_44FrPa}', 'QCTF{g00D_N0isss3_QRrFgR}', 'QCTF{g00D_N0isss3_b72lKH}', 'QCTF{g00D_N0isss3_qVplnW}', 'QCTF{g00D_N0isss3_Ulzaeo}', 'QCTF{g00D_N0isss3_vGyJgn}', 'QCTF{g00D_N0isss3_xm1We3}', 'QCTF{g00D_N0isss3_emPbZH}', 'QCTF{g00D_N0isss3_OVhOo7}', 'QCTF{g00D_N0isss3_JIZKVQ}', 'QCTF{g00D_N0isss3_DY8Y1S}', 'QCTF{g00D_N0isss3_4XODwA}', 'QCTF{g00D_N0isss3_pstK0V}', 'QCTF{g00D_N0isss3_z0innz}', 'QCTF{g00D_N0isss3_i1uECz}', 'QCTF{g00D_N0isss3_CWIx0S}', 'QCTF{g00D_N0isss3_Xyfhxk}', 'QCTF{g00D_N0isss3_rFPLl8}', 'QCTF{g00D_N0isss3_3AdoSt}', 'QCTF{g00D_N0isss3_1nleTy}', 'QCTF{g00D_N0isss3_DVoGPv}', 'QCTF{g00D_N0isss3_SZZlxu}', 'QCTF{g00D_N0isss3_9aNvmx}']