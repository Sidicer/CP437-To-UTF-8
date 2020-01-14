# Pabandome atsidaryti įrašymo failą kaip binarinį (ne tekstinį)
# output file: Recoded386intel.txt
# input file: 386intel.txt

with open('Recoded386intel.txt','wb') as f: # "f" - atidaryto failo kintamasis, "wb" - Write Binary Mode
    f.write(bytes(range(256)))              # Užpildome baitais nuo 0 iki 255

# Atidarius 'Recoded386intel.txt' failą matome
# visus galimus simbolius nuo 0 iki 255
#
# Tai reiškia, kad sėkmingai įrašėme binariniu būdu,
# todėl galime eiti prie perkodavimo:

# Veiksmų seka:
#
# Nuskaitysime turimą '386intel.txt' failą su code page 437 kodavimu (DOS OEM-US).
# Įrašysime į naują failą su UTF-8 kodavimu ("Unicode" nėra koduotė)

with open('386intel.txt',encoding='cp437') as infile:                   # 'with' - kol dirbame su failu; 
                                                                        # 'encoding' - nurodome kokios koduotės tikimės nuskaitydami;
    with open('Recoded386intel.txt','w',encoding='utf8') as outfile:    # Nurodome kad išvesties failas bus utf-8 koduotės ir atidarome jį 'write' būdu
        outfile.write(infile.read())                                    # Įrašome į išvesties failą tai ką nuskaitome įvesties faile
# išvesties failas <- įrašyti <- įvesties failas <- nuskaityti
