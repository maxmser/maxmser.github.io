# Entscheidungen und offene Punkte

Diese Datei hält fest, was für die Projektseite entschieden wurde und warum. Neue Einträge kommen mit Datum dazu. Bestehende Einträge werden nicht still überschrieben, sondern ergänzt oder als geändert markiert.

## Zweck der Seite

Stand 05.11.2026. Die Seite soll Menschen, die Max' Bewerbungen lesen, zeigen, wie er denkt und was er baut. Max ist Product Leader im Bereich Digital Product und Technology mit mehr als 15 Jahren Erfahrung und baut nebenbei eigene technische Projekte mit Claude Code. Die Seite soll nüchtern, schnell und minimalistisch sein. Es gibt keinen Blog und keine Posts, sondern nur Projektbeschreibungen.

## Feste Entscheidungen vom 05.11.2026

Die Sprache der Seite ist Englisch. Hugo ist so eingerichtet, dass später eine deutsche Version ergänzt werden kann. Englisch ist die Standardsprache und liegt im Wurzelverzeichnis der Seite. Inhalte gibt es vorerst nur auf Englisch. Für eine deutsche Version braucht es später einen Block `[languages.de]` in `hugo.toml`, eine Datei `i18n/de.toml` mit den Oberflächentexten und deutsche Inhaltsdateien mit der Endung `.de.md` neben den englischen.

Der Generator ist Hugo in der Extended-Version. Lokal ist Hugo 0.169.0 extended über Homebrew installiert, und genau diese Version ist im GitHub-Actions-Workflow festgenagelt. Es gibt kein fertiges Theme, sondern eigene, möglichst schlanke Layouts.

Gehostet wird auf GitHub Pages. Veröffentlicht wird über GitHub Actions. Das Repository heißt `maxmser.github.io` und ist öffentlich. Der GitHub-Benutzername `maxmser` wurde am 05.11.2026 über `gh api user` ermittelt und von Max bestätigt.

Der lokale Projektordner ist `~/Documents/Projekte/Website`.

Der Titelsatz der Seite lautet: "Product leader who builds things to understand them." Er steht als Überschrift auf der Startseite. Der Seitenname im Browser-Tab und in der Navigation ist "Max Moser". Diesen Namen hat Max am 05.11.2026 festgelegt.

Version 1 enthält kein JavaScript, keine externen Anfragen, keine Cookies und kein Analytics. Schriften werden selbst gehostet. Bis zum 05.11.2026 verwendete die Seite den System-Schriftstapel des jeweiligen Geräts, seitdem vorerst Inter (siehe Abschnitt "Schrift: vorerst Inter"). Damit der Browser nicht nach einer Datei `favicon.ico` fragt, ist ein leeres Favicon eingetragen. Auch der automatische Hugo-Generator-Hinweis im Seitenkopf ist abgeschaltet.

Geändert am 06.11.2026: Die Regel "kein JavaScript" gilt nicht mehr. Max hat entschieden, dass reines JavaScript ohne Framework erlaubt ist, solange es klein bleibt. Keine externen Anfragen, keine Cookies und kein Analytics gelten weiter. Was eingebaut ist, steht im Abschnitt "Geschwindigkeit: Vorladen und Service Worker".

Es gibt noch keine eigene Domain. Die Seite läuft vorerst unter https://maxmser.github.io/.

## Umzug auf eine eigene Domain

Stand 05.11.2026. Ursprünglich war geplant, dass für den Umzug auf eine Domain nur `baseURL` und eine CNAME-Datei nötig sind. Das stimmt für diesen Aufbau nicht ganz. Die GitHub-Dokumentation sagt, dass eine CNAME-Datei ignoriert wird und nicht nötig ist, wenn die Seite über einen eigenen GitHub-Actions-Workflow veröffentlicht wird. Die Domain wird stattdessen im Repository unter Settings, dann Pages, im Feld "Custom domain" eingetragen.

Für den Umzug braucht es deshalb drei Schritte. Erstens wird `baseURL` in `hugo.toml` auf die neue Domain geändert. Zweitens wird die Domain in den Pages-Einstellungen des Repositorys eingetragen. Drittens werden beim Domain-Anbieter die DNS-Einträge gesetzt, die GitHub in seiner Dokumentation nennt. Der Build im Workflow übernimmt die Adresse ohnehin aus den Pages-Einstellungen.

Quellen: GitHub Docs, "Troubleshooting custom domains and GitHub Pages" und "Managing a custom domain for your GitHub Pages site".

## Seitenstruktur

Stand 05.11.2026. Die Seite hat vier Arten von Seiten. Die Startseite zeigt den Titelsatz, einen kurzen Einleitungsabsatz und die Liste der Projekte. Die Projektübersicht unter `/projects/` listet alle Projekte. Jedes Projekt hat eine eigene Seite. Dazu kommt das Impressum unter `/imprint/`.

Die Layouts sind `baseof.html` als Grundgerüst, `home.html` für die Startseite, `list.html` für die Projektübersicht, `single.html` für Projektseiten und `text.html` für einfache Textseiten wie das Impressum. Dazu kommen drei kleine Teilvorlagen für die Navigation, die Projektliste und die Liste "More projects". Taxonomien und der RSS-Feed sind abgeschaltet, weil es keinen Blog gibt. Die Sitemap bleibt, weil sie Suchmaschinen hilft und keine externen Anfragen auslöst.

Nachtrag vom 06.11.2026: Dazu kommen zwei Teilvorlagen. `sections.html` teilt den Text einer Seite an jeder Überschrift zweiter Ordnung in Abschnitte auf, damit die Überschrift links und der Text rechts stehen kann. `dev-font-switch.html` ist der lokale Schriftschalter, siehe Abschnitt "Design-Umsetzung vom 06.11.2026".

Das englische Wort für Impressum auf der Seite ist "Imprint". Diese Wahl ist vorläufig und kann geändert werden.

## Projektseiten

Stand 05.11.2026. Für Projektseiten gibt es einen Archetyp in `archetypes/projects.md`. Er legt die Felder title, summary, date, status, stack und weight an. Status beschreibt den Zustand des Projekts, zum Beispiel "in use" oder "prototype". Stack ist eine Liste der verwendeten Technologien. Weight bestimmt die Reihenfolge, kleinere Zahlen stehen weiter oben. Im Text gibt es vier feste Abschnitte: Problem, Decisions, Outcome und What I learned. Unter jeder Überschrift steht vorerst ein Platzhalter mit dem Hinweis TODO.

Die Projektseiten sind als Ordner angelegt, also zum Beispiel `content/projects/radio-pwa/index.md`. So können später Bilder direkt neben dem Text liegen.

## Projektplan für Version 1

Stand 05.11.2026. Diese vier Projekte bekommen eine eigene Seite. Sie sind bisher nur als Platzhalter angelegt.

1. Fire TV setup for my parents, im Ordner `content/projects/fire-tv-setup`.
2. Job search pipeline, im Ordner `content/projects/job-search-pipeline`. Als Umfang hat Max genannt: Crawler, LLM-Bewertung und tägliche Durchsicht durch einen Agenten.
3. Living-room audio stack, im Ordner `content/projects/living-room-audio`. Als Umfang hat Max genannt: Loudness-Daemon, Raumkorrektur und Anbindung an Home Assistant.
4. Radio PWA, im Ordner `content/projects/radio-pwa`.

Zusätzlich gibt es eine Liste "More projects" ohne eigene Seiten. Sie steht in der Datei `content/projects/_index.md` und enthält den Homeserver und den CV generator. Das LED matrix display steht auch in der Liste, ist aber ausgeblendet, weil es noch nicht fertig ist. Zum Einblenden wird dort die Zeile `hidden: true` entfernt.

## Layout-Absicht

Stand 05.11.2026. Das Design macht Max später selbst in einer eigenen Runde. Die Richtung ist Schweizer Rastergrafik im Stil von Josef Müller-Brockmann. Deshalb gibt es jetzt nur eine neutrale Basis, die später nicht im Weg steht.

Das HTML ist semantisch aufgebaut, mit header, nav, main, article, section und footer. Es gibt genau eine CSS-Datei, `assets/css/main.css`. Sie definiert ein 12-spaltiges CSS-Grid, in dem jedes Element vorerst die volle Breite einnimmt. Schriftgrößen, Zeilenhöhen, Abstände, Rasterbreite und Farben sind als CSS-Variablen am Anfang der Datei gesammelt. Hugo verkleinert die Datei beim Build und hängt eine Prüfsumme an den Dateinamen, damit Browser nach Änderungen keine veraltete Version verwenden.

Nachtrag vom 06.11.2026: Das Layout ist inzwischen umgesetzt, siehe Abschnitt "Design-Umsetzung vom 06.11.2026". Die CSS-Datei wird nicht mehr als eigene Datei ausgeliefert, sondern beim Build verkleinert und direkt in jede Seite geschrieben. Die Quelle bleibt die eine Datei `assets/css/main.css`. Die Prüfsumme im Dateinamen entfällt damit.

## Impressum

Stand 05.11.2026. Das Impressum ist ein Platzhalter mit den Feldern Name, Wohnort und Kontakt. Als Wohnort ist Wien eingetragen. Grundlage ist die Offenlegungspflicht nach § 25 Mediengesetz. Für kleine Websites, die nur ihren Inhaber vorstellen und nicht geeignet sind, die öffentliche Meinung zu beeinflussen, reicht eine verkürzte Offenlegung. Das Unternehmensserviceportal des Bundes (usp.gv.at) nennt dafür den Namen, den Wohnort und bei Unternehmen den Unternehmensgegenstand. Die genauen Pflichtangaben für eine private Person sollten vor dem Livegang noch einmal geprüft werden.

Eine Datenschutzseite gibt es nicht, solange kein Analytics läuft und keine Cookies gesetzt werden.

## Veröffentlichung

Stand 05.11.2026. Max hat die Veröffentlichung am 05.11.2026 freigegeben und selbst ausgeführt. Das öffentliche Repository ist https://github.com/maxmser/maxmser.github.io. Die Pages-Quelle wurde vor dem ersten Push über die GitHub-API auf "GitHub Actions" gestellt. Der erste Build und das Deployment liefen ohne Fehler durch. Die Seite ist unter https://maxmser.github.io/ erreichbar, vorerst noch mit Platzhaltern.

Für Commits ist als Autor "Max Moser" mit der anonymen GitHub-Adresse 275640851+maxmser@users.noreply.github.com eingetragen. Grund: Das Repository ist öffentlich, und die E-Mail-Adresse steht in jedem Commit für alle sichtbar. Die Einstellung gilt global für Git auf Max' Mac.

Die lokalen Git-Schritte führt Max selbst im Terminal aus. Claude arbeitet in einer Linux-VM, die zwar den Ordner sieht, aber nicht ins Terminal des Macs tippen kann und keine GitHub-Anmeldung hat.

