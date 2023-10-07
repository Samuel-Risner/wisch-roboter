# wisch-roboter - Web UI

Dieser Zweig kümmert sich um das Web Interface.

# Minimierte Version von `index.html` erstellen

1. NodeJS und Python müssen installiert sein
2. TailwindCSS bauen:

```shell
npm run build_tw
```

3. Minimieren:

```shell
python kompilieren.py
```

Schritte 2 und 3 können abgekürzt werden:

```shell
npm run build
```

# Dateien welche durch das minimieren entstehen

Durch das erstellen der minimierten Version von `index.html` werden die Dateien `kompiliert.html`, `kompiliert.ino` und `output.css` erstellt.

`output.css` enthält das von TailwindCSS erstellte CSS, welches in `kompiliert.html` und `kompiliert.ino` verwendet wird.

`kompiliert.html` ist eine minimierte Version von `index.html` in welche das CSS von `output.css` eingefügt wurde.

`kompiliert.ino` enthält eine C++ Funktion welche den Inhalt von `kompiliert.html` verwendet.

# Verwendung in anderen Zweigen

Andere Zweige welche die Funktion in `kompiliert.ino` verwenden:

(Momentan gibt es noch keine anderen Zweige.)

# Lizenz

Dieser Zweig steht unter der MIT Lizenz zur Verfügung. Weitere Infos befinden sich in der Datei `LICENSE`.

Von der Lizenz ausgenommen sind die Dateien unter `SVGs/`, da diese von [Solar Icons](https://www.svgrepo.com/author/Solar%20Icons/) unter der [CC Attribution License](https://www.svgrepo.com/page/licensing/#CC%20Attribution) veröffentlicht wurden. Weitere Infos befinden sich unter `SVGs/LICENSE`.

- [`black-hole-svgrepo-com.svg`](https://www.svgrepo.com/svg/528043/black-hole)
- [`close-circle-svgrepo-com.svg`](https://www.svgrepo.com/svg/527651/close-circle)
- [`square-arrow-left-up-svgrepo-com.svg`](https://www.svgrepo.com/svg/528650/square-arrow-left-up)
- [`square-arrow-up-svgrepo-com.svg`](https://www.svgrepo.com/svg/528653/square-arrow-up)

Die SVGs wurden in der Datei `index.html` verwendet, welche in minimierter Form in anderen Zweigen dieses Repos verwendet wird.

Bei all den SVGs wurden die `width` und `height` Attribute entfernt und sie wurden mit CSS Skaliert und ggf. gedreht. Manchmal wurden auch `id` attribute hinzugefügt.
