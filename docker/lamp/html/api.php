<?php
header('Access-Control-Allow-Origin: *');
    ini_set('error_reporting', E_ALL);
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    header('Content-type: json/application');
    require './connect.php';
    require './functions.php';
    $url = $_SERVER['REQUEST_URI'];
    $url_components = parse_url($url);

    parse_str($url_components['query'], $params);

    if(isset($params['group_id'])){
        getSchedule($params['group_id'], $connect);
    }

    if(isset($params['all'])){
        getAll($connect);
    }
?>


