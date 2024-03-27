<?php
//* Database
    // Universal Config
    class Database_Connection
    {
        private $host = "localhost";
        private $user = "db_sys";
        private $password = "P@ssword";
        private $db = "env_db";

        public function __construct()
        {
        
            $conn = mysqli_connect($this -> host, $this -> user, $this -> password, $this -> db);

            if($conn->connect_error)
            {
                die ("<h1>Database Connection Failed</h1>");
            }
            //echo "Database Connected Successfully";
            return $this->conn = $conn;
        }
    }
    $db = new Database_Connection;
    $link = $db->conn;
    
$result = mysqli_query($link,'SELECT * FROM env_tb ORDER by id DESC LIMIT 1');
$row = mysqli_fetch_array($result);
$data_arr=array($row['id'],$row['date_time'],$row['sensor_id'],$row['temp'],$row['hum'],$row['lux'],$row['volt']);
$datas = json_encode($data_arr);
echo $datas;
?>