<?php

#const BIERDATEI = '/home/jgrundmann/Biermenge.txt';
const BIERDATEI = '/tmp/bier';

$bierstand = file_get_contents(BIERDATEI);
$speichere = static fn(string $menge) => file_put_contents(BIERDATEI, $menge);

$biermengeAusEingabe = static function (?array $postVars): ?int {
    $beerInLiter = (int)$postVars['biermenge'];

    return 0 <= $beerInLiter && $beerInLiter < 2000
        ? $beerInLiter
        : null;
};

if (array_key_exists('biermenge', $_REQUEST)
    && $mengeGetrunkeninLiter = $biermengeAusEingabe($_REQUEST)) {

    $speichere($mengeGetrunkeninLiter);
}
?>

<!doctype html>
<html lang="en" data-bs-theme="auto">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.112.5">
    <title>Biercounter - KG Silschede</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
</head>
<body class="d-flex align-items-center py-4 bg-body-tertiary">
    <main class="form-signin w-100 m-auto">
        <h1 class="h3 mb-3 fw-normal">KG Silschede Biercounter</h1>
        <div>Aktueller Stand: <?= $bierstand ?>L</div>

        <form action="index.php" method="POST">

            <div class="form-floating">
                <input type="text" class="form-control" name="biermenge" id="floatingInput" placeholder="775">
                <label for="floatingInput">Bier in Liter</label>
            </div>

            <button class="btn btn-primary w-100 py-2" type="submit">Saufen!</button>
            <p class="mt-5 mb-3 text-body-secondary">&copy; Gevelsberger Kirmes 2023</p>
        </form>
    </main>
</body>
</html>