Geändert am 06.11.2026: Claude arbeitet seit diesem Tag direkt auf Max' Mac und führt die Git-Schritte selbst aus. Committet wird, wenn Max es verlangt. Gepusht und damit veröffentlicht wird nur nach seiner ausdrücklichen Freigabe. Nach jedem Push prüft Claude mit `gh run watch`, ob der Build durchläuft.

## Vorerst nicht in Suchmaschinen

Stand 05.11.2026. Max hat entschieden, die Seite vorerst auf noindex zu setzen, solange sie nur Platzhalter enthält. Jede Seite trägt dafür im Kopf die Angabe `<meta name="robots" content="noindex">`. Gesteuert wird das über `noindex = true` im Abschnitt `[params]` in `hugo.toml`.

Bewusst gibt es keine robots.txt, die das Crawlen sperrt. Laut Google Search Central wirkt noindex nur, wenn der Crawler die Seite abrufen darf. Eine Sperre in robots.txt würde verhindern, dass er die noindex-Angabe überhaupt sieht.

Die Sitemap ist in dieser Zeit abgeschaltet, weil eine Sitemap mit Seiten, die nicht indexiert werden sollen, widersprüchliche Signale sendet.

Wenn die Inhalte fertig sind, sind zwei Schritte nötig. Erstens wird `noindex` in `hugo.toml` auf false gesetzt oder gelöscht. Zweitens wird "sitemap" wieder aus `disableKinds` entfernt.

## Schrift: vorerst Inter

Stand 05.11.2026. Max hat entschieden, vorerst Inter zu verwenden. Eingebaut ist Inter in der Version 4.1 als variable Schrift, also eine Datei für alle Schriftstärken, dazu eine zweite Datei für Kursiv. Inter steht unter der SIL Open Font License 1.1 und darf frei auf Websites verwendet werden. Die Lizenzdatei liegt neben den Schriftdateien in `static/fonts/inter/`.

Die Schrift wird selbst gehostet. Es gibt also keine Anfragen an Google Fonts oder andere fremde Server. Die Dateien stammen unverändert aus dem offiziellen Release auf GitHub (rsms/inter, Version 4.1 vom 16.11.2024). Die normale Schriftdatei wird im Seitenkopf vorgeladen, damit der Text schneller in Inter erscheint. Die Kursiv-Datei lädt der Browser nur, wenn auf einer Seite kursiver Text vorkommt.

Jede der beiden Dateien ist etwa 350 KB groß, weil sie alle Schriftsysteme von Inter enthält, auch Kyrillisch, Griechisch und Vietnamesisch. Man könnte sie später auf lateinische Zeichen kürzen. Das würde die Ladezeit beim ersten Besuch spürbar senken.

Nachtrag vom 06.11.2026: Die Dateien sind gekürzt, siehe Abschnitt "Schrift gekürzt".

Inter ist eine Zwischenlösung. Die endgültige Schriftwahl bleibt offen, siehe unten. Nachtrag vom 06.11.2026: Die Dateien von Inter 4.1 wurden durch einen eigenen Build mit dem "a" mit Schweif ersetzt, siehe den nächsten Abschnitt.

## Schrift: Inter mit "a" mit Schweif (cv16)

Stand 06.11.2026. Max will Inter mit dem "a" mit Schweif verwenden, wie es Helvetica hat. Rasmus Andersson hat diese Variante am 17.11.2024 auf X gezeigt, als Character Variant cv16 "Lower-case a with tail". Max hatte sich an den Post erinnert und ihn als Screenshot geschickt. Claude hatte die Variante vorher nicht gefunden, weil sie in keiner veröffentlichten Version von Inter enthalten ist.

Geprüft am 06.11.2026: Die neueste offizielle Version ist Inter 4.1 vom 16.11.2024. Sie enthält cv16 nicht. Auch die Inter-Version auf Google Fonts enthält cv16 nicht. Im Quellcode auf GitHub ist cv16 vorhanden. Der Quellcode trägt die Versionsnummer 4.2, die letzte Änderung ist der Commit 353b61b vom 18.11.2024. Eine Version 4.2 wurde nie veröffentlicht.

Deshalb wurden die beiden Schriftdateien `InterVariable.woff2` und `InterVariable-Italic.woff2` am 06.11.2026 aus diesem Quellcode gebaut, mit den Werkzeugen und Skripten des Inter-Repos (fontmake 3.9). Sie ersetzen die Dateien von Inter 4.1. Gegenüber 4.1 kommen die Varianten cv15 und cv16 dazu. Achsen, Stärken und Familienname sind gleich geblieben. Die Lizenz ist unverändert die SIL Open Font License 1.1.

Im CSS ist cv16 für die ganze Seite eingeschaltet. Die Variante gibt es nur für die aufrechte Schrift. In kursivem Text erscheint weiter das normale "a".

So wurde gebaut, falls die Dateien neu erzeugt werden müssen: Das Repo github.com/rsms/inter auf Commit 353b61b klonen. Eine Python-3.11-Umgebung mit fontmake 3.9, glyphspkg 0.1, skia-pathops 0.8, ufo2ft und defcon anlegen. Dann für Roman und Italic jeweils die Schritte aus dem Makefile des Repos einzeln ausführen: `glyphspkg` wandelt das Glyphs-Paket um, `fontmake -o ufo` erzeugt die Master, danach laufen `misc/tools/postprocess-designspace.py` und `misc/tools/gen-var-designspace.py`, dann `fontmake -o variable` und zum Schluss `misc/tools/bake-vf.py`. Die TTF-Dateien wurden mit fontTools in WOFF2 umgewandelt. Das vollständige Makefile braucht weitere Werkzeuge wie fontbakery und gftools, die für die Web-Schriften nicht nötig sind.

Risiko: Der Quellcode ist ein unveröffentlichter Arbeitsstand. Er kann kleine Fehler enthalten, die vor einem offiziellen Release noch behoben worden wären. Wenn Inter 4.2 offiziell erscheint, sollten die Dateien durch die offiziellen ersetzt werden.

## Design-Grundlagen für den Design-Durchgang

Stand 06.11.2026. Grundlage ist eine Recherche zu Josef Müller-Brockmann und zur Übertragung seines Rastersystems ins Web. Ein statischer Entwurf der Startseite liegt im Ordner `design/entwurf-2026-11-06/`. Max hat ihn als Vorher-Nachher-Bild gesehen. Der Entwurf ist noch nicht in die Hugo-Layouts übernommen. Nachtrag vom 06.11.2026: Er ist inzwischen übernommen, siehe Abschnitt "Design-Umsetzung vom 06.11.2026".

Die wichtigste Regel: Die Zeilenhöhe der Grundschrift ist die einzige Maßeinheit für alle vertikalen Abstände. Bei Müller-Brockmann entspricht die Höhe eines Rasterfeldes einer Zahl von Textzeilen, und der Abstand zwischen Feldern beträgt eine oder mehrere Zeilen. Im CSS bildet die Einheit `rlh` das ab. Sie ist die Zeilenhöhe des Root-Elements und gilt seit Mai 2026 in allen großen Browsern als breit verfügbar.

Damit `1rlh` wirklich eine Zeile Fließtext ist, müssen Schriftgröße und Zeilenhöhe auf `html` stehen, nicht auf `body`. Im Entwurf sind das `font-size: 1.125rem` und `line-height: 1.5`, also 18 Pixel Schrift und 27 Pixel Zeilenhöhe. Der Recherchebericht hatte in seinem eigenen CSS-Beispiel genau diesen Fehler.

Weitere Regeln aus der Recherche, die der Entwurf umsetzt: Alle vertikalen Abstände sind ganze oder halbe Vielfache von `1rlh`. Überschriften bekommen eine Zeilenhöhe, die ein Vielfaches von `1rlh` ist. Fließtext ist auf etwa 62 bis 65 Zeichen Breite begrenzt. Das Raster hat 4 Spalten auf kleinen Bildschirmen, 8 ab 40em und 12 ab 64em. Der Spaltenabstand ist `1rlh`. Es gibt nur vier Schriftgrößen und zwei Stärken. Hierarchie entsteht zuerst über Position und Abstand. Text steht linksbündig im Flattersatz, und auf breiten Bildschirmen bleiben Spalten bewusst frei.

Trennlinien werden als Hintergrund gezeichnet und nicht als Rahmen, damit sie den Zeilenrhythmus nicht um ein Pixel verschieben. Schriftgrößen stehen in `rem`, Medienabfragen in `em`, damit Zoom und Nutzereinstellungen das ganze System mitskalieren.

Offen ist, ob Inter Display auch für den Fließtext gelten soll oder nur für Überschriften. Max hat am 06.11.2026 gesagt, dass er Inter in der Display-Variante verwenden will. Im Fließtext mit 18 Pixel ist Display etwas enger gesetzt als die Textvariante. Der Vergleich liegt als `schrift-vergleich.png` im Entwurfsordner.

Nachtrag vom 06.11.2026: Max hat sich zunächst für Display nur bei den großen Überschriften entschieden. So ist die Seite jetzt eingestellt: Seitentitel mit optischer Größe 32, alle anderen Texte mit optischer Größe 14. Danach wollte Max die Varianten lieber im Browser vergleichen. Die Entscheidung ist deshalb wieder offen, siehe Abschnitt "Design-Umsetzung vom 06.11.2026" zum Schriftschalter.

## Design-Umsetzung vom 06.11.2026

Stand 06.11.2026. Der Entwurf ist in die Hugo-Layouts übernommen, und zwar für die Startseite, die Projektübersicht, die Projektseiten, das Impressum und die Fußzeile. Alle Seiten nutzen dasselbe Raster mit 4, 8 und 12 Spalten. Links steht jeweils der Name eines Abschnitts, rechts der Inhalt. Auf Projektseiten stehen Status und Stack links neben der Kurzbeschreibung.

Geprüft wurde in Chrome bei 320, 375, 768 und 1440 Pixel Breite, mit 200 Prozent Browser-Zoom und mit 200 Prozent reinem Text-Zoom. Ein Skript hat dabei gemessen, dass jede Textzeile auf dem Zeilenraster von 27 Pixel liegt und dass keine Seite horizontal scrollt. In Safari und auf dem iPhone ist das Layout bisher nur von Hand anzusehen.

Die Unterstützung von `rlh` und `subgrid` wurde am 06.11.2026 an den Baseline-Daten des W3C-Projekts web-features geprüft (Version 3.45.0). Beides gilt als breit verfügbar, `rlh` seit dem 21.05.2026 und `subgrid` seit dem 15.03.2026. Der Schriftschalter nutzt `:has()`, das seit 2023 breit verfügbar ist.

Folgende Entscheidungen hat Claude ohne Rückfrage getroffen. Max hat sie mit der Freigabe zum Veröffentlichen akzeptiert, sie lassen sich aber jederzeit ändern. Erstens sind die Abschnittsnamen halbfett mit Stärke 500 statt fett mit 600 wie im Entwurf, weil die Regel nur zwei Stärken erlaubt. Der Entwurf hatte drei. Zweitens haben alle Seitentitel die große Display-Größe, auch "Imprint" und die Projekttitel. Drittens hat die Projektliste in der Übersicht links keinen Namen, weil der Seitentitel schon "Projects" heißt. Viertens steht jede Technik im Stack in einer eigenen Zeile. Fünftens sind Links im Fließtext unterstrichen, Navigation und Projektlisten nur beim Darüberfahren.

