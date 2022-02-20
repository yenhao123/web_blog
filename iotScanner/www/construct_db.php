<?php
	$ip = $_GET['ip'];
	//$ip = '140.112.40.0/24';
	//update
	echo shell_exec("sh /var/www/html/ccu_proj_manyPorts/api/log/rm_sh.sh");		
	//running
	$command = "python3 /var/www/html/ccu_proj_manyPorts/api/main.py 2>a.txt --ip ".$ip;
	echo shell_exec($command);
	echo 'finish';
?>

