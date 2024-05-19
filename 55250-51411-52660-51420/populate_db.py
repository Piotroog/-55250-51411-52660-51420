from aplikacja_ang.models import Slowko

slownik_polsko_angielski = [

]



obiekty_slowko = [Slowko(polskie=par[0], angielskie=par[1]) for par in slownik_polsko_angielski]

Slowko.objects.bulk_create(obiekty_slowko)