Ein Fehler wurde während der Umsetzung gefunden und behoben. Die Zeilenhöhe steht als feste Länge `1rlh` auf `body`, damit jeder Text genau eine Rasterzeile hoch ist. Dadurch wurde die kleine Nummer in der Projektliste bei der Ausrichtung an der Grundlinie des Titels nach unten geschoben, und jede Zeile war 2 Pixel zu hoch. Die Nummer hat jetzt die Zeilenhöhe 1, und das Raster stimmt wieder.

Die Abschnitte der Projektseiten entstehen, indem `sections.html` den fertigen Text an jedem `<h2` aufteilt. Mit dem Archetyp funktioniert das sicher. Bei ungewöhnlichem Markdown, zum Beispiel rohem HTML mit `<h2` im Text, ist es nicht getestet.

Zum Vergleichen der Schriftvarianten gibt es einen Schalter mit vier Stellungen: Display nur bei Überschriften, Display überall, Text überall und automatisch nach Größe. Er erscheint nur unter `hugo server` und ist im veröffentlichten Build nicht enthalten. Er braucht kein JavaScript, merkt sich die Wahl aber nicht über einen Seitenwechsel hinaus. Nach der Entscheidung werden die Datei `layouts/_partials/dev-font-switch.html` und ihre Zeile in `baseof.html` gelöscht.

## Schrift gekürzt

Stand 06.11.2026. Die Schrift war mit Abstand der größte Teil jeder Seite. HTML und CSS zusammen sind gezippt etwa 2,5 KB groß, die Schriftdatei hatte 356 KB. Max hat das Kürzen freigegeben.

Beide Dateien enthalten jetzt nur noch lateinische Zeichen und die Stärken 400 bis 500, die die Seite benutzt. Die normale Datei ist von 356 KB auf 72 KB geschrumpft, die kursive von 387 KB auf 77 KB. Erhalten sind beide Achsen, also Stärke und optische Größe, alle OpenType-Funktionen einschließlich cv16 und alle Namenseinträge. Umlaute, ß, deutsche Anführungszeichen, Gedankenstrich und Eurozeichen sind enthalten. Deutsch und Englisch sind damit vollständig abgedeckt.

Weil die Schrift nur noch bis Stärke 500 reicht, ist fett markierter Text auf 500 gesetzt. Sonst würde der Browser bei Fett eine künstlich verdickte Schrift erzeugen. Eine dritte Stärke wäre später ein neuer Build.

Gegenprobe: Bei Stärke 400 sind die gemessenen Textbreiten exakt gleich wie vorher. Bei 500 weicht eine Zeile in 100 Pixel großer Schrift um 0,1 Pixel ab, eine Rundung beim Kürzen der Achse, die man nicht sieht.

Die Lizenz erlaubt das. Inter nennt nach dem Copyright-Hinweis keinen geschützten Schriftnamen ("Reserved Font Name"), deshalb dürfen gekürzte Dateien den Namen behalten. Die Lizenzdatei bleibt neben den Schriftdateien.

So wurde gekürzt, mit fontTools: Zuerst begrenzt `fontTools.varLib.instancer` die Stärken-Achse mit `wght=400:500`. Dann behält `fontTools.subset` den lateinischen Zeichenbereich `U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD`, mit den Optionen `--layout-features='*' --name-IDs='*' --name-languages='*' --notdef-outline --flavor=woff2`. Ausgangspunkt sind die ungekürzten Dateien aus Commit 2eba55d. Das Werkzeug glyphhanger wurde nicht verwendet. Es ruft intern dasselbe fontTools auf, sucht die Zeichen aber aus den Seiten heraus, und die Texte sind noch Platzhalter.

Geändert am 06.11.2026, zweiter Schritt: Die Schrift enthält jetzt nur noch Englisch und Deutsch und nur die Funktionen, die die Seite nutzt. Die normale Datei ist von 72 KB auf 34,6 KB geschrumpft, die kursive auf 36,2 KB. Enthalten sind 130 Zeichen: Grundlatein, ÄÖÜäöüß, é, deutsche und englische Anführungszeichen, Binde- und Gedankenstriche, Auslassungspunkte, Paragraf, Copyright, Grad, Mal, Euro, Markenzeichen, Minus und vier Pfeile. An Funktionen bleiben Kerning, Akzente, kontextabhängige Formen, Brüche, Tabellenziffern sowie die Varianten cv16, cv05, cv10 und ss02. Die beiden Achsen Stärke 400 bis 500 und optische Größe 14 bis 32 sind erhalten.

Zeichensatz, Funktionen und Stärken stehen jetzt an einer einzigen Stelle, in `data/font.toml`. Das Skript `tools/build-fonts.py` baut daraus die Dateien in `static/fonts/inter/`, ausgehend von den vollständigen Schriften in `tools/fonts-src/`. Die Teilvorlage `font-check.html` liest dieselbe Datei und bricht den Build ab, wenn eine Seite ein Zeichen enthält, das nicht in der Schrift ist. Sonst würde so ein Zeichen still in einer anderen Schrift erscheinen. Geprüft am 06.11.2026 mit einem "ñ" in einer Kurzbeschreibung: Der Build bricht mit einer klaren Meldung ab. Für ein neues Zeichen wird es in `data/font.toml` ergänzt und `python3 tools/build-fonts.py` ausgeführt.

Zur Kompression: WOFF2 packt intern mit Brotli. fontTools ruft Brotli ohne Qualitätsangabe auf, und der Standard ist die höchste Stufe 11. Zopfli ist ein Packer für gzip und das ältere WOFF 1 und für WOFF2 nicht zuständig. Zusätzlich nutzt das Skript die freiwillige Umwandlung der Breitentabelle `hmtx`, das spart 112 Bytes.

## Geschwindigkeit: Vorladen und Service Worker

Stand 06.11.2026. Max will, dass die Seite sehr schnell lädt, und zwar vor allem die Zeit bis zur ersten Antwort des Servers bei jedem Klick. Gemessen am 06.11.2026: Hat der Zwischenspeicher von GitHub Pages die Seite vorrätig, antwortet er nach etwa 10 bis 25 Millisekunden. Hat er sie nicht, dauert es etwa 170 bis 190 Millisekunden. Bei einer Seite mit wenigen Besuchern dürfte der zweite Fall häufig sein.

Das CSS steht direkt im HTML. Beim ersten Aufruf fällt damit eine Anfrage weg, auf die der Browser vor dem Anzeigen warten müsste. Beim ersten Besuch lädt der Browser nur noch HTML und Schrift.

Für Chrome und Edge stehen im Seitenkopf Speculation Rules. Sie laden alle internen Seiten sofort vor und bauen eine Seite schon fertig auf, wenn der Mauszeiger 200 Millisekunden auf dem Link liegt. Dazu kommt eine Regel mit der Stufe "conservative", die erst bei Berührung oder Mausdruck vorlädt. Das ist genau der Teil, dem das WebKit-Team im Juni 2025 zugestimmt hat. Safari kann ihn nutzen, sobald Apple ihn einschaltet. Gemessen in Chrome: Nach dem Klick kam keine neue Anfrage an den Server, die Wartezeit auf den Server war 0 Millisekunden. Das fertige Aufbauen beim Hover wurde im Test ohne Bildschirm nicht beobachtet.

Safari kann bisher weder Speculation Rules noch `<link rel="prefetch">`. Laut den Baseline-Daten unterstützen das nur Chrome und Edge beziehungsweise Chrome und Firefox. Safari 27.2 meldet zwar, Speculation Rules zu kennen, lädt aber mit keiner Regelart etwas vor. Das wurde am 06.11.2026 getestet. Auch instant.page hilft dort nicht. Laut seinem Quellcode in Version 5.2.0 beendet es sich sofort, wenn der Browser kein `link rel="prefetch"` kann. FastClick ist überflüssig. Laut eigener Dokumentation haben Chrome und Safari die Verzögerung von 300 Millisekunden beim Tippen seit Ende 2015 nicht mehr.

Getestet und verworfen für Safari: Seiten mit `fetch()` vorzuladen. Safari fragt beim Klick trotzdem noch einmal beim Server. Ein unsichtbarer iframe funktionierte zwar, Max fand das aber zu sehr einen Trick.

Deshalb gibt es einen Service Worker in reinem JavaScript, die Datei `assets/js/sw.js`. Der Browser installiert ihn beim ersten Besuch. Er legt alle Seiten und die Schrift in einem eigenen Speicher im Browser ab und beantwortet Klicks von dort. Service Worker sind laut Baseline-Daten seit 2020 in allen großen Browsern breit verfügbar, in Safari seit Version 11.1. Gemessen am 06.11.2026 mit einem Testserver, der jede Seite 800 Millisekunden zurückhält: Die erste Seite kam nach etwa 830 Millisekunden, die Seite nach dem Klick in Chrome nach 14, in Safari nach 3 und in Firefox nach 60 Millisekunden.

So bleiben die Seiten aktuell. Die Datei bekommt bei jedem Build eine neue Versionsnummer. Laut MDN holt der Browser diese Datei bei Updates immer vom Server und umgeht dabei den Zwischenspeicher von GitHub Pages, der 10 Minuten gilt. Die neue Version holt alle Seiten frisch vom Server und löscht den alten Speicher. Außerdem fragt der Service Worker bei jeder Seite im Hintergrund beim Server nach, ob sie sich geändert hat. Nach einem Deploy sieht ein wiederkehrender Besucher deshalb genau eine Seite in der alten Fassung. Wer zum ersten Mal kommt, ist nie betroffen. Max hat das am 06.11.2026 als akzeptabel eingestuft. Den einen veralteten Aufruf kann man nicht vermeiden, ohne vor jeder Seite beim Server nachzufragen, und genau diese Wartezeit soll wegfallen.

Zwei Fehler im ersten Entwurf wurden beim Testen gefunden und behoben. Die neue Version hätte alte Seiten aus dem Zwischenspeicher von GitHub Pages geholt, dann wäre der Versionswechsel wirkungslos gewesen. Und die Schrift wäre beim ersten Besuch doppelt geladen worden.

Der Service Worker ist nur im veröffentlichten Build aktiv, nicht unter `hugo server`, weil er beim Bearbeiten alte Fassungen festhalten würde. Er liegt unter `/sw.js` ohne Prüfsumme im Namen, weil sich sein Name nie ändern darf. Er wird nicht verkleinert, weil Hugo ihn dabei umbenennt. Er lädt erst nach der Seite und bremst sie nicht.

