KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        for i in range(self.alkioiden_lkm):
            if n == self.ljono[i]:
                return True
        return False

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        self._varmista_tila()
        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1
        return True

    def _varmista_tila(self):
        if self.alkioiden_lkm < len(self.ljono):
            return

        vanha_lista = self.ljono
        uusi_koko = len(vanha_lista) + self.kasvatuskoko
        if uusi_koko == len(vanha_lista):
            uusi_koko += 1
        self.ljono = self._luo_lista(uusi_koko)
        self.kopioi_lista(vanha_lista, self.ljono)

    def poista(self, n):
        for indeksi in range(self.alkioiden_lkm):
            if self.ljono[indeksi] == n:
                self._siirra_alkiot_vasemmalle(indeksi)
                self.alkioiden_lkm -= 1
                self.ljono[self.alkioiden_lkm] = 0
                return True
        return False

    def _siirra_alkiot_vasemmalle(self, alku):
        for indeksi in range(alku, self.alkioiden_lkm - 1):
            self.ljono[indeksi] = self.ljono[indeksi + 1]

    def kopioi_lista(self, a, b):
        for i in range(min(len(a), len(b))):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)
        for i in range(self.alkioiden_lkm):
            taulu[i] = self.ljono[i]
        return taulu

    def __str__(self):
        alkiot = (str(self.ljono[i]) for i in range(self.alkioiden_lkm))
        return "{" + ", ".join(alkiot) + "}"

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z
