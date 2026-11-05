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

Es gibt noch keine eigene Domain. Die Seite läuft vorerst unter https://maxmser.github.io/.

## Umzug auf eine eigene Domain

Stand 05.11.2026. Ursprünglich war geplant, dass für den Umzug auf eine Domain nur `baseURL` und eine CNAME-Datei nötig sind. Das stimmt für diesen Aufbau nicht ganz. Die GitHub-Dokumentation sagt, dass eine CNAME-Datei ignoriert wird und nicht nötig ist, wenn die Seite über einen eigenen GitHub-Actions-Workflow veröffentlicht wird. Die Domain wird stattdessen im Repository unter Settings, dann Pages, im Feld "Custom domain" eingetragen.

Für den Umzug braucht es deshalb drei Schritte. Erstens wird `baseURL` in `hugo.toml` auf die neue Domain geändert. Zweitens wird die Domain in den Pages-Einstellungen des Repositorys eingetragen. Drittens werden beim Domain-Anbieter die DNS-Einträge gesetzt, die GitHub in seiner Dokumentation nennt. Der Build im Workflow übernimmt die Adresse ohnehin aus den Pages-Einstellungen.

Quellen: GitHub Docs, "Troubleshooting custom domains and GitHub Pages" und "Managing a custom domain for your GitHub Pages site".

## Seitenstruktur

Stand 05.11.2026. Die Seite hat vier Arten von Seiten. Die Startseite zeigt den Titelsatz, einen kurzen Einleitungsabsatz und die Liste der Projekte. Die Projektübersicht unter `/projects/` listet alle Projekte. Jedes Projekt hat eine eigene Seite. Dazu kommt das Impressum unter `/imprint/`.

Die Layouts sind `baseof.html` als Grundgerüst, `home.html` für die Startseite, `list.html` für die Projektübersicht, `single.html` für Projektseiten und `text.html` für einfache Textseiten wie das Impressum. Dazu kommen drei kleine Teilvorlagen für die Navigation, die Projektliste und die Liste "More projects". Taxonomien und der RSS-Feed sind abgeschaltet, weil es keinen Blog gibt. Die Sitemap bleibt, weil sie Suchmaschinen hilft und keine externen Anfragen auslöst.

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

## Impressum

Stand 05.11.2026. Das Impressum ist ein Platzhalter mit den Feldern Name, Wohnort und Kontakt. Als Wohnort ist Wien eingetragen. Grundlage ist die Offenlegungspflicht nach § 25 Mediengesetz. Für kleine Websites, die nur ihren Inhaber vorstellen und nicht geeignet sind, die öffentliche Meinung zu beeinflussen, reicht eine verkürzte Offenlegung. Das Unternehmensserviceportal des Bundes (usp.gv.at) nennt dafür den Namen, den Wohnort und bei Unternehmen den Unternehmensgegenstand. Die genauen Pflichtangaben für eine private Person sollten vor dem Livegang noch einmal geprüft werden.

Eine Datenschutzseite gibt es nicht, solange kein Analytics läuft und keine Cookies gesetzt werden.

## Veröffentlichung

Stand 05.11.2026. Max hat die Veröffentlichung am 05.11.2026 freigegeben und selbst ausgeführt. Das öffentliche Repository ist https://github.com/maxmser/maxmser.github.io. Die Pages-Quelle wurde vor dem ersten Push über die GitHub-API auf "GitHub Actions" gestellt. Der erste Build und das Deployment liefen ohne Fehler durch. Die Seite ist unter https://maxmser.github.io/ erreichbar, vorerst noch mit Platzhaltern.

Für Commits ist als Autor "Max Moser" mit der anonymen GitHub-Adresse 275640851+maxmser@users.noreply.github.com eingetragen. Grund: Das Repository ist öffentlich, und die E-Mail-Adresse steht in jedem Commit für alle sichtbar. Die Einstellung gilt global für Git auf Max' Mac.

Die lokalen Git-Schritte führt Max selbst im Terminal aus. Claude arbeitet in einer Linux-VM, die zwar den Ordner sieht, aber nicht ins Terminal des Macs tippen kann und keine GitHub-Anmeldung hat.

## Vorerst nicht in Suchmaschinen

Stand 05.11.2026. Max hat entschieden, die Seite vorerst auf noindex zu setzen, solange sie nur Platzhalter enthält. Jede Seite trägt dafür im Kopf die Angabe `<meta name="robots" content="noindex">`. Gesteuert wird das über `noindex = true` im Abschnitt `[params]` in `hugo.toml`.

Bewusst gibt es keine robots.txt, die das Crawlen sperrt. Laut Google Search Central wirkt noindex nur, wenn der Crawler die Seite abrufen darf. Eine Sperre in robots.txt würde verhindern, dass er die noindex-Angabe überhaupt sieht.

Die Sitemap ist in dieser Zeit abgeschaltet, weil eine Sitemap mit Seiten, die nicht indexiert werden sollen, widersprüchliche Signale sendet.

Wenn die Inhalte fertig sind, sind zwei Schritte nötig. Erstens wird `noindex` in `hugo.toml` auf false gesetzt oder gelöscht. Zweitens wird "sitemap" wieder aus `disableKinds` entfernt.

## Schrift: vorerst Inter

Stand 05.11.2026. Max hat entschieden, vorerst Inter zu verwenden. Eingebaut ist Inter in der Version 4.1 als variable Schrift, also eine Datei für alle Schriftstärken, dazu eine zweite Datei für Kursiv. Inter steht unter der SIL Open Font License 1.1 und darf frei auf Websites verwendet werden. Die Lizenzdatei liegt neben den Schriftdateien in `static/fonts/inter/`.

Die Schrift wird selbst gehostet. Es gibt also keine Anfragen an Google Fonts oder andere fremde Server. Die Dateien stammen unverändert aus dem offiziellen Release auf GitHub (rsms/inter, Version 4.1 vom 16.11.2024). Die normale Schriftdatei wird im Seitenkopf vorgeladen, damit der Text schneller in Inter erscheint. Die Kursiv-Datei lädt der Browser nur, wenn auf einer Seite kursiver Text vorkommt.

Jede der beiden Dateien ist etwa 350 KB groß, weil sie alle Schriftsysteme von Inter enthält, auch Kyrillisch, Griechisch und Vietnamesisch. Man könnte sie später auf lateinische Zeichen kürzen. Das würde die Ladezeit beim ersten Besuch spürbar senken.

Inter ist eine Zwischenlösung. Die endgültige Schriftwahl bleibt offen, siehe unten.

## Offene Punkte

Stand 05.11.2026.

Domain: Es gibt noch keine eigene Domain. Wenn eine gekauft ist, folgt der Umzug wie oben beschrieben.

Schriftwahl: Söhne liegt nur als Desktop-Lizenz vor. Für die Website braucht es eine eigene Web-Lizenz. Alternativ sollen freie Schriften geprüft werden. Die gewählte Schrift wird dann selbst gehostet, also ohne Anfragen an fremde Server. Seit dem 05.11.2026 ist vorerst Inter eingebaut.

Inhalte der Projektseiten: Alle Texte sind noch Platzhalter. Max erarbeitet sie später Schritt für Schritt. Das betrifft auch den Einleitungsabsatz der Startseite, die Kurzbeschreibungen der Projekte sowie Status und Stack in jedem Projekt.

Impressum: Name und Kontakt sind noch einzutragen, und die Pflichtangaben sind vor dem Livegang zu prüfen.

Design: Das eigentliche Layout im Stil von Müller-Brockmann folgt in einer eigenen Runde.
