<?php
    ini_set('error_reporting', E_ALL);
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    $connect = mysqli_connect('mysql-server', 'schedule', '12345678', 'schedule');
    mysqli_set_charset($connect,"utf8");
?>
