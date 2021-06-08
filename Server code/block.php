<?php
set_time_limit(30);
$servername = "localhost";
$username = "root";
$password = "";
$database="doc_digit";
$doc_id=-1;
$uid=$_POST['uid'];
// Create connection
$conn = new mysqli($servername, $username, $password,$database);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO `blocked`(`uid`) VALUES ('".$uid."')";

if ($conn->query($sql) === TRUE) {
  echo "true";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}
?>