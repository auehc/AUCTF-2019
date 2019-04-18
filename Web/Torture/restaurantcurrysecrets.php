<?php

echo "<html>";
echo "Request it";

if ( isset($_POST) ){
	echo "Close, but no cigar. Try again";
}
elseif ( isset($_HEAD) ){
	echo "Good!, You may proceed.";
	echo "Go to ./uploads/tryme.php";
}
else {
	echo "Invalid request.";
}

echo "</html>"
?>
