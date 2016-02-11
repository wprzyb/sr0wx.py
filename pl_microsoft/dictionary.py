#!/usr/bin/python
# -*- coding: utf-8 -*-

# Caution! I am not responsible for using these samples. Use at your own risk
# Google, Inc. is the copyright holder of samples downloaded with this tool.
#
# Unfortunatelly, Google gives no license text for these samples. I hope
# they're made with free (beer)/open source/free (freedom) software,
# but I have no idea.

# This is the GENERAL download list and settings for polish language

LANGUAGE = 'pl'

CUT_START = 0.0
CUT_END = 0.1

LONG_CUT_START = 0.570
LONG_CUT_END = 0.42

TEMPO = 1.0

CUT_PREFIX = 'ę. '
CUT_SUFFIX = ' k'

download_list = [
    # welcome and goodbye messages
    ["tu eksperymentalna automatyczna stacja pogodowa k"],
    ["tu automatyczna stacja pogodowa powiatu brzeskiego"],
    ["tu automatyczna stacja pogodowa powiatu prudnickiego"],


    ["tu automatyczna stacja pogodowa powiatu olsztyniskiego",
        "tu_automatyczna_stacja_pogodowa_powiatu_olsztynskiego"],

    ["ę. Stanisław Paweł 6 Jokohama Roman, Ewa", "sp6yre"],
    ["ę. stanisław kłebek 6 jadwiga natalia kłebek ", "sq6jnq"],
    ["ę. stanisław kłebek 6 adam cezary maria", "sq6acm"],
    ["ę. stanisław paweł 6 karol ewa olga", "sp6keo"],


    ["tu Stanisław Paweł 6 Jokohama Roman, Ewa", 'tu_sp6yre'],
    ["tu stanisław kłebek 6 jadwiga natalia kłebek k", 'tu_sq6jnq'],
    ["tu stanisław kłebek 6 adam cezary maria", 'tu_sq6acm'],
    ["tu stanisław paweł 6 karol ewa olga", "tu_sp6keo"],

    ["stan pogody z dnia k"],
    ["stan pogody z godziny"],

    ["pierwszego"], ["drugiego"], ["trzeciego"], ["czwartego"],
    ["piątego"], ["szóstego"], ["siódmego"],
    ["ę. ósmego", 'osmego'], ["dziewiątego"], ["dziesiątego"],
    ["jedenastego"], ["dwunastego"],
    ["trzynastego"], ["czternastego"], ["piętnastego"],
    ["szesnastego"], ["siedemnastego"], ["osiemnastego"],
    ["dziewiętnastego"], ["dwudziestego"], ["trzydziestego"],

    ["stycznia"],
    ["lutego"], ["marca"], ["kwietnia"], ["maja"], ["czerwca"],
    ["lipca"], ["sierpnia"], ["września"], ["października"],
    ["listopada"], ["grudnia"],

    ["zero"],
    ["zero zero"], ["jeden"],
    ["dwa"], ["trzy"], ["cztery"], ["pięć"], ["sześć"],
    ["siedem"], ["osiem"], ["dziewięć"], ["dziesięć"],
    ["jedenaście"], ["dwanaście"], ["trzynaście"],
    ["czternaście"], ["piętnaście"], ["szesnaście"],
    ["siedemnaście"], ["osiemnaście"], ["dziewiętnaście"],
    ["dwadzieścia"], ["trzydzieści"], ["czterdzieści"],
    ["pięćdziesiąt"], ["sześćdziesiąt"], ["siedemdziesiąt"],
    ["osiemdziesiąt"], ["dziewięćdziesiąt"], ["sto"],
    ["dwieście"], ["trzysta"], ["czterysta"], ["pięćset"],
    ["sześćset"], ["siedemset"], ["osiemset"], ["dziewięćset"],
    ["tysiąc"],

    ["źródło"],

    # różne
    ["temperatura"], ["stopień celsjusza"],
    ["minus"], ["stopnie celsjusza"], ["stopni celsjusza"],
    ["kierunek wiatr"], ["północny"], ["północno"], ["wschodni"],
    ["wschodnio"], ["zachodni"], ["zachodnio"], ["południowy"],
    ["południowo"], ["wilgotność"], ["procent"], ["prędkość wiatru"],
    ["metr na sekundę"], ["metrów na sekundę"],
    ["stopień"], ["stopnie"], ["stopni"],
    ["widoczność"], ["kilometr"], ["kilometry"],
    ["kilometrów"], ["temperatura odczuwalna"],
    ["prognoza na następne"], ["godzin"], ["godzina"],
    ["godziny"], ["temperatura od"],

    ["pierwsza"], ["druga"], ["trzecia"], ["czwarta"], ["piąta"],
    ["szósta"], ["siódma"], ["ósma", "osma"], ["dziewiąta"], ["dziesiąta"],
    ["jedenasta"], ["dwunasta"], ["trzynasta"], ["czternasta"],
    ["piętnasta"], ["szesnasta"], ["siedemnasta"], ["osiemnasta"],
    ["dziewiętnasta"], ["dwudziesta"],

    ["kierunek wiatru"], ["metr na sekundę"], ["metry na sekundę"],
    ["metrów na sekundę"], ["kilometr na godzinę"], ["kilometry na godzinę"],
    ["kilometrów na godzinę"],

    ["ciśnienie"], ["hektopaskal"],
    ["hektopaskale"], ["hektopaskali"], ["tendencja spadkowa"],
    ["tendencja wzrostowa"], ["temperatura odczuwalna"],
    ["temperatura minimalna"], ["maksymalna"],
    ["następnie"],

    # literowanie polskie wg. "Krótkofalarstwo i radiokomunikacja - poradnik",
    # Łukasz Komsta SQ8QED, Wydawnictwa Komunikacji i Łączności Warszawa, 2001,
    # str. 130 (z drobnymi modyfikacjami fonetycznymi)

    ['adam', 'a'],
    ['barbara', 'b'],
    ['celina', 'c'],
    ['dorota', 'd'],
    ['edward', 'e'],
    ['franciszek k', 'f'],
    ['gustaw', 'g'],
    ['henryk k', 'h'],
    ['irena', 'i'],
    ['józef', 'j'],
    ['karol', 'k'],
    ['ludwik k', 'l'],
    ['marek k', 'm'],
    ['natalia', 'n'],
    ['olga', 'o'],
    ['paweł', 'p'],
    ['kłebek k', 'q'],  # wł. Quebec
    ['roman', 'r'],
    ['stefan', 's'],
    ['tadeusz', 't'],
    ['urszula', 'u'],
    ['violetta', 'v'],
    ['wacław', 'w'],
    ['xawery', 'x'],
    ['ypsylon', 'y'],  # wł. Ypsilon
    ['zygmunt', 'z'],
    ['łamane'],

    # Sample dla WorldWeatherOnline

    ['bezchmurnie'], ['burza'], ['burza śnieżna'], ['częściowe zachmurzenie'],
    ['grad'], ['intensywne opady śniegu'],
    ['lokalna przelotna marznąca mżawka'], ['lokalne burze'],
    ['lokalne przelotne opady deszczu'],
    ['lokalny słaby deszcz'], ['marznąca mgła'], ['marznąca mżawka'],
    ['mgła'], ['mżawka'], ['opady śniegu'], ['pochmurno'],
    ['przelotne opady deszczu'], ['przelotne ulewy'],
    ['słabe opady marznącego deszczu'], ['słabe opady śniegu'],
    ['słabe opady śniegu z deszczem'], ['słabe opady śniegu ziarnistego'],
    ['słabe przelotne opady deszczu'], ['słaby deszcz'], ['śnieg'],
    ['śnieg z deszczem'], ['ulewny deszcz'], ['ulewy'],
    ['umiarkowane lub ciężkie opady śniegu z deszczem'],
    ['umiarkowane opady deszczu'], ['umiarkowane opady marznącego deszczu'],
    ['umiarkowane opady śniegu'], ['umiarkowane opady śniegu z deszczem'],
    ['umiarkowane opady śniegu ziarnistego'], ['zachmurzenie całkowite'],
    ['zamglenia'], ['zamieć śnieżna'], ['pokrywa chmur'],
    ['łorld łeder onlajn', "worldweatheronline"],

    # Sample dla radioactive@Home

    ['promieniowanie tła'],
    ['przecinek', 'przecinek'],
    ['mikrosjiwerta na godzinę', 'mikrosiwerta_na_godzine'],
    ['w normie'],
    ['podwyższone'],
    ['wysokie'],

]
