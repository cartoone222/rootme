<?php
$ressource = fopen('index.php', 'rb');
echo fread($ressource, filesize('index.php'));
?>