Notausschalter, falls der Service Worker einmal Probleme macht: Den Inhalt von `assets/js/sw.js` durch einen ersetzen, der beim Installieren alle Speicher löscht und `self.registration.unregister()` aufruft, und veröffentlichen. Ein bloßes Entfernen der Datei reicht nicht, weil installierte Service Worker in den Browsern der Besucher weiterlaufen.

Rechtlich gilt nach den Leitlinien 2/2023 des Europäischen Datenschutzausschusses jedes Ablegen von Daten auf dem Gerät als Speichern im Sinne der ePrivacy-Regel. Ob dafür eine Einwilligung nötig ist oder eine Ausnahme greift, lassen die Leitlinien ausdrücklich offen. Streng gelesen betrifft das auch das Vorladen in den normalen Zwischenspeicher des Browsers. Max hat das am 06.11.2026 als vernachlässigbar eingestuft. Gespeichert werden nur die öffentlichen Seiten der Website selbst, keine Daten über Besucher.

## Schrift: Varianten cv05, cv10 und ss02

Stand 06.11.2026. Max hat zusätzlich zu cv16 drei Varianten gewählt: cv05 "l" mit Schweif, cv10 "G" mit Sporn wie bei Helvetica und ss02 zur Unterscheidung ähnlicher Zeichen, also Null mit Strich, großes "I" mit Serifen und "l" mit Schweif. ss02 enthält den Schweif am "l" schon, cv05 ist damit doppelt, schadet aber nicht. Der Sporn am "G" ist sehr fein und erst bei starker Vergrößerung deutlich.

Geändert am 06.11.2026: Max möchte das große "I" ohne Querstriche. In der Schrift fasst ss02 vier Einzelvarianten zusammen, nämlich cv05 für das "l" und das "ł" mit Schweif, cv07 für die andere Form des "ß", cv08 für das "I" mit Querstrichen und `zero` für die Null mit Strich. Das steht in der Ersetzungstabelle der Schrift selbst. Statt ss02 sind deshalb jetzt cv07 und `zero` eingeschaltet, sodass nur cv08 wegfällt und alles andere gleich aussieht. Geändert wurden `font-feature-settings` in `assets/css/main.css` und die Liste `features` in `data/font.toml`, danach wurde die Schrift neu gebaut. Die normale Datei wiegt jetzt 22.276 statt 22.264 Byte, die kursive 23.544 statt 23.512 Byte. Dass ss02 auch das "ß" verändert, stand vorher nicht in diesem Abschnitt. Es bleibt vorerst so, bis Max anders entscheidet.

Geprüft am 06.11.2026: Der Quellcode von Inter hat nur den Zweig `master` auf Commit 353b61b. Gegenüber der offiziellen Version 4.1 sind nur cv15 "Simplified tabular one" und cv16 neu. Über keine Funktion erreichbar sind nur fünf Glyphen, nämlich kyrillische Gegenstücke zum Schweif-a und Bauteile. Weitere versteckte Varianten gibt es nicht.

Zum Vergleichen gibt es die Musterseite `design/schriftmuster/index.html`. Sie zeigt alle 24 benannten Varianten und weitere Funktionen jeweils links normal und rechts verändert, dazu alle 2849 Zeichen der vollständigen Schrift, markiert danach, ob sie in der Schrift der Seite sind. Sie wird mit `python3 design/schriftmuster/build.py` erzeugt, liest `data/font.toml` und ist weder veröffentlicht noch im Repository, nur ihr Skript.

## Ersatzschrift mit Inters Maßen

Stand 06.11.2026. Auf langsamem Netz sprang die Projektliste kurz um eine Zeile (CLS 0,007). Gemessen wurde die Ursache: Der Browser legt das Layout zuerst mit den Maßen der Ersatzschrift an, und mit Inter bricht danach eine Zeile anders um. Das passierte auch mit der Schrift im HTML, solange sie noch nicht entpackt war.

Deshalb gibt es zwei Ersatzschriften auf Basis von Arial oder Helvetica, die auf Inters Maße angepasst sind, eine für Fließtext und eine für die großen Titel. Arial und Helvetica sind in der Breite identisch, ein Satz Werte passt also für macOS, iOS und Windows. Gemessen wurde die mittlere Breite nach englischer Buchstabenhäufigkeit, für Fließtext mit Inter in Stärke 400 und optischer Größe 14, für Titel in Stärke 500 und optischer Größe 32. Die Werte sind für Fließtext `size-adjust: 107.48%`, `ascent-override: 90.14%`, `descent-override: 22.44%` und für Titel `size-adjust: 100.16%`, `ascent-override: 96.72%`, `descent-override: 24.08%`, jeweils mit `line-gap-override: 0%`. Android hat keine der beiden Schriften und nutzt die unangepasste Systemschrift.

Ergebnis am 06.11.2026 auf langsamem 4G: Der Sprung ist weg, CLS 0.

## Schrift beim ersten Besuch im HTML

Stand 06.11.2026. Max wollte prüfen, ob die Schrift als Base64 direkt im HTML schneller ist, und zwar nur beim ersten Besuch. Danach soll sie aus dem Speicher kommen.

Gemessen am 06.11.2026, je sieben Erstbesuche mit leerem Speicher, Handy-Breite, CPU vierfach gedrosselt, mit einem Testserver, der wie GitHub Pages mit gzip komprimiert. Base64 kostet gezippt kaum mehr Bytes als die Datei selbst, etwa 1 Prozent. Auf langsamem 4G (150 Millisekunden Latenz, 1,6 Megabit pro Sekunde) erscheint der erste Text etwa 65 Millisekunden später, dafür aber gleich in Inter, und Inter ist 140 bis 330 Millisekunden früher da. Auf normalem 4G (40 Millisekunden, 12 Megabit pro Sekunde) erscheint der Text mit Base64 50 bis 70 Millisekunden früher.

Vergleich des fertigen Umbaus mit dem bisherigen Stand: Auf langsamem 4G war Text bisher nach 280 Millisekunden in der Ersatzschrift sichtbar und Inter nach 687 Millisekunden fertig, mit einem Sprung im Layout. Jetzt ist Text nach 356 Millisekunden gleich in Inter sichtbar, Inter ist nach 365 Millisekunden fertig, und nichts springt. Auf normalem 4G erscheint Text jetzt nach 104 statt nach 172 Millisekunden.

So ist es umgesetzt. Hugo baut jede Seite zweimal. `index.html` enthält die aufrechte Schrift als Base64 im CSS, mit `font-display: block`, weil die Daten schon da sind. `lean.html` verweist auf die Schriftdatei und lädt sie vor. Die schlanke Fassung steht auf noindex, und ihre kanonische Adresse ist die normale Seite. Der Service Worker legt beim ersten Besuch die schlanken Fassungen unter den normalen Adressen ab, dazu einmal die Schriftdatei. Jeder spätere Aufruf bekommt die schlanke Seite und die Schrift aus dem Speicher. Nur die allererste Seite eines Besuchs ist also größer, gezippt etwa 38 statt 2,4 KB. Die Vorlage erkennt die schlanke Fassung daran, dass Hugo in ihr die normale Seite als alternative Ausgabe führt.

Damit Chrome nicht die großen Fassungen aller Seiten vorlädt, gibt es kein sofortiges Vorladen mehr. Chrome baut eine Seite weiter fertig auf, wenn der Mauszeiger auf dem Link liegt. Die Regel für Berührung oder Mausdruck bleibt für Safari.

Die Schriftdatei wird im Service Worker nicht mehr bei jedem Seitenwechsel beim Server nachgefragt, weil sie sich nur mit einem Deploy ändert und dann ohnehin neu geholt wird.

Getestet am 06.11.2026 mit einem Testserver, der jede Seite 800 Millisekunden zurückhält. Der Erstbesuch bekam in Chrome, Safari und Firefox die Seite mit Base64, die Schrift war sofort geladen. Danach holte der Service Worker die sieben schlanken Seiten und einmal die Schrift. Nach dem Klick kam die schlanke Seite aus dem Speicher, in Chrome nach 18, in Safari nach 5 und in Firefox nach 86 Millisekunden, die Schrift war geladen, ohne neuen Download. Auch das Update nach einem Deploy funktioniert: Die erste Seite kommt einmal in der alten Fassung, danach holt der neue Service Worker alle schlanken Seiten der neuen Fassung.

## Schrift: Display überall und Laufweite

Stand 06.11.2026. Max hat entschieden, Inter Display für alle Texte zu verwenden, also auch für Fließtext und kleine Angaben. Damit ist die optische Größe auf 32 festgelegt. Die Achse steckt nicht mehr in der Datei, `data/font.toml` legt sie mit `optical_size = 32` fest. Die normale Schriftdatei ist dadurch von 34,6 KB auf 22,3 KB geschrumpft, die Seite für den ersten Besuch gezippt von 38 KB auf 25,6 KB. Der lokale Schriftschalter ist entfernt.

Max fand die Buchstaben von Display bei kleinen Größen zu eng. Das bestätigt die Messung. Display ist für große Größen gemacht und deshalb enger gesetzt als die optische Größe, die Inter bei kleiner Schrift selbst vorsieht. Gemessen am 06.11.2026, gewichtet nach englischer Buchstabenhäufigkeit, als Unterschied zwischen Display und der optischen Größe, die der Schriftgröße entspricht: Bei 18 Pixel in Stärke 400 sind die Seitenabstände der Buchstaben zusammen 0,020 em kleiner, die Buchstaben selbst 0,015 em schmaler. Bei 14,6 Pixel sind es 0,025 em und 0,018 em in Stärke 400 sowie 0,022 em und 0,016 em in Stärke 500.

Ausgeglichen wird nur der Abstand, nicht die schmaleren Buchstaben, denn die sind der Charakter von Display. Die Laufweite beträgt deshalb +0,020 em bei 18 Pixel und +0,024 em bei 14,6 Pixel. Die großen Titel behalten ihre leicht negative Laufweite aus dem Entwurf. Ein Vergleichsbild hat Max am 06.11.2026 gesehen.

Zur Herkunft: Inter 3 hatte eine Formel für die Laufweite je Schriftgröße, Laufweite in em = −0,0223 + 0,185 × e^(−0,1745 × Schriftgröße in Pixel), Stand 07.02.2019. Die Seite dazu ist auf rsms.me nicht mehr vorhanden, nur noch im Archiv unter d.rsms.me/inter-website/v3/dynmetrics/. In Inter 4 übernimmt die Achse für die optische Größe diese Aufgabe. Dass die Achse die Formel ersetzt, ist eine Schlussfolgerung aus dem Wegfall der Seite, eine ausdrückliche Aussage von Rasmus Andersson dazu wurde nicht gefunden. Die Formel wurde deshalb nicht zusätzlich angewendet.

## Abgleich mit den Typografie-Regeln des Lebenslauf-Generators

Stand 06.11.2026. Max hat auf das Dokument `Jobsuche/cv-generator/typografie_regeln.md` vom 22.10.2026 hingewiesen. Es ist das einzige Dokument zu Typografie und Rhythmus im Projekte-Ordner. Es wurde für die Lebensläufe geschrieben, viele Regeln gelten aber auch hier. Der Abgleich am 06.11.2026 ergab Folgendes.

