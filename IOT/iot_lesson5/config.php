<?php 

class Database_Connection
{
    private $host = "localhost";
    private $user = "db_sys";
    private $password = "P@ssword";
    private $db = "on_db";

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

?>