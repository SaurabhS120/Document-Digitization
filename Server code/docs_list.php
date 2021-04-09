<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "doc_digit";
$uid=$_POST['uid'];
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
$sql = "SELECT doc_name,doc_id FROM docs WHERE uid='".$uid."';";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  $first=true;
  while($row = $result->fetch_assoc()) {
	if($first){
		echo $row["doc_name"].":".$row["doc_id"];
		$first=false;
	}
	else
		echo ",".$row["doc_name"].":".$row["doc_id"];
  }
}
$conn->close();
?>