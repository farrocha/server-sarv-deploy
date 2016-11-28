<?php
$Nombre = $_GET["File"]
rename("/home/sarv/SERVER_SARV_MONO/NoticiasCarga/" . $Nombre , "/home/sarv/SERVER_SARV_MONO/NoticiasVideo/" . $Nombre);
echo "Archivo movido"
?>

