<?php error_reporting( E_ALL );
echo "Archivo = {$_GET["File"]}";
echo rename("/home/sarv/SERVER_SARV_MONO/NoticiasCarga/{$_GET["File"]}", "/home/sarv/SERVER_SARV_MONO/NoticiasVideo/{$_GET["File"]}");
echo "        Archivo movido";
?>

