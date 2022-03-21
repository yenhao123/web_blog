<?php
	$ip = $_GET['ip'];
	$ip = '140.123.84.0/24';
	//running
	$command = "python3 ../api/main.py --ip ".$ip." 2>err.txt ";
	echo shell_exec($command);
	echo 'finish';
?>

