# POP-LITE
Corpus of Romanian Popular Fiction (1850-1920)

# Description
Contains 100 novels TEI encoded and 23 novels TEI encoded in extension 

# Coordinator
Roxana Patras 

# Editors
Loredana Cuzmici, Lucretia Pascariu, Alexandra Olteanu, Oana Ionescu 

# Contributors
Students of the Faculty of Letters of "Alexandru Ioan Cuza" University of Iași

# Citation suggestion: 
"POP-LITE: Corpus of Romanian Popular Fiction (1850-1920), edited by Roxana Patras, Loredana Cuzmici, Lucretia Pascariu, Alexandra Olteanu, Oana Ionescu, 2024"

# Editing guidelines 

##various fixes (workflow)
1. TEI-XML files have been automatically annotated with RELATE platform: https://relate.racai.ro. We used POS and NER features. 
2. Because NER features have produced suboptimal annotation, we merged RELATE output with RONER model (available via Spacy)
3. Relate TEI-XML files needed revalidation before running RONER
4. We wrote a custom function to aggregate the two layers of annotation: POS & NER

## Automatic corrections
alterations = [('ş', 'ș'), ('ţ', 'ț'), ('Ş', 'Ș'), (' in ', ' în '), (' cînd ', ' când '), (' cind ', ' când '), (' cît ', ' cât '), (' pînă ', ' până '), (' uă ', ' o '), (' maĭ ', ' mai '), (' dînsa ', ' dânsa '), (' ii ', ' îi '), (' dînsul ', ' dânsul '), (' decît ', ' decât '), ('ĭ', 'i'), ('ó', 'oa'), ('ǐ', 'i'), (' quare ', ' care '), (' atît ', ' atât '), (' cîte ', ' câte '), (' chă ', ' că '), (' lîngă ', ' lângă '), ('’', '-'), ("é", "ea"), ('ĕ', 'ă'), ('ç', 'ț'), (' eŭ ', ' eu '), (' mĕ ', ' mă '), (' mîna ', ' mâna '), (' aŭ ', ' au '), (' cîteva ', ' câteva '), (' insă ', ' însă '), (' inse ', ' însă '), (' incă ', ' încă '), (' âncă ', ' încă '), (' inca ', ' încă '), (' insa ', ' însă '), (' sě ', ' să '), (' dînșii ', ' dânșii '), (' dînsei ', ' dânsei '), (' încît ', ' încât '), (' atîtea ', ' atâtea '), (' șcii ', ' știi '), (' șciu ', ' știu '), (' nișce ', ' niște '), (' Bucureșci ', ' București '), (' erà ', ' era '), (' ell ', ' el '), ('înd ', 'ând '), ('ȡ', 'z'), ('ᶁ', 'z'), ('ḑ', 'z'), ('ĕ', 'ă'), ('ŭ', 'u'), ('ê', 'â'), ('’', '-'), (' ȡi ', ' zi '), (' chăci ', ' căci '), (' p ', ' pe '), (' ii ', ' îi '), (' d ', ' de '), (' ă ', ' '), (' t ', ' te '), (' l ', ' le '), (' n ', ' nu '), (' as ', ' aș '), (' ma ', ' mă '), (' il ', ' îl '), (' ti ', ' -ți '), (' intr-o ', ' într-o '), (' intr-un ', ' într-un '), (' zisse', ' zise '), (' iși ', ' își '), (' v ', ' v- '), (' iți ', ' îți '), (' imi ', ' îmi '), (' c ', ' c- '), (' toti ', ' toți '), (' dupa ', ' după '), (' tote ', ' toate '), (' è ', ' e '), (' u ', ' '), (' it ', ' îl '), (' mě ', ' mă '), (' r ', ' '), (' asa ', ' așa '), (' iii ', ' îi '), (' ul ', ' îl '), (' iui ', ' lui '), (' î ', ' în '), (' us ', ' '), (' fat ', ' fată '), (' înt ', ' într '), (' inainte ', ' înainte '), (' erá ', ' era '), (' odata ', ' odată '), (' b ', ' '), (' căte ', ' câte '), (' ile ', ' ele '), (' cit ', ' cât '), (' cat ', ' cât '), (' mia ', ' mi-a '), (' sâ ', ' să '), (' toii ', ' toiu '), (' incepu ', ' începu '), (' șl ', ' și '), (' salle ', ' sale '), (' oras ', ' oraș '), (' lingă ', ' lângă '), (' faca ', ' facă '), (' totă ', ' toată '), (' acèsta ', ' aceasta '), (' g ', ' '), (' all ', ' al '), (' cc ', ' că '), (' vedi ', ' vezi '), (' sa-i ', ' să-i '), (' lom ', ' lor '), (' ell ', ' el '), (' dile ', ' zile '), (' hot ', ' hoț '), (' șă ', ' să '), (' f ', ' '), (' j ', ' '), (' is ', ' îs '), (' indată ', ' îndată '), (' alle ', ' ale '), (' melle ', ' mele '), (' totusi ', ' totuși '), (' dis ', ' zis '), (' ómeni ', ' oameni '), (' d-ze ', ' dumnezeu '), (' sa-l ', ' să-l '), (' vădu ', ' văzu '), (' tie ', ' ție '), (' nostre ', ' noastre '), (' luâ ', ' luă '), (' să-t ', ' să-ți ')]
