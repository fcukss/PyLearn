"""
В небольшом городе население p0 = 1000в начале года.
 Население регулярно увеличивается на 2 percentв год,
 и, кроме того, 50 в город ежегодно приезжают новые жители.
 Сколько лет нужно городу, чтобы его население стало больше
 или равно количеству жителей p = 1200?

 At the end of the first year there will be:
1000 + 1000 * 0.02 + 50 => 1070 inhabitants

At the end of the 2nd year there will be:
1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

At the end of the 3rd year there will be:
1141 + 1141 * 0.02 + 50 => 1213

It will need 3 entire years.
"""


def nb_year(p0, percent, aug, p):
    percent /= 100
    year=0

    while p >= p0:
        p0 = p0+p0*percent+aug
        year+=1
    return year


print(nb_year(1500, 5, 100, 5000))
