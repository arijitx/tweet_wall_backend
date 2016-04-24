<?php
header('Access-Control-Allow-Origin: *');
error_reporting(-1);
header('Content-Type: application/json');
$data=file_get_contents('analytics.json');
echo $data;
?>