Schon erfüllt: Senkrechte Abstände in festen Schritten (Bringhurst 2.2.2) sind die Grundlage des Rasters. Die Zeilenlänge liegt mit höchstens 62 Zeichen im empfohlenen Bereich von 45 bis 75 Zeichen. Korrektur vom 06.11.2026: Das stimmte nicht. Gemeint war die Angabe `62ch`, und gemessen ergab sie mit Inter etwa 77 und später mit Crimson Pro auf breiten Bildschirmen bis zu 86 Zeichen. Siehe Abschnitt "B als Standard". Überschriften stehen näher am folgenden Text als am vorigen. Tabellenziffern stehen in der nummerierten Liste, Proportionalziffern im Text. Ligaturen sind kein Thema, weil Inter für Englisch keine störenden Ligaturen setzt.

Neu umgesetzt am 06.11.2026: Erstens bekommt jeder Absatz `text-wrap: pretty`, damit kein einzelnes kurzes Wort allein in der letzten Zeile steht (Regel 8.4). Das wirkt in Chrome, Edge und Safari ab Version 26, Firefox ignoriert es. Zweitens hängen Aufzählungszeichen und Nummern in Listen links vor der Textachse, damit der Text bündig am Raster bleibt (Regel 4.2). Drittens bekommen auch Titel, Kurzbeschreibungen, Status, Stack und die Liste "More projects" typografische Zeichen. Hugo setzt im Fließtext bereits gerundete Anführungszeichen und Apostrophe, aus `--` den Halbgeviertstrich, aus `---` den Geviertstrich und aus drei Punkten die Auslassungspunkte. Für Angaben aus dem Kopf der Inhaltsdateien galt das bisher nicht. Das erledigt jetzt die Teilvorlage `typo.html`. Geprüft mit einem Testsatz.

Regeln für Max beim Schreiben der englischen Texte: Gedankenstrich als Halbgeviertstrich mit Leerzeichen nach Bringhurst, geschrieben als ` -- `. Zeiträume mit Halbgeviertstrich ohne Leerzeichen, geschrieben als `2008--2012`. Kein Leerzeichen vor dem Prozentzeichen, also 12%. Währungszeichen direkt vor der Zahl, also €40 million. Zahl und Einheit nicht trennen, bei Bedarf mit `&nbsp;`. Das Et-Zeichen nur in Namen. Zahlen von eins bis neun in Wörtern, ab zehn in Ziffern. Anführungszeichen und Apostrophe können gerade getippt werden, sie werden automatisch gesetzt.

Bewusst nicht umgesetzt oder offen: Die Größenreihe der Seite (14,6, 18, 45, 58,5 und 72 Pixel) folgt nicht der klassischen Reihe, die das Dokument nennt (unter anderem 14, 18, 48, 60, 72). Bringhurst verlangt eine feste Reihe, nicht unbedingt die klassische. Eine Angleichung wäre möglich, siehe offene Punkte. Der Zeilenabstand beträgt 150 Prozent und liegt damit leicht über den 120 bis 145 Prozent, die das Dokument nennt. Er bleibt, weil er die Grundeinheit des Rasters ist und Display bei kleiner Größe etwas mehr Luft verträgt. Silbentrennung bleibt aus. Nachtrag vom 06.11.2026: Max wünscht Silbentrennung, sie ist jetzt im Lauftext eingeschaltet, siehe Abschnitt "B als Standard". Folgen von Großbuchstaben werden nicht gesperrt. Inter hätte dafür die Funktion `cpsp`, die ließe sich für Abkürzungen gezielt einschalten, wenn sie in den Texten häufig vorkommen.

## Ersatzschrift: Nachtrag zu Display überall

Stand 06.11.2026. Mit Display überall gibt es nur noch eine Ersatzschrift mit je einem Satz Werte für Stärke 400 (`size-adjust: 98.05%`, `ascent-override: 98.80%`, `descent-override: 24.60%`) und Stärke 500 (`size-adjust: 100.16%`, `ascent-override: 96.72%`, `descent-override: 24.08%`). Vorher bekamen die halbfetten Projekttitel die Werte der Stärke 400.

Ehrliche Einschränkung, gemessen am 06.11.2026: Eine Ersatzschrift kann den Sprung nicht für jeden Text ausschließen. Bei 412 Pixel Breite passt der Platzhalter "TODO: One-sentence summary." mit Inter gerade noch in eine Zeile, mit der Ersatzschrift nicht. Auf langsamem 4G entsteht dadurch wieder ein kleiner Sprung von 0,007, auf normalem 4G keiner. Lighthouse wertet alles unter 0,1 als gut. Mit den echten Texten wird das neu gemessen.

Gemessen am 06.11.2026 gegen den Stand von Commit 1c945ed, je sieben Erstbesuche: Auf langsamem 4G erscheint Text nach 292 statt nach 348 Millisekunden, auf normalem 4G nach 100 statt nach 108 Millisekunden.

## Lauftext in Crimson Pro

Stand 06.11.2026. Max wollte zu Inter eine Serifenschrift als Ergänzung, ähnlich gut wie Signifier von Klim. Verglichen wurden freie Schriften unter der SIL Open Font License, nämlich Newsreader, Source Serif 4, Literata, Junicode, Libre Caslon Text, Spectral, Crimson Pro, EB Garamond, Playfair, Instrument Serif und Hedvig Letters Serif, dazu die kommerzielle Fabric Serif von Monokrom als Testschrift. Geprüft wurde nach der Methode von Tim Brown ("Combining Typefaces", 2013): x-Höhe, Ober- und Unterlängen, Breite, Öffnung, Strichkontrast und der Grauwert im Satz. Fabric Serif passt in den Proportionen am besten zu Inter, ist aber kommerziell, und ihre Lizenz verbietet Veränderungen an der Schrift, was das Kürzen der Schrift betreffen könnte. Das ist nicht geklärt. Max hat sich am 06.11.2026 für Crimson Pro entschieden, und zwar als Schrift für den Lauftext, nicht für Überschriften.

Die Rollen sind getrennt: Crimson Pro setzt die Einleitung und den Lauftext (`.intro-text`, `.prose`), Inter alles, was die Seite gliedert, also Titel, Navigation, Abschnittsnamen, Angaben zum Projekt und die Projektlisten. Butterick empfiehlt, jeder Schrift eine feste Rolle zu geben.

Crimson Pro steht in 21 Pixel auf 27 Pixel Zeilenabstand. Das sind 129 Prozent und damit innerhalb der 120 bis 145 Prozent aus den Typografie-Regeln, und 21 ist eine Stufe der klassischen Reihe. Crimson Pro hat bei gleicher Schriftgröße eine deutlich kleinere x-Höhe als Inter (0,42 gegenüber 0,516 der Schriftgröße), deshalb steht sie größer als Inter mit 18 Pixel. Gemessen am 06.11.2026 hat eine Zeile im Mittel 73 Zeichen auf dem Desktop, 57 auf dem Tablet und 35 auf dem Handy. Mit Inter waren es 77, 60 und 36. Der Desktop liegt damit wieder unter der Grenze von 75 Zeichen, das Handy bleibt wie zuvor unter 45.

Die Schrift ist gekürzt wie Inter, auf Stärke 400 bis 500 und auf den Zeichensatz der Seite ohne die Zeichen, die Crimson Pro nicht hat, nämlich den geschützten Bindestrich und die vier Pfeile. Die Einstellungen stehen in `data/font.toml` unter `[serif]`. Die gerade Datei wiegt 19,6 Kilobyte, die kursive 20,4 Kilobyte. Die Prüfung der Zeichen beim Build prüft Lauftext und Kurzbeschreibung jetzt gegen den Zeichensatz von Crimson Pro.

Beim ersten Besuch steht die gerade Crimson Pro wie Inter direkt im HTML. Gemessen am 06.11.2026 mit je sieben Erstbesuchen kostet das auf langsamem 4G etwa 100 Millisekunden, bis Text erscheint (392 statt 292 Millisekunden), auf normalem 4G nichts (100 Millisekunden wie zuvor). Spätere Besuche bekommen die schlanken Seiten aus dem Service Worker. Die Ersatzschrift für Crimson Pro ist Georgia mit Crimsons Maßen, gemessen wie bei Inter: `size-adjust: 90.68%`, `ascent-override: 98.86%`, `descent-override: 23.69%`.

Nebenbei behoben: Das Werkzeug `tools/build-fonts.py` schrieb bei jedem Lauf die aktuelle Zeit in die Schrift, sodass gleiche Einstellungen verschiedene Dateien ergaben. Jetzt bleibt das Datum der Quelle erhalten, und zwei Läufe ergeben dieselben Dateien.

## Grundlinienraster

Stand 06.11.2026. Max wünscht einen streng senkrechten Rhythmus: Alles soll auf einem gedachten Raster einrasten. Bisher lagen nur die Zeilen im Raster, die Grundlinien nicht. Jede Schriftgröße setzt ihre Grundlinie an eine andere Stelle innerhalb der Zeile. Gemessen am 06.11.2026 lagen die Grundlinien bis zu 8,5 Pixel auseinander, und ein Abschnittsname stand 2 Pixel neben der ersten Zeile des Textes daneben.

Jetzt liegt jede Grundlinie an derselben Stelle in einem Raster aus halben Zeilen, also alle 13,5 Pixel. Crimson Pro in 21 Pixel und Inter in 18 Pixel landen dort von selbst. Die kleinen Texte in Inter mit 14,6 Pixel und der Seitentitel werden um gemessene Beträge verschoben, mit `position: relative`, sodass sich sonst nichts bewegt. Die Beträge stehen in `--snap-small` und `--snap-display` und sind in Zeilen angegeben, nicht in Pixel, damit sie mit einer größeren Schrifteinstellung des Lesers mitwachsen. `text-box-trim` wäre der neuere Weg, ist laut MDN aber nicht in Firefox verfügbar.

Beide Schriften haben gleiche Werte in den Tabellen für die Höhenmaße, die verschiedene Browser verschieden lesen, und das Kennzeichen für die einheitliche Nutzung ist gesetzt. Daraus folgt, dass Safari, Firefox und Chrome die Grundlinie gleich setzen sollten. Gemessen ist nur Chrome. Chrome rundet die Höhenmaße auf ganze Pixel. Ein Rest von unter einem Pixel lässt sich deshalb nicht vermeiden, bei doppelter Textgröße liegt Inter in 18 Pixel einen Pixel neben Crimson Pro.

Elemente in einer anderen Schrift oder hoch- und tiefgestellte Zeichen im Lauftext haben die Zeilenhöhe 0, damit sie eine Zeile nicht höher machen. Bilder im Lauftext haben noch keine Höhe im Raster. Sobald es Bilder gibt, muss das gelöst werden.

