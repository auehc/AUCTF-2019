<?php
ob_start();
$ref = $_SERVER['HTTP_REFERER'];
if ( strpos($ref, '../restaurantcurrysecrets.php') == FALSE ){
	echo "No cheating!";
	header("Location: http://www.youtube.com/watch?v=dQw4w9WgXcQ");
}
else if ( strpos($ref, './home.html') == TRUE ){
	echo "<html>";
	if( isset($_POST["username"]) && isset($_POST["password"]) ){
		if($_POST["username"] == "zodiac" && $_POST["password"] == "Yoknapatawpha"){
			echo "aubie{1_Gu3$-Th3_fuz$-1$\_$7rong}";
		}
		else{
		}
	}
	else{
		echo "Username and password fields required";
	}	
#write a form such that they have to fuzz the user and pass
# U: zodiac P:Yoknapatawpha
}
else{
	header("Location: ./home.html");
}

?>

<html>
<body>
	<form action="tryme.php" method="POST">
		<p>
			Username: <br>
			<input type="text" name="username" align="justify"/><br>
			Password: <br>
			<input type="password" name="password" align="justify"/><br>
		</p>
		<center><input type="submit" value="Login"/></center>
	</form>
</body>
</html>
