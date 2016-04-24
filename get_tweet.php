<?php
header('Access-Control-Allow-Origin: *');
error_reporting(-1);
if(isset($_GET['q']) && isset($_GET['limit'])){
	$q=$_GET['q'];
	$limit=$_GET['limit'];
	$ret=exec('python /var/www/html/Tweet-W/bot.py '.$q.' '.$limit,$output);
	echo $ret;
	echo PHP_EOL . implode(PHP_EOL, $output);
	header('Content-Type: application/json');
	$data=file_get_contents('response.json');
    echo $data;
	$ret=exec('python /var/www/html/Tweet-W/stream_bot.py '.$q,$output);
}
?>