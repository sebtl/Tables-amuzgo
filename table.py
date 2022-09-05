import pandas as pd


df = pd.read_excel('amuzgo_tables.xlsx')
i = 0
for index in range(1994):
    amuzgo = (df.iloc[i,0])
    ton_0 = (df.iloc[i,1])
    esp = (df.iloc[i,2])

    pasado_0 = (df.iloc[i,3])
    ton_1 = (df.iloc[i,4])
    pasado_1 = (df.iloc[i,5])
    ton_2 = (df.iloc[i,6])
    pasado_2 = (df.iloc[i,7])
    ton_3 = (df.iloc[i,8])
    pasado_3 = (df.iloc[i,9])
    ton_4 = (df.iloc[i,10])
    pasado_4 = (df.iloc[i,11])
    ton_5 = (df.iloc[i,12])
    pasado_5 = (df.iloc[i,13])
    ton_6 = (df.iloc[i,14])
    pasado_6 = (df.iloc[i,15])
    ton_7 = (df.iloc[i,16])

    presente_0 = (df.iloc[i,17])
    ton_8 = (df.iloc[i,18])
    presente_1 = (df.iloc[i,19])
    ton_9 = (df.iloc[i,20])
    presente_2 = (df.iloc[i,21])
    ton_10 = (df.iloc[i,22])
    presente_3 = (df.iloc[i,23])
    ton_11 = (df.iloc[i,24])
    presente_4 = (df.iloc[i,25])
    ton_12 = (df.iloc[i,26])
    presente_5 = (df.iloc[i,27])
    ton_13 = (df.iloc[i,28])
    presente_6 = (df.iloc[i,29])
    ton_14 = (df.iloc[i,30])

    futuro_0 = (df.iloc[i,31])
    ton_15 = (df.iloc[i,32])
    futuro_1 = (df.iloc[i,33])
    ton_16 = (df.iloc[i,34])
    futuro_2 = (df.iloc[i,35])
    ton_17 = (df.iloc[i,36])
    futuro_3 = (df.iloc[i,37])
    ton_18 = (df.iloc[i,38])
    futuro_4 = (df.iloc[i,39])
    ton_19 = (df.iloc[i,40])
    futuro_5 = (df.iloc[i,41])
    ton_20 = (df.iloc[i,42])
    futuro_6 = (df.iloc[i,43])
    ton_21 = (df.iloc[i,44])


    subjuntivo_0 = (df.iloc[i,45])
    ton_22 = (df.iloc[i,46])
    subjuntivo_1 = (df.iloc[i,47])
    ton_23 = (df.iloc[i,48])
    subjuntivo_2 = (df.iloc[i,49])
    ton_24 = (df.iloc[i,50])
    subjuntivo_3 = (df.iloc[i,51])
    ton_25 = (df.iloc[i,52])
    subjuntivo_4 = (df.iloc[i,53])
    ton_26 = (df.iloc[i,54])
    subjuntivo_5 = (df.iloc[i,55])
    ton_27 = (df.iloc[i,56])
    subjuntivo_6 = (df.iloc[i,57])
    ton_28 = (df.iloc[i,58])



    pasado_con_fre_0 = (df.iloc[i,59])
    ton_29 = (df.iloc[i,60])
    pasado_con_fre_1 = (df.iloc[i,61])
    ton_30 = (df.iloc[i,62])
    pasado_con_fre_2 = (df.iloc[i,63])
    ton_31 = (df.iloc[i,64])
    pasado_con_fre_3 = (df.iloc[i,65])
    ton_32 = (df.iloc[i,66])
    pasado_con_fre_4 = (df.iloc[i,67])
    ton_33 = (df.iloc[i,68])
    pasado_con_fre_5 = (df.iloc[i,69])
    ton_34 = (df.iloc[i,70])
    pasado_con_fre_6 = (df.iloc[i,71])
    ton_35 = (df.iloc[i,72])


    futuro_con_0 = (df.iloc[i,73])
    ton_36 = (df.iloc[i,74])
    futuro_con_1 = (df.iloc[i,75])
    ton_37 = (df.iloc[i,76])
    futuro_con_2 = (df.iloc[i,77])
    ton_38 = (df.iloc[i,78])
    futuro_con_3 = (df.iloc[i,79])
    ton_39 = (df.iloc[i,80])
    futuro_con_4 = (df.iloc[i,81])
    ton_40 = (df.iloc[i,82])
    futuro_con_5 = (df.iloc[i,83])
    ton_41 = (df.iloc[i,84])
    futuro_con_6 = (df.iloc[i,85])
    ton_42 = (df.iloc[i,86])
    with open('tables_latex.txt','a',encoding='UTF-8') as file:
        file = file.write('/begin{table}[H]\n/begin{tabular}{@{}lll@{}}\n/toprule\n/multicolumn{3}{c}{/textbf{/begin{tabular}[c]{@{}c@{}}'+amuzgo+' '+ton_0+'\n// '+esp+'/end{tabular}}} /index{'+amuzgo+', '+esp+'}                                                                                                                                                                                                                                                                         // /midrule //\n/rowcolor[HTML]{EFEFEF} \n                                                                                                         & {/color[HTML]{000000} Pasado}                                                                                                         & {/color[HTML]{000000} Presente}                                                                             ////\n{/color[HTML]{000000} /begin{tabular}[c]{@{}l@{}}1 SG//2 SG//3 SG\n//1 PL.INCL//1 PL.EXCL//2 PL//3 PL/end{tabular}} & {/color[HTML]{000000} /begin{tabular}[c]{@{}l@{}}'+pasado_0+' '+ton_1+' \n// '+pasado_1+' '+ton_2+'\n// '+pasado_2+' '+ton_3+'\n// '+pasado_3+' '+ton_4+'\n// '+pasado_4+' '+ton_5+'\n// '+pasado_5+' '+ton_6+'\n// '+pasado_6+' '+ton_7+'\n/end{tabular}} & /begin{tabular}[c]{@{}l@{}}'+presente_0+' '+ton_8+'\n// '+presente_1+' '+ton_9+'\n// '+presente_2+' '+ton_10+'\n// '+presente_3+' '+ton_11+'\n// '+presente_4+' '+ton_12+'\n// '+presente_5+' '+ton_13+'\n// '+presente_6+' '+ton_14+'\n/end{tabular} ////\n/rowcolor[HTML]{EFEFEF} \n                                                                                                         & {/color[HTML]{000000} Futuro}                                                                                                     & /cellcolor[HTML]{EFEFEF}{/color[HTML]{000000} Subjuntivo}                                                       ////\n{/color[HTML]{000000} /begin{tabular}[c]{@{}l@{}}1 SG//2 SG//3 SG\n//1 PL.INCL//1 PL.EXCL//2 PL//3 PL/end{tabular}} & /begin{tabular}[c]{@{}l@{}}'+futuro_0+' '+ton_15+'\n// '+futuro_1+' '+ton_16+'\n// '+futuro_2+' '+ton_17+'\n// '+futuro_3+' '+ton_18+'\n// '+futuro_4+' '+ton_19+'\n// '+futuro_5+' '+ton_20+'\n// '+futuro_6+' '+ton_21+'\n/end{tabular}                           & /begin{tabular}[c]{@{}l@{}}'+subjuntivo_0+' '+ton_22+'\n// '+subjuntivo_1+' '+ton_23+'\n// '+subjuntivo_2+' '+ton_24+'\n// '+subjuntivo_3+' '+ton_25+'\n// '+subjuntivo_4+' '+ton_26+'\n// '+subjuntivo_5+' '+ton_27+'\n// '+subjuntivo_6+' '+ton_28+'\n/end{tabular} ////\n/rowcolor[HTML]{EFEFEF} \n/cellcolor[HTML]{EFEFEF}                                                                                 & {/color[HTML]{000000} /begin{tabular}[c]{@{}l@{}}Pasado con// frecuencia/end{tabular}}                                                & {/color[HTML]{000000} /begin{tabular}[c]{@{}l@{}}Futuro// continuativo/end{tabular}}                        ////\n{/color[HTML]{000000} /begin{tabular}[c]{@{}l@{}}1 SG//2 SG//3 SG\n//1 PL.INCL//1 PL.EXCL//2 PL//3 PL/end{tabular}} & /begin{tabular}[c]{@{}l@{}}'+pasado_con_fre_0+' '+ton_29+'\n// '+pasado_con_fre_1+' '+ton_30+'\n// '+pasado_con_fre_2+' '+ton_31+'\n// '+pasado_con_fre_3+' '+ton_32+'\n// '+pasado_con_fre_4+' '+ton_33+'\n// '+pasado_con_fre_5+' '+ton_34+'\n// '+pasado_con_fre_6+' '+ton_35+'\n/end{tabular}                           & /begin{tabular}[c]{@{}l@{}}\n'+futuro_con_0+' '+ton_36+'\n// '+futuro_con_1+' '+ton_37+'\n// '+futuro_con_2+' '+ton_38+'\n// '+futuro_con_3+' '+ton_39+'\n// '+futuro_con_4+' '+ton_40+'\n// '+futuro_con_5+' '+ton_41+'\n// '+futuro_con_6+' '+ton_42+'\n/end{tabular} //// /bottomrule\n/end{tabular}\n/end{table}\n\n%TABLE\n\n')
    i+=1

# Effectuer les changements suivants sur le fichier de sortie 'tables_latex.txt' pour respecter le format Latex
# '/' --> \
# 'ⁿ' --> \textsuperscript{n}
# 'Ầ' --> \gravis{Â}
# 'Ấ' --> \acutus{Â}
# 'Ế' --> \acutus{Ê}
# 'ệ' --> \d{ê}
# 'ộ' --> \d{ô}
# 'ậ' --> \d{â}
# 'Ǻ' --> \acutus{Å}
# 'ữ' --> \~{\uhorn}
# 'ề' --> \gravis{ê}
# 'ồ' --> \gravis{ô}
# 'Ǚ' --> \diaeresis{\v{U}}











