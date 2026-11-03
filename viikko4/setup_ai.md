# Poistiko agentti toisteisuuden mielestäsi järkevästi? Onko testikoodi nyt helpommin luettavaa?

- Kyllä ainakin jos sitäa arvioidaan rivi määrän ja toisteisuuden perusteella. Koodi on nyt paremmin seurattavissa jos halutaan päättää muuttaa alustamista tarvitsee muuttaa vain yhtä paikkaa usean sijasta.

# Muuttiko agentti testien toiminnallisuutta, esim. poistiko tai heikensikö se tarkistuksia (assert_called_with vs. assert_called)?

- Kaikki assert-kutsut säilyivät samana ja testin coverage ei muuttunut paremmaksi tai huonommaksi, refaktorointi koodille oli ainut tavoite ja se toteutui. assert_called_with on mielestäni oikea vaihtoehto tässä testitilanteessa.

# Jouduitko korjaamaan agentin tekemiä muutoksia itse tai pyytämään siltä muutoksia? Mitä ja miksi?

- En joutunut ohjaamaan agenttia tai sen muutoksia varmaan siitä syystä että se pystyy yksinkertaisen tehtävän saamaan valmiiksi melko helposti.
