<?php
	$ip = $_GET['ip'];
	$ip = '140.123.84.0/24';
	//running
	$command = "python3 ../api/main.py 2>err.txt --ip ".$ip;
	echo shell_exec($command);
	echo 'finish';
?>

