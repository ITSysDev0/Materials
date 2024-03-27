<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <form action="sample.php" method="post">
        <button type="submit" name="set" class="button1">Set</button>

        <input type="text" name="id_number" id="id_number" class="text1" placeholder="Input_ID">
        <button type="submit" name="number" class="button2">Set Number</button>
    </form>
</body>
<?php
$data = $_POST['id_number'];
// if(isset($_POST['set'])){
//         // Universal Config
//     require_once('config.php');
//     $sql = "INSERT INTO on_tb (data) VALUES (1)";
//     mysqli_query($link,$sql);
//     mysqli_close($link);
// }
if(isset($_POST['set'])){
    // Universal Config
require_once('config.php');
$sql = "SELECT id FROM on_tb ORDER BY id DESC LIMIT 1";
$result = mysqli_query($link,$sql);
$row = mysqli_fetch_array($result);
print($row['id']);
}
if(isset($_POST['number'])){
    require_once('config.php');
    $sql = "SELECT date_time FROM on_tb WHERE id = $data";
    $result = mysqli_query($link,$sql);
    $row = mysqli_fetch_array($result);
    print($row['date_time']);
    //mysqli_close($link);
}
?>
</html>