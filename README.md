# Offer Trin Iaith

Casgliad o sgriptiau ar gyfer hwyluso trin agweddau o destunau Cymraeg, gan gynnwys gweithredu treigladau, lluosogi geiriau Cymraeg, a chyfrif y nifer o lythrennau Cymraeg sydd mewn gair Cymraeg, gan gyfrif deugraffau fel 'll' a 'ch' fel un llythyren yn unig.

*A collection of scripts to facilitate the manipulation of Welsh texts, including the mutation of Welsh words, forming plural forms of Welsh words, and counting the number of Welsh letters in a word, where digraphs such as 'll' and 'ch' count as a single letter.*

## mutate.py

Mae'r ffeil `mutate.py` yn cynnwys casgliad o ffwythiannau ar gyfer treiglo geiriau Cymraeg, gan gynnws ffwythiannau unigol ar gyfer peri treigladau meddal, llaes a thrwynol.

*The file `mutate.py` contains a collection of Python functions for mutating Welsh words, and includes separate functions for soft, aspirate and nasal mutations.*

## pluralize.py

Mae'r ffeil `pluralize.py` yn dangos sut i ddefnyddio'r ffeil sing2plur.json i luosogi ffurfiau unigol, e.e. i droi 'iâr' yn 'ieir'.

*The file `pluralize.py` demonstrates how to use sing2plur.json to pluralize singular Welsh forms, and turn 'iâr' ('hen') into 'ieir' ('hens').*

## welsh_letters.py

Mae `welsh_letters.py` yn darparu gwybodaeth hwylus am yr wyddor Gymraeg, gan gynnwys dull o gyfrif nifer y llythrennau Cymraeg a geir mewn gair, fel bod 'llaeth' yn air 4 llythyren yn hytrach na gair chwe llythyren.

*The file `welsh_letters.py` provides useful information abouth the Welsh alphabet, including a method for counting the occurence of Welsh letters in a word, so that 'llaeth' counts as a 4 letter word rather than a 6 letter word.*
