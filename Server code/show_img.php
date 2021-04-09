<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "doc_digit";
$doc_id=$_POST['doc_id'];
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
$sql = "SELECT type FROM docs WHERE doc_id='".$doc_id."';";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  if($row = $result->fetch_assoc()) {
	  $type=$row['type'];
  }
}
$conn->close();

header("Location: "."http://localhost/documents/".$doc_id.".".$type);
?>