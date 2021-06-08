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
$sql = "SELECT * FROM blocked WHERE uid='".$uid."';";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  echo 'true';
}
else{
    echo 'false';
}
$conn->close();
?>