Geprüft wird das mit `node tools/raster-check.mjs` gegen `hugo server`. Das Skript öffnet alle Seiten in Chrome in vier Breiten und bei doppelter Textgröße. Es meldet jede Grundlinie außerhalb des Rasters, jeden Textblock, dessen Höhe nicht im Raster liegt, und seitliches Scrollen. Am 06.11.2026 lagen alle Grundlinien auf sieben Seiten in allen fünf Ansichten im Raster. Gegenproben haben gezeigt, dass das Skript eine fehlende Verschiebung und eine zu hohe Zeile findet. Nach jeder Änderung an Schriftgrößen oder Schriften müssen die Beträge neu gemessen werden.

Zugleich wurde die Größenreihe der Seitentitel an die klassische Reihe angeglichen: 48 Pixel auf 54 Pixel Zeilenabstand auf dem Handy, 60 auf 67,5 Pixel auf dem Tablet und 72 auf 81 Pixel auf dem Desktop. Das sind überall 112,5 Prozent. Bisher waren es 45, 58,5 und 72 Pixel, und auf dem Tablet war der Zeilenabstand des Titels mit 138 Prozent sehr locker. Auf dem Handy bricht der Titel der Startseite dadurch in fünf Zeilen um.

## Bilder im Raster und Testseite

Stand 06.11.2026. Max wollte Lauftext und Bilder auf einer Projektseite sehen, um das Layout zu prüfen. Weil keine Projekttexte erfunden werden, gibt es dafür die Testseite `content/projects/layout-test/` mit Text aus Herman Melvilles "Moby-Dick" von 1851, der gemeinfrei ist, und zwei erzeugten Testbildern. Die Seite wird gebaut und ist unter `/projects/layout-test/` erreichbar, erscheint aber in keiner Liste und wird vom Service Worker nicht vorgeladen (`build: list: never`). Sie enthält alle Elemente, die im Lauftext vorkommen können: Einleitung, Abschnitte, Zwischenüberschrift, Listen, Zitat, Code im Text und als Block, Hervorhebungen, einen Link und Bilder mit Bildunterschrift.

Bilder liegen neben der Markdown-Datei und werden mit `![Alternativtext](datei.jpg "Bildunterschrift")` eingebunden. Ein Bild in einer eigenen Zeile wird zu einer Abbildung mit Unterschrift (`layouts/_markup/render-image.html`). Hugo erzeugt daraus WebP-Dateien in bis zu fünf Breiten, und der Browser lädt die passende. Breite und Höhe stehen im HTML, damit nichts springt, und die Bilder laden erst, wenn sie in die Nähe des sichtbaren Bereichs kommen. Veröffentlicht werden nur die verkleinerten Fassungen, nicht die Originale. Fehlt eine Datei oder ein Alternativtext, bricht der Build ab.

Damit Bilder das Grundlinienraster nicht stören, wird ihre Höhe mit der CSS-Funktion `round()` auf halbe Zeilen abgerundet. Das Bild wird dabei um höchstens 13,5 Pixel beschnitten. Laut MDN ist `round()` seit Mai 2024 in allen aktuellen Browsern verfügbar (Chrome 125, Firefox 118, Safari 15.4), die nötigen Containereinheiten seit Chrome 105, Firefox 110 und Safari 16. Ältere Browser zeigen das Bild in seiner natürlichen Höhe. Bilder im Hochformat, etwa Bildschirmfotos vom Handy, stehen in der Breite eines Handys, also zwölf Zeilen oder 324 Pixel.

Dabei aufgefallen und behoben: Hugo hat Codeblöcke bisher mit dunklem Hintergrund im Stil "Monokai" eingefärbt, als feste Stilangaben im HTML. Das passte nicht zum schwarz-weißen Design und war nur nicht sichtbar, weil es noch keinen Codeblock gab. Die Färbung ist jetzt aus. Außerdem war Code in einem Codeblock doppelt verkleinert, auf 0,875 von 0,875 der Schriftgröße.

Die Prüfung `tools/raster-check.mjs` kontrolliert jetzt auch die Höhe aller Blöcke im Lauftext, also Abbildungen, Listen, Zitate und Code. Seiten, die nirgends verlinkt sind, werden als zusätzliche Pfade übergeben: `node tools/raster-check.mjs http://localhost:1313 /projects/layout-test/`. Am 06.11.2026 lagen alle Grundlinien auf acht Seiten in fünf Ansichten im Raster. Code steht in der Festbreitenschrift des Betriebssystems, deren Maße je nach System verschieden sind. Zu Codeblöcken siehe den Abschnitt "Gestaltungs-Review".

## Gestaltungs-Review

Stand 06.11.2026. Max wollte wissen, ob der senkrechte Rhythmus und die Größen der Überschriften stimmen. Ein eigener Prüfer hat Code, Screenshots und die Typografie-Regeln unabhängig begutachtet. Sein Urteil: Der Rhythmus funktioniert als System, mit wenigen, klar abgestuften Abständen (0, eine halbe, eine, zwei, drei und vier Zeilen). Die Befunde wurden an der Seite nachgemessen. Bei einem davon war die Zahl falsch: Der Abstand vor dem Einleitungstext betrug auf dem Desktop vier Zeilen und nicht acht. Die Aussage bleibt trotzdem richtig. Max hat am 06.11.2026 die sechs klaren Mängel zur Umsetzung freigegeben.

Erstens stand Text vor dem ersten Abschnitt näher am folgenden Abschnitt als an der Kurzbeschreibung, zu der er gehört. Er steht jetzt im Kopf der Seite, eine Zeile unter der Kurzbeschreibung und vier Zeilen vor dem ersten Abschnitt (`layouts/_partials/lead.html`).

Zweitens war der Abschnittsname mit 14,6 Pixel kleiner als die Zwischenüberschrift im Text mit 18 Pixel. Auf dem Handy, wo beide in einer Spalte stehen, wirkte die untergeordnete Überschrift dadurch lauter. Beide haben jetzt 18 Pixel. Den Rang des Abschnitts tragen die Linie darüber, die linke Spalte und der größere Abstand.

Drittens hingen die Aufzählungszeichen auf dem Handy im Seitenrand, etwa zehn Pixel vom Bildschirmrand entfernt. Listen sind dort jetzt um eine Zeile eingerückt. Ab 40em hängen die Zeichen wie bisher im Zwischenraum vor der Textspalte.

Viertens lagen Bilder im Hochformat mit 324 Pixel Breite nicht auf den Spalten des Rasters. Sie sind jetzt auf dem Desktop genau drei und auf dem Tablet vier der sechs Textspalten breit, auf dem Handy so breit wie der Text. Nachtrag vom 06.11.2026: Auf dem Handy sind es inzwischen drei von vier Spalten, siehe Abschnitt "B als Standard".

Fünftens war Code zu groß: Die x-Höhe lag 14 Prozent über der von Crimson Pro. Code steht jetzt in 0,75 der Textgröße. Ein Versuch mit 0,8 brachte nichts, weil Chrome die Maße der Festbreitenschrift des Systems anders rundet als berechnet. Korrektur vom selben Tag: Zunächst stand hier, der Codeblock sitze bei normaler Textgröße genau im Raster. Das stimmte nur für die alte Größe 0,875. Mit 0,75 lag er einen Pixel daneben, was eine großzügige Toleranz der Prüfung verdeckt hatte. Codeblöcke werden jetzt wie die übrigen Schriften um einen gemessenen Betrag verschoben (`--snap-mono`, ein Pixel), und die Sonderregel in der Prüfung ist entfernt. Auf macOS liegen sie damit bei normaler und doppelter Textgröße im Raster. Andere Systeme haben eine andere Festbreitenschrift und können abweichen.

Sechstens hatten Status und Stack auf dem Handy sechs kurze Zeilen mit 185 Prozent Zeilenabstand. Das Raster erlaubt für kleine Schrift nur ganze oder halbe Zeilen, deshalb ist die Lösung weniger Zeilen und nicht engere. Auf dem Handy stehen Name und Wert jetzt nebeneinander, das sind drei Zeilen. Ab 40em bleibt die eigene Spalte neben der Kurzbeschreibung.

Nicht umgesetzt sind die Vorschläge, die Geschmackssache sind. Bildunterschriften könnten schmaler sein, etwa 60 statt 93 Zeichen pro Zeile. Die Kurzbeschreibung könnte als Vorspann eine Stufe größer stehen, in 24 Pixel. Der Abschnittsname könnte auf dem Handy näher am Text stehen. Die Linie über der Fußzeile könnte grau sein, damit "Imprint" nicht wie ein leerer Abschnitt wirkt. Der Titel der Startseite könnte auf dem Handy 36 statt 48 Pixel groß sein, weil er heute in fünf Zeilen umbricht. Kurzbeschreibung und Lauftext könnten auf dem Tablet dieselbe rechte Kante haben.

## Zwei Versionen zum Umschalten

Stand 06.11.2026. Max wollte die Vorschläge aus dem Review, die Geschmackssache sind, auf dem Handy mit dem aktuellen Stand vergleichen. Die Testseite hat dafür unten eine kleine Leiste mit "A: current" und "B: proposals". Version B wird mit `?v=b` in der Adresse eingeschaltet. Ein kurzes Skript liest nur die Adresse, gespeichert wird nichts. Die Regeln für Version B stehen nur in `layouts/_partials/variant-switch.html` und werden nur auf Seiten mit `variants: true` geladen, nicht im Stylesheet der Seite.

Version B enthält: Bildunterschriften höchstens vier von sechs Textspalten breit (ab 40em), die Kurzbeschreibung als Vorspann in Crimson Pro 24 Pixel, den Abschnittsnamen auf dem Handy eine halbe Zeile über dem Text statt einer ganzen, die Linie über der Fußzeile grau und den Seitentitel auf dem Handy in 36 auf 40,5 Pixel statt 48 auf 54. Alle Grundlinien liegen auch in Version B im Raster, mit einer Ausnahme: Der Vorspann in 24 Pixel liegt bei doppelter Textgröße zwei Pixel daneben. Exakt gerechnet liegt er einen Pixel neben Crimson Pro in 21 Pixel, und Chrome rundet das bei normaler und doppelter Größe verschieden. Wird Version B übernommen, muss das gelöst werden.

Nachtrag vom 06.11.2026: Max findet Version B besser und fragte, ob die Bilder auf den Linien liegen und ob die Bildunterschrift zu weit weg steht. Gemessen lagen Ober- und Unterkante der Bilder auf den Zeilenkanten, also 6,5 Pixel neben den Grundlinien. Von der Bildkante bis zur Oberkante der Unterschrift waren es 22,9 Pixel. Über dem Bild lagen 61 Pixel Weißraum, unter der Unterschrift 96 Pixel, zwischen zwei Absätzen 42 Pixel. In Version B hängt das Bild jetzt oben an der Versalhöhe einer Textzeile und steht unten auf einer Grundlinie, wie in den Rastersystemen von Müller-Brockmann. Die Unterschrift steht eine Zeile tiefer, mit 16,4 Pixel Abstand zum Bild, und über und unter der Abbildung liegen jeweils 55,5 Pixel. Ein feineres Raster als 13,5 Pixel ist dafür nicht nötig, weil sich die Bilder an Versalhöhe und Grundlinie ausrichten und nicht am Raster selbst.

