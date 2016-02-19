#!/usr/bin/python
# -*- coding: utf-8 -*-

LANGUAGE = 'pl'
TRIM_START = 0.0
TRIM_END = 0.7


class Phrase(object):
    def __init__(self, text, sounds_like=None, save_as=None):
        self.text = text
        self.sounds_like = text if sounds_like is None else sounds_like
        self.save_as = self._as_filename(text) if save_as is None else save_as

    @staticmethod
    def _as_filename(phrase):
        return phrase.lower()\
            .replace(u" ", "_")\
            .replace(u"ą", "a")\
            .replace(u"ć", "c")\
            .replace(u"ę", "e")\
            .replace(u"ł", "l")\
            .replace(u"ń", "n")\
            .replace(u"ó", "o")\
            .replace(u"ś", "s")\
            .replace(u"ź", "z")\
            .replace(u"ż", "z")


phrases = (
    # welcome and goodbye messages
    Phrase(u"tu eksperymentalna automatyczna stacja pogodowa"),
    Phrase(u"tu automatyczna stacja pogodowa"),
    Phrase(u"stanisław roman zero wanda ksawery", save_as="sr0wx"),
    Phrase(u"tu stanisław roman zero wanda ksawery", save_as="tu_sr0wx"),

    Phrase(u"stan pogody z dnia"),
    Phrase(u"stan pogody z godziny"),
    Phrase(u"jutro"),

    Phrase(u"pierwszego"),
    Phrase(u"drugiego"),
    Phrase(u"trzeciego"),
    Phrase(u"czwartego"),
    Phrase(u"piątego"),
    Phrase(u"szóstego"),
    Phrase(u"siódmego"),
    Phrase(u"ósmego"),
    Phrase(u"dziewiątego"),
    Phrase(u"dziesiątego"),
    Phrase(u"jedenastego"),
    Phrase(u"dwunastego"),
    Phrase(u"trzynastego"),
    Phrase(u"czternastego"),
    Phrase(u"piętnastego"),
    Phrase(u"szesnastego"),
    Phrase(u"siedemnastego"),
    Phrase(u"osiemnastego"),
    Phrase(u"dziewiętnastego"),
    Phrase(u"dwudziestego"),
    Phrase(u"trzydziestego"),

    Phrase(u"stycznia"),
    Phrase(u"lutego"),
    Phrase(u"marca"),
    Phrase(u"kwietnia"),
    Phrase(u"maja"),
    Phrase(u"czerwca"),
    Phrase(u"lipca"),
    Phrase(u"sierpnia"),
    Phrase(u"września"),
    Phrase(u"października"),
    Phrase(u"listopada"),
    Phrase(u"grudnia"),

    Phrase(u"zero"),
    Phrase(u"zero zero"),
    Phrase(u"jeden"),
    Phrase(u"dwa"),
    Phrase(u"trzy"),
    Phrase(u"cztery"),
    Phrase(u"pięć"),
    Phrase(u"sześć"),
    Phrase(u"siedem"),
    Phrase(u"osiem"),
    Phrase(u"dziewięć"),
    Phrase(u"dziesięć"),
    Phrase(u"jedenaście"),
    Phrase(u"dwanaście"),
    Phrase(u"trzynaście"),
    Phrase(u"czternaście"),
    Phrase(u"piętnaście"),
    Phrase(u"szesnaście"),
    Phrase(u"siedemnaście"),
    Phrase(u"osiemnaście"),
    Phrase(u"dziewiętnaście"),
    Phrase(u"dwadzieścia"),
    Phrase(u"trzydzieści"),
    Phrase(u"czterdzieści"),
    Phrase(u"pięćdziesiąt"),
    Phrase(u"sześćdziesiąt"),
    Phrase(u"siedemdziesiąt"),
    Phrase(u"osiemdziesiąt"),
    Phrase(u"dziewięćdziesiąt"),
    Phrase(u"sto"),
    Phrase(u"dwieście"),
    Phrase(u"trzysta"),
    Phrase(u"czterysta"),
    Phrase(u"pięćset"),
    Phrase(u"sześćset"),
    Phrase(u"siedemset"),
    Phrase(u"osiemset"),
    Phrase(u"dziewięćset"),
    Phrase(u"tysiąc"),

    Phrase(u"źródło"),

    # różne
    Phrase(u"temperatura"),
    Phrase(u"stopień celsjusza"),
    Phrase(u"minus"),
    Phrase(u"stopnie celsjusza"),
    Phrase(u"stopni celsjusza"),
    Phrase(u"wiatr"),
    Phrase(u"północny"),
    Phrase(u"północno"),
    Phrase(u"wschodni"),
    Phrase(u"wschodnio"),
    Phrase(u"zachodni"),
    Phrase(u"zachodnio"),
    Phrase(u"południowy"),
    Phrase(u"południowo"),
    Phrase(u"wilgotność"),
    Phrase(u"procent"),
    Phrase(u"prędkość wiatru"),
    Phrase(u"metr na sekundę"),
    Phrase(u"metrów na sekundę"),
    Phrase(u"stopień"),
    Phrase(u"stopnie"),
    Phrase(u"stopni"),
    Phrase(u"widoczność"),
    Phrase(u"kilometr"),
    Phrase(u"kilometry"),
    Phrase(u"kilometrów"),
    Phrase(u"temperatura odczuwalna"),
    Phrase(u"prognoza na następne"),
    Phrase(u"godzin"),
    Phrase(u"godzina"),
    Phrase(u"godziny"),
    Phrase(u"temperatura od"),

    Phrase(u"pierwsza"),
    Phrase(u"druga"),
    Phrase(u"trzecia"),
    Phrase(u"czwarta"),
    Phrase(u"piąta"),
    Phrase(u"szósta"),
    Phrase(u"siódma"),
    Phrase(u"ósma"),
    Phrase(u"dziewiąta"),
    Phrase(u"dziesiąta"),
    Phrase(u"jedenasta"),
    Phrase(u"dwunasta"),
    Phrase(u"trzynasta"),
    Phrase(u"czternasta"),
    Phrase(u"piętnasta"),
    Phrase(u"szesnasta"),
    Phrase(u"siedemnasta"),
    Phrase(u"osiemnasta"),
    Phrase(u"dziewiętnasta"),
    Phrase(u"dwudziesta"),

    Phrase(u"kierunek wiatru"),
    Phrase(u"metry na sekundę"),
    Phrase(u"metrów na sekundę"),
    Phrase(u"kilometr na godzinę"),
    Phrase(u"kilometry na godzinę"),
    Phrase(u"kilometrów na godzinę"),

    Phrase(u"ciśnienie"),
    Phrase(u"hektopaskal"),
    Phrase(u"hektopaskale"),
    Phrase(u"hektopaskali"),
    Phrase(u"tendencja spadkowa"),
    Phrase(u"tendencja wzrostowa"),
    Phrase(u"temperatura odczuwalna"),
    Phrase(u"temperatura minimalna"),
    Phrase(u"maksymalna"),
    Phrase(u"następnie"),

    # literowanie polskie wg. "Krótkofalarstwo i radiokomunikacja - poradnik",
    # Łukasz Komsta SQ8QED, Wydawnictwa Komunikacji i Łączności Warszawa, 2001,
    # str. 130 (z drobnymi modyfikacjami fonetycznymi)

    Phrase(u"adam", save_as='a'),
    Phrase(u"barbara", save_as='b'),
    Phrase(u"celina", save_as='c'),
    Phrase(u"dorota", save_as='d'),
    Phrase(u"edward", save_as='e'),
    Phrase(u"franciszek", save_as='f'),
    Phrase(u"gustaw", save_as='g'),
    Phrase(u"henryk", save_as='h'),
    Phrase(u"irena", save_as='i'),
    Phrase(u"józef", save_as='j'),
    Phrase(u"karol", save_as='k'),
    Phrase(u"ludwik k", save_as='l'),
    Phrase(u"marek k", save_as='m'),
    Phrase(u"natalia", save_as='n'),
    Phrase(u"olga", save_as='o'),
    Phrase(u"paweł", save_as='p'),
    Phrase(u"kłebek", save_as='q'),  # wł. Quebec
    Phrase(u"roman", save_as='r'),
    Phrase(u"stefan", save_as='s'),
    Phrase(u"tadeusz", save_as='t'),
    Phrase(u"urszula", save_as='u'),
    Phrase(u"violetta", save_as='v'),
    Phrase(u"wacław", save_as='w'),
    Phrase(u"xawery", save_as='x'),
    Phrase(u"ypsylon", save_as='y'),  # wł. Ypsilon
    Phrase(u"zygmunt", save_as='z'),
    Phrase(u"łamane"),

    # Phrase dla WorldWeatherOnline

    Phrase(u"bezchmurnie"),
    Phrase(u"burza"),
    Phrase(u"burza śnieżna"),
    Phrase(u"częściowe zachmurzenie"),
    Phrase(u"grad"),
    Phrase(u"intensywne opady śniegu"),
    Phrase(u"lokalna przelotna marznąca mżawka",
           sounds_like=u"lokalna przelotna mar-znąca mżawka"),
    Phrase(u"lokalne burze"),
    Phrase(u"lokalne przelotne opady deszczu"),
    Phrase(u"lokalny słaby deszcz"),
    Phrase(u"marznąca mgła",
           sounds_like=u"mar-znąca mgła"),
    Phrase(u"marznąca mżawka",
           sounds_like=u"mar-znąca mżawka"),
    Phrase(u"mgła"),
    Phrase(u"mżawka"),
    Phrase(u"opady śniegu"),
    Phrase(u"pochmurno"),
    Phrase(u"przelotne opady deszczu"),
    Phrase(u"przelotne ulewy"),
    Phrase(u"słabe opady marznącego deszczu",
           sounds_like=u"słabe opady marznącego deszczu"),
    Phrase(u"słabe opady śniegu"),
    Phrase(u"słabe opady śniegu z deszczem"),
    Phrase(u"słabe opady śniegu ziarnistego"),
    Phrase(u"słabe przelotne opady deszczu"),
    Phrase(u"słaby deszcz"),
    Phrase(u"śnieg"),
    Phrase(u"śnieg z deszczem"),
    Phrase(u"ulewny deszcz"),
    Phrase(u"ulewy"),
    Phrase(u"umiarkowane lub ciężkie opady śniegu z deszczem"),
    Phrase(u"umiarkowane opady deszczu"),
    Phrase(u"umiarkowane opady marznącego deszczu",
           sounds_like=u"umiarkowane opady marznącego deszczu"),
    Phrase(u"umiarkowane opady śniegu"),
    Phrase(u"umiarkowane opady śniegu z deszczem"),
    Phrase(u"umiarkowane opady śniegu ziarnistego"),
    Phrase(u"zachmurzenie całkowite"),
    Phrase(u"zamglenia"),
    Phrase(u"zamieć śnieżna"),
    Phrase(u"pokrywa chmur"),
    Phrase(u"World Weather Online",
           sounds_like=u"łorld łeder onlajn",
           save_as="worldweatheronline"),
)
