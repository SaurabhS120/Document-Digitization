<?php
set_time_limit(30);
echo "name : " . $_POST["name"];
$servername = "localhost";
$username = "root";
$password = "";
$database="doc_digit";
$doc_id=-1;
$docname=$_POST['name'];
$uid=$_POST['uid'];
$path_parts = pathinfo($_FILES["file"]["name"]);
$type=$path_parts['extension'];
// Create connection
$conn = new mysqli($servername, $username, $password,$database);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
$sql = "select MAX(doc_id) from docs;";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
  // output data of each row
  $row = $result->fetch_assoc();
  $doc_id=$row['MAX(doc_id)']+1;
} else {
  $doc_id=1;
}
$sql = "INSERT INTO `docs`(`doc_id`, `uid`, `doc_name`, `type`) VALUES ('".$doc_id."','".$uid."','".$docname."','".$type."')";

if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}
if(!is_dir('documents'))
	mkdir("documents");
echo 'Path : '."documents/" . $doc_id. '.' .$type;
move_uploaded_file($_FILES["file"]["tmp_name"],"documents/" . $doc_id. '.' .$type);
?>