Der Zeilenabstand von Bildunterschriften war zu groß. Kleine Schrift kann im Raster aus halben Zeilen nur 13,5 oder 27 Pixel Zeilenabstand haben, also 92 oder 185 Prozent, und zweizeilige Unterschriften wirkten mit 185 Prozent locker. Ein erster Versuch gab den Unterschriften 20,25 Pixel Zeilenabstand und rundete ihre Höhe mit einem kleinen Skript auf das Raster auf. Max schlug dann ein feineres Raster vor, um bessere Ankerpunkte zu haben. Das ist die bessere Lösung, das Skript ist wieder entfernt.

Version B rastet deshalb auf Viertelzeilen von 6,75 Pixel ein statt auf halbe Zeilen von 13,5 Pixel (`--baseline-grid: 0.25rlh`). Lauftext läuft weiter auf 27 Pixel, also vier Viertelzeilen. Kleine Schrift, nämlich Bildunterschriften sowie Status und Stack, läuft auf 20,25 Pixel, also drei Viertelzeilen und 138 Prozent. Damit passt sie mit jeder Zeilenzahl ins Raster. Die erste Zeile einer Unterschrift steht eine Zeile unter der Grundlinie des Bildes. Über und unter jeder Abbildung liegen gemessen genau 55,5 Pixel Weißraum, unabhängig davon, wie viele Zeilen die Unterschrift hat. Der Preis: Nach einer Unterschrift mit ungerader Zeilenzahl liegt der folgende Text eine Viertelzeile anders als der Text über dem Bild. Er liegt weiter im Raster, nur im feineren. Innerhalb einer Spalte ist das nicht zu sehen, die Abstände bleiben in festen Schritten. Die Prüfung `tools/raster-check.mjs` liest die Rasterweite aus `--baseline-grid` und prüft Version B auf Viertelzeilen.

## Version C mit Charter

Stand 06.11.2026. Max fragte, ob es Charter von Matthew Carter frei gibt, weil sie gut passen könnte. Geprüft wurden zwei freie Wege. Bitstream hat Charter 1992 dem X Consortium mit einer Lizenz überlassen, die Nutzen, Verändern und Weitergeben für jeden Zweck erlaubt, solange der Lizenzhinweis erhalten bleibt. Gelesen wurde der Text bei Butterick und im Paket XCharter auf CTAN, nicht im Original bei X.org. Die Schrift hat nur die Schnitte normal, kursiv, fett und fett kursiv, kein Medium. Charis SIL ist eine Neuzeichnung nach dem Vorbild von Charter unter der SIL Open Font License, mit Medium ab Version 7. Sie hat aber die geschützten Namen "Charis" und "SIL", und laut der Liste häufiger Fragen zur Lizenz (2.6) gilt das Kürzen für das Web als Veränderung, sodass die gekürzte Schrift umbenannt werden müsste.

Gemessen an Charis SIL passt Charter in den Proportionen gut zu Inter, das Verhältnis von x-Höhe zu Versalhöhe ist 0,72 gegenüber 0,71. Sie hat aber die kräftigsten Striche aller geprüften Schriften, 0,193 der x-Höhe, gegenüber 0,187 bei Fabric, die Max im Lauftext zu fett fand, und 0,179 bei Crimson Pro.

Version C der Testseite (`?v=c`) ist Version B mit XCharter 1.26 als Lauftext. XCharter erweitert Bitstream Charter und steht unter denselben Bedingungen. Der Lizenzhinweis liegt in `static/fonts/charter/LICENSE.txt` und bleibt in den Schriftdateien enthalten. Die Schrift ist auf denselben Zeichensatz wie Crimson Pro gekürzt und wiegt 13 bis 14 Kilobyte je Schnitt. Sie wird nur auf der Testseite geladen. Charter steht in 19 Pixel auf 27 Pixel Zeilenabstand, das sind 142 Prozent, und der Vorspann in 21 Pixel. Die x-Höhe liegt damit nah an Inter in 18 Pixel. Fett gesetzter Text nutzt den fetten Schnitt.

Zwei Mängel der Quelle wurden beim Bauen behoben. Die Schrift hatte zwei verschiedene Sätze von Höhenmaßen, und der kursive Schnitt war höher als der normale. Ohne Korrektur hätten Browser die Grundlinie verschieden gesetzt, und jedes kursive Wort hätte seine Zeile um einen Pixel höher gemacht. Die Prüfung `tools/raster-check.mjs` hatte genau das gefunden. Jetzt haben alle drei Schnitte dieselben Maße (`vertical_metrics` in `data/font.toml`). Bilder hängen in Version C an der Versalhöhe von Charter, die bei 19 Pixel 12,75 Pixel beträgt, und Code steht wie in den anderen Versionen in 15,75 Pixel. Am 06.11.2026 lagen in Version C alle Grundlinien im Raster, auch bei doppelter Textgröße.

## Charter in drei Fassungen

Stand 06.11.2026. Max fand, dass die Charter der Testseite anders aussieht als die, die auf dem iPhone eingebaut ist oder die Medium verwendet. Gemessen ist die Charter in macOS eine überarbeitete Fassung von Bitstream aus den Jahren 1990 bis 2003 im TrueType-Format, mit einem zusätzlichen schwarzen Schnitt. XCharter beruht auf den PostScript-Schriften von 1992. Beide haben dieselben Zeichenbreiten sowie dieselbe Versal- und x-Höhe, unterscheiden sich aber in der Digitalisierung und in den Höhenmaßen. Medium nennt Charter als Schrift für Texte. Welche Fassung Medium verwendet, ließ sich nicht prüfen, weil Medium den automatischen Abruf sperrt.

Die Testseite zeigt deshalb drei Fassungen, alle auf Grundlage von Version B in derselben Größe. C ist XCharter. D ist die in macOS und iOS eingebaute Charter, die über `local()` ohne Download verwendet wird. Fehlt sie auf einem Gerät, zeigt die Leiste einen Hinweis, und es erscheint XCharter. Ob iOS Webseiten die eingebaute Charter nutzen lässt, war zum Zeitpunkt des Baus nicht geprüft. E ist eine gekürzte Fassung von Charis SIL 6.101, der freien Nachzeichnung von Charter. Weil "Charis" und "SIL" geschützte Namen sind und das Kürzen als Veränderung gilt, heißt die Schrift intern "Test Serif E", die Einträge zu Marke und Hersteller sind entfernt, Urheberrecht und Lizenz bleiben, und weder die Leiste noch der Quelltext der Seite nennt den Namen. Die Lizenz liegt in `static/fonts/test-serif-e/OFL.txt`.

Damit alle drei Fassungen genau gleich im Raster stehen, bekommen XCharter und die Nachzeichnung beim Bauen die Höhenmaße der Apple-Charter, 0,98 und −0,24 der Schriftgröße. Charis hatte von Haus aus sehr große Maße, 1,20 und −0,44. Am 06.11.2026 lagen in allen drei Fassungen alle Grundlinien im Raster, auch bei doppelter Textgröße. In Chrome auf dem Mac sehen C und D fast gleich aus, D etwas feiner. E läuft deutlich breiter und kräftiger.

## Entscheidung: Lauftext bleibt Crimson Pro

Stand 06.11.2026. Nach dem Vergleich der Charter-Fassungen hat Max entschieden, bei Crimson Pro als Schrift für Einleitung und Lauftext zu bleiben, weil sie am meisten Charakter hat. Charter in allen drei Fassungen ist damit verworfen. Die Versionen C, D und E der Testseite bleiben vorerst als Vergleich erhalten. Nachtrag vom selben Tag: Mit "B als Standard" sind der Schalter und die Charter-Versionen entfernt.

Die Seite, die alle Charter-Fassungen untereinander zeigt (`/projects/charter-compare/`), ist auf Wunsch von Max nicht veröffentlicht, sondern nur gesichert. Sie liegt im lokalen Zweig `archiv/charter-vergleich` (Commit 149531b) und lässt sich mit `git cherry-pick 149531b` zurückholen.

## B als Standard

Stand 06.11.2026. Max hat Version B zum Standard für alle Seiten gemacht. Seither rastet die Seite auf Viertelzeilen von 6,75 Pixel ein. Bilder hängen an der Versalhöhe und stehen auf einer Grundlinie. Bildunterschriften sowie Status und Stack laufen auf 20,25 Pixel Zeilenabstand. Die Kurzbeschreibung steht als Vorspann in Crimson Pro 24 Pixel, der Seitentitel auf dem Handy in 36 auf 40,5 Pixel. Die Linie über der Fußzeile ist grau, und der Abschnittsname steht auf dem Handy eine halbe Zeile über dem Text. Der Schalter zwischen den Versionen und die Charter-Versionen samt ihren Schriftdateien sind entfernt. Die Geschichte bleibt in Git, die Vergleichsseite im lokalen Zweig `archiv/charter-vergleich`.

Der Vorspann in 24 Pixel lag bei doppelter Textgröße bisher zwei Pixel neben dem Raster. Seine Verschiebung steht jetzt in Pixel statt in Zeilen (`--snap-standfirst: -2px`). Gemessen braucht er bei normaler und bei doppelter Textgröße dieselben zwei Pixel, weil Chrome die Höhenmaße der Schrift auf ganze Pixel rundet. Für andere Textgrößen ist das nicht gemessen.

Max wünschte auf dem iPhone weniger Rand. Der Seitenrand ist auf dem Handy jetzt 20,25 Pixel statt 27 (`--margin: clamp(0.75rlh, 5vw, 4rlh)`). Das entspricht dem üblichen Randabstand von iOS. Der Spaltenabstand bleibt eine Zeile.

Silbentrennung ist im Lauftext und in Bildunterschriften eingeschaltet (`hyphens: auto`, mit `-webkit-` für Safari vor Version 17). Laut MDN ist das seit September 2023 in allen verbreiteten Browsern verfügbar, und getrennt wird nur bei passender Sprachangabe, hier Englisch. Nicht getrennt werden der Vorspann, Überschriften und Code, weil große Schrift und Befehle nicht zerlegt werden sollen. Getrennt werden Wörter ab sechs Buchstaben, mit mindestens drei Buchstaben vor und drei nach der Trennung (`hyphenate-limit-chars: 6 3 4`). Die vier ist Absicht: Chrome zählt ein folgendes Satzzeichen mit. Diese Grenzen kennen laut MDN nur Chrome und Firefox. Für Safari sind zusätzlich die alten Angaben mit `-webkit-` gesetzt, ob das aktuelle Safari sie beachtet, ist nicht geprüft. Gemessen sinkt die Lücke am rechten Rand auf dem Handy von 9,8 auf etwa 9 Prozent der Zeilenbreite.

## Typografische Prüfung und gestalterische Prüfung

Stand 06.11.2026. Nach dem Umstieg auf B haben ein Gestalter und ein Typograf die Seite unabhängig geprüft. Die Befunde wurden nachgemessen. Umgesetzt wurden die klaren Mängel.

Erstens hatte der schmalere Rand Bilder im Hochformat auf dem Handy von den Spalten gelöst: 324 Pixel bei einer Textspalte von 334,5 Pixel. Sie sind jetzt drei von vier Spalten breit, so passt ein Bildschirmfoto auf einen Bildschirm.

Zweitens waren die Zeilen auf breiten Bildschirmen zu lang. `62ch` ergab mit Crimson Pro 736 Pixel, weil ihre Null breit ist, und gemessen bis zu 86 Zeichen ab etwa 1700 Pixel Breite. Die Zeilenlänge kommt jetzt aus dem Raster: Lauftext und Vorspann laufen über sechs Spalten, ab 92em über fünf. Gemessen liegen die Zeilen zwischen 1440 und 2560 Pixel im Mittel bei 62 bis 75 Zeichen. Bilder und Unterschriften bleiben auf den Spalten, ab 92em drei beziehungsweise vier von fünf. `--measure` ist nur noch ein Sicherheitsnetz, das in diesem Raster nicht greift.

Drittens konnte eine Zeile mit einem Gedankenstrich beginnen. Vor jedem Gedanken- und Geviertstrich mit Leerzeichen steht jetzt ein geschütztes Leerzeichen (`layouts/_partials/dash-nbsp.html`, angewandt auf Lauftext, Einleitungen, Titel und Bildunterschriften).

Viertens wurde die Silbentrennung an die Elemente vererbt, wo sie nicht hingehört. Inline-Code wurde getrennt, und wer ihn kopiert, hätte einen falschen Bindestrich übernommen. Überschriften, Code und der Vorspann sind jetzt ausgenommen, und die Grenzen sind wie oben beschrieben angepasst.

Fünftens stehen im Lauftext jetzt Mediävalziffern, wie es Regel 5.2 der Typografie-Regeln nach Bringhurst empfiehlt. Crimson Pro hat sie, die gekürzte Schrift enthält dafür jetzt die Funktionen `onum` und `lnum` und wiegt 22,3 statt 19,6 Kilobyte. Der Vorspann behält Versalziffern wie die Titel.

Geschmackssache und offen sind: die Spalte mit den Nummern in der Projektliste, die auf dem Handy viel Breite kostet; weniger Abstand über dem Titel auf dem Handy; ein engerer Zeilenabstand für Codeblöcke (heute 171 Prozent); dieselbe rechte Kante für Vorspann und Lauftext auf dem Tablet; die Null mit Strich nur dort, wo sie Verwechslungen verhindert; die Kennzeichnung von Zitaten zugleich durch Kursiv, Linie und Einzug; größere Tippflächen für Navigation und Fußzeile. Vor einer deutschen Fassung fehlen das schmale Leerzeichen in beiden Schriften und Silbentrennung in den Abschnittsnamen, weil lange deutsche Wörter dort sonst ohne Trennstrich umbrechen.

## Zurück zum Raster aus halben Zeilen

Stand 06.11.2026. Mit eingezeichnetem Raster (rot ganze Zeilen, blau halbe) sah Max, dass Text stellenweise zwischen den Linien saß. Gemessen lag nach einer Bildunterschrift mit gerader Zeilenzahl der folgende Text eine Viertelzeile neben dem Raster, auf dem Handy ebenso alles vor Status und Stack. Ursache war das Raster aus Viertelzeilen: Der Abstand nach Abbildungen betrug 1¾ Zeilen, und drei Zeilen kleiner Schrift zu 20,25 Pixel ergeben 4½ halbe Zeilen. Die Prüfung war grün, weil sie auf Viertelzeilen prüfte, während das sichtbare Raster halbe Zeilen zeigt.

Max wollte den Zeilenabstand der Bildunterschriften von 138 Prozent behalten und den Text darunter auf eine Linie schieben. Das ist jetzt so gelöst: Das Raster besteht wieder aus halben Zeilen (`--baseline-grid: 0.5rlh`). Bildunterschriften sowie Status und Stack laufen weiter auf 20,25 Pixel, ihre erste Grundlinie liegt auf dem Raster, die folgenden Zeilen bewusst dazwischen. Ein kurzes Skript am Ende jeder Seite (`layouts/baseof.html`) misst diese Blöcke und polstert sie unten auf ganze halbe Zeilen auf, sodass der folgende Text wieder auf einer Linie steht. Es nutzt `ResizeObserver`, das laut MDN vor dem Zeichnen läuft, und läuft erneut, wenn Schrift oder Breite sich ändern. Unterschriften mit gerader Zeilenzahl bekommen eine halbe Zeile mehr, damit ihre letzte Zeile genug Abstand zum Text darunter hat. Nach Abbildungen folgen anderthalb Zeilen Abstand. Gemessen liegen über dem Bild 55,5 Pixel Weißraum und darunter 55,5 Pixel, nach einer Unterschrift mit gerader Zeilenzahl 62,25 Pixel. Ohne JavaScript kann der Text nach solchen Blöcken eine Viertelzeile neben dem Raster liegen.

Die Prüfung `tools/raster-check.mjs` prüft wieder auf halbe Zeilen. Bei kleiner Schrift auf 20,25 Pixel prüft sie nur die erste Grundlinie eines Blocks, dessen Höhe aber streng. Am 06.11.2026 lagen auf acht Seiten in fünf Ansichten alle geprüften Grundlinien auf dem Raster, und eine eigene Messung bestätigte, dass auf Desktop, Tablet und Handy der Text nach jeder Unterschrift wieder auf einer Linie steht.

## Linien auf dem Raster

Stand 06.11.2026. Mit eingezeichnetem Raster fragte Max, ob nicht auch die Linien auf dem Raster liegen müssten. Gemessen lagen die Linien über den Abschnitten und zwischen den Einträgen der Projektliste 7 Pixel unter einer Rasterlinie, also fast genau zwischen zwei Linien, und die Linie über der Fußzeile 9 Pixel, weil sie mit dem Text der Fußzeile um 2 Pixel verschoben wurde. Die Abstände der Kästen stimmten, nur die Linien selbst waren nicht ausgerichtet.

Max hat sich für die Variante entschieden, bei der die Linie über einem Abschnitt auf die Rasterlinie darunter rückt und der Abschnittsname anderthalb Zeilen unter ihr hängt. Die Linie gehört so sichtbar zum neuen Abschnitt: Vom Text davor sind es 94,5 Pixel Weißraum, zum eigenen Namen etwa 27. Jeder Wechsel zwischen Abschnitten wird dadurch eine halbe Zeile höher. Die Alternative, die Linie auf die Rasterlinie darüber zu setzen, hätte den Gesamtabstand gleich gelassen, die Linie aber näher an den vorigen Text gerückt. Die Trennlinien der Projektliste liegen jetzt auf der Rasterlinie genau in der Mitte zwischen zwei Einträgen, eine Zeile von der Grundlinie darüber und eine von der darunter. Die Linie über der Fußzeile liegt ebenfalls auf dem Raster. Verschoben wird dort nur noch der Link, nicht mehr die ganze Fußzeile.

Alle Linien nutzen denselben Versatz, `--rule-offset`, 6,5 Pixel unter der Oberkante ihres Kastens. Die Prüfung `tools/raster-check.mjs` prüft jetzt auch die Linien. Eine Gegenprobe mit dem alten Stylesheet hat gezeigt, dass sie verrutschte Linien findet. Am 06.11.2026 lagen alle Grundlinien und alle Linien auf acht Seiten in fünf Ansichten auf dem Raster.

## Offene Punkte

Stand 05.11.2026.

Domain: Es gibt noch keine eigene Domain. Wenn eine gekauft ist, folgt der Umzug wie oben beschrieben.

Schriftwahl: Söhne liegt nur als Desktop-Lizenz vor. Für die Website braucht es eine eigene Web-Lizenz. Alternativ sollen freie Schriften geprüft werden. Die gewählte Schrift wird dann selbst gehostet, also ohne Anfragen an fremde Server. Seit dem 05.11.2026 ist vorerst Inter eingebaut.

Inhalte der Projektseiten: Alle Texte sind noch Platzhalter. Max erarbeitet sie später Schritt für Schritt. Das betrifft auch den Einleitungsabsatz der Startseite, die Kurzbeschreibungen der Projekte sowie Status und Stack in jedem Projekt.

Impressum: Name und Kontakt sind noch einzutragen, und die Pflichtangaben sind vor dem Livegang zu prüfen.

Design: Das eigentliche Layout im Stil von Müller-Brockmann folgt in einer eigenen Runde. Seit dem 06.11.2026 gibt es dafür einen Entwurf, siehe Abschnitt "Design-Grundlagen für den Design-Durchgang". Nachtrag vom 06.11.2026: Das Layout ist umgesetzt und veröffentlicht.

Stand 06.11.2026, neue offene Punkte:

Optische Größe der Schrift: Display nur bei Überschriften oder überall ist noch nicht entschieden. Max vergleicht die Varianten mit dem lokalen Schalter. Wird die optische Größe auf einen Wert festgelegt, kann die Achse aus der Schrift entfallen. Gemessen am 06.11.2026 wird die Datei dadurch rund ein Drittel kleiner. Nachtrag vom 06.11.2026: Entschieden, Display überall, siehe Abschnitt "Schrift: Display überall und Laufweite".

Größenreihe: Die Größen 14,6, 45 und 58,5 Pixel stammen aus dem Entwurf und gehören keiner klassischen Reihe an. Möglich wäre eine Angleichung an 14, 48 und 60 Pixel. Nicht entschieden. Nachtrag vom 06.11.2026: Die Seitentitel stehen jetzt in 48, 60 und 72 Pixel, siehe Abschnitt "Grundlinienraster". Die kleine Größe von 14,6 Pixel bleibt vorerst.

CDN-Knoten warm halten: Gemessen am 06.11.2026 war jede Seite am Wiener Knoten von GitHub Pages nach 10 Minuten wieder kalt. Ein Treffer kostet 23 bis 30 Millisekunden, ein Fehltreffer 160 bis 190. Ein Abruf aller Dateien alle 5 Minuten vom Homeserver aus könnte den Knoten warm halten. Unbelegt ist, ob das auch für andere Besucher wirkt. Nicht umgesetzt.

Beschreibung der Startseite: Die Startseite hat keine Meta-Beschreibung für Suchmaschinen, weil ihr Text noch fehlt. Lighthouse meldet das. Der Text kommt mit den übrigen Inhalten.

Prüfung nach der Veröffentlichung: Service Worker auf der echten Seite, Test auf dem iPhone und eine Lighthouse-Messung gegen https://maxmser.github.io/. Eine Messung gegen `hugo server` taugt dafür nicht, weil der lokale Server ein Skript für das automatische Neuladen einbaut, nicht komprimiert und keine Cache-Angaben